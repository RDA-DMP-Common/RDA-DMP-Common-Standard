import pandas as pd
import json
import numpy as np

# Function to build a nested dictionary for a given path
def build_nested_dict(keys, value, parent_path, required_fields):
    if len(keys) == 1:
        # Add the $id and title for the field
        value["$id"] = f"{parent_path}/properties/{keys[0]}"
        value["title"] = f"The {keys[0].capitalize()} Schema"
        
        # If the field is required, add it to the required fields list
        if keys[0] in required_fields:
            return {keys[0]: value}, keys[0]
        else:
            return {keys[0]: value}, None
    
    # Create an intermediate object for nested data structure
    nested_object = {
        "$id": f"{parent_path}/properties/{keys[0]}",
        "type": "object",
        "title": f"The {keys[0].capitalize()} Schema",
        "properties": {}
    }
    
    # Recursively build the nested object
    nested_object["properties"], child_required = build_nested_dict(keys[1:], value, nested_object["$id"], required_fields)
    
    # If any child is required, add it to the parent required list
    if child_required:
        nested_object.setdefault("required", []).append(child_required)
    
    return {keys[0]: nested_object}, None

# Function to merge dictionaries, handling cases where non-nested values exist
def merge_dicts(d1, d2):
    for key in d2:
        if key in d1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            merge_dicts(d1[key], d2[key])
        else:
            d1[key] = d2[key]

# Load the CSV file (adjust the path as necessary)
df = pd.read_csv('input/dmp_structure.csv', encoding='ISO-8859-1')

# Adjust data types based on patterns
df["data_type"] = np.where(df["data_type"].str.contains('controlled vocabulary', case=True, na=False), "controlled vocabulary", df['data_type'])
df["data_type"] = np.where(df["data_type"].str.contains('DateTime.', case=True, na=False), "date-time", df['data_type'])
df["data_type"] = np.where(df["data_type"].str.contains('Date.', case=True, na=False), "date", df['data_type'])
df["data_type"] = np.where(df["data_type"].str.contains('string', case=True, na=False), "string", df['data_type'])

df["fieldname"] = df["fieldname"].str.rstrip("/")
df['format'] = None

# Set the format based on data type
df.loc[df['data_type'] == 'date', 'format'] = 'date'
df.loc[df['data_type'] == 'date-time', 'format'] = 'date-time'
df.loc[df['data_type'] == 'URI', 'format'] = 'uri'
df.loc[df['fieldname'].str.contains('mbox', case=False, na=False), 'format'] = 'email'

# Initialize the base schema
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/FAIRERdata/maDMP-Standard/blob/Master/examples/JSON/GC-RDA JSON-schema/GC-RDA-maDMP-schema.json",  # Update this to the appropriate $id
    "title": "GC-RDA maDMP Schema",  # Add a meaningful title for your schema
    "type": "object",
    "properties": {}
}

# Iterate through each row and construct the schema
for _, row in df.iterrows():
    field_path = row['fieldname'].split('/')
    data_type = row['data_type'].lower()  # Convert to lowercase for easier matching
    allowed_values = row['allowed_values']
    example_value = row['example_value']
    description = row['description']
    question = row['question']
    format = row['format']
    requirement = row['requirement']  # New column for requirement
    required_when = row['required when']

    # Determine JSON schema type based on the data type
    if "date_time" in data_type:
        json_type = "string"
    elif "date" in data_type:
        json_type = "string"
    elif data_type == "nested data structure":
        json_type = "object"
    elif data_type == "controlled vocabulary":
        json_type = "string"
    elif data_type == "uri":
        json_type = "string"  # JSON schema uses string for URIs
    else:
        json_type = data_type

    # Build the schema object for the current field
    schema_object = {
        "type": json_type
    }

    # Add description if not empty
    if pd.notna(description) and description.strip():
        schema_object["description"] = description

    if pd.notna(allowed_values):
        schema_object["enum"] = [v.strip() for v in allowed_values.split(',')]

    if pd.notna(example_value):
        schema_object["example"] = example_value

    if pd.notna(question):
        schema_object["question"] = question

    if pd.notna(format):
        schema_object["format"] = format
    
    if pd.notna(required_when):
        schema_object["requiredWhen"] = [v.strip() for v in required_when.split(',')]

    # Collect required fields
    required_fields = []
    if pd.notna(requirement) and requirement.strip().lower() == 'required':
        required_fields.append(field_path[-1])

    # Create the nested dictionary for this field path, adding $id and title dynamically
    nested_dict, required_field = build_nested_dict(field_path, schema_object, "#", required_fields)

    # Merge the nested dictionary into the base schema properties
    merge_dicts(json_schema['properties'], nested_dict)

    # If the current field is required, add it to the required list
    if required_field:
        json_schema.setdefault("required", []).append(required_field)

# Output the generated JSON schema as a JSON file or print it out
with open('GC-RDA-maDMP-schema.json', 'w') as f:
    json.dump(json_schema, f, indent=4)

# Or, print it out to see the result
print(json.dumps(json_schema, indent=4))
