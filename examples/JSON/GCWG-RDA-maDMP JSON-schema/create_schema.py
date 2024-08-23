import pandas as pd
import json
import numpy as np
import urllib.parse

# Function to build a nested dictionary for a given path
def build_nested_dict(keys, value, parent_path):
    if len(keys) == 1:
        # Add the $id and title for the field
        value["$id"] = f"{parent_path}/properties/{keys[0]}"
        value["title"] = f"The {keys[0].capitalize()} Schema"
        return {keys[0]: value}

    # Create an intermediate object for nested data structure
    nested_object = {
        "$id": f"{parent_path}/properties/{keys[0]}",
        "type": "object",
        "title": f"The {keys[0].capitalize()} Schema",
        "properties": {}
    }

    # Recursively build the nested object
    nested_object["properties"] = build_nested_dict(keys[1:], value, nested_object["$id"])

    return {keys[0]: nested_object}

# Function to merge dictionaries, handling cases where non-nested values exist
def merge_dicts(d1, d2):
    for key in d2:
        if key in d1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            merge_dicts(d1[key], d2[key])
        else:
            d1[key] = d2[key]

# Load the CSV file (adjust the path as necessary)
google_sheet_id = '1OfY5dKEfbvFhlhBjRb4UfdPKqQiB9mjZwe_60R7mu-A'
worksheet_name = 'GC maDMP Master Sheet'
# URL-encode the worksheet name
encoded_worksheet_name = urllib.parse.quote(worksheet_name)
# Construct the URL for the CSV export
url = f'https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_worksheet_name}'

# Read the data into a pandas DataFrame
df = pd.read_csv(url, encoding='utf-8')

# Columns that are necessary to generate the schema
kept_columns = ["Data type", "Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)",
                'Allowed Values\n(for JSON schema file)', 'Example value', 'Description', 
                'Front-end user-friendly question', 'GC DMP Requirement', 'required when']

# Adjust data types based on patterns
df["Data type"] = np.where(df["Data type"].str.contains('controlled vocabulary', case=True, na=False), "controlled vocabulary", df['Data type'])
df["Data type"] = np.where(df["Data type"].str.contains('DateTime.', case=True, na=False), "date-time", df['Data type'])
df["Data type"] = np.where(df["Data type"].str.contains('Date.', case=True, na=False), "date", df['Data type'])
df["Data type"] = np.where(df["Data type"].str.contains('string', case=True, na=False), "string", df['Data type'])

df["Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)"] = df["Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)"].str.rstrip("/")
df['format'] = None

# Set the format based on data type
df.loc[df['Data type'] == 'date', 'format'] = 'date'
df.loc[df['Data type'] == 'date-time', 'format'] = 'date-time'
df.loc[df['Data type'] == 'URI', 'format'] = 'uri'
df.loc[df['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].str.contains('mbox', case=False, na=False), 'format'] = 'email'

# Initialize the base schema
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/FAIRERdata/maDMP-Standard/blob/Master/examples/JSON/GCWG-RDA-maDMP JSON-schema/GCWG-RDA-maDMP-schema.json",  # Update this to the appropriate $id
    "title": "GCWG-RDA-maDMP-Schema",  # schema title
    "type": "object",
    "properties": {},
    "additionalProperties": False,
    "required": ["dmp"]  # Add "dmp" to the top-level required array
}

# A dictionary to track the required fields at each level
required_fields_dict = {}

# Iterate through each row and construct the schema
for _, row in df.iterrows():
    field_path = row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].split('/')
    data_type = row['Data type'].lower()  # Convert to lowercase for easier matching
    allowed_values = row['Allowed Values\n(for JSON schema file)']
    example_value = row['Example value']
    description = row['Description']
    question = row['Front-end user-friendly question']
    format = row['format']
    requirement = row['GC DMP Requirement']  # New column for requirement
    required_when = row['required when']

    # Determine JSON schema type based on the data type
    if "date_time" in data_type:
        json_type = "string"
    elif "date" in data_type:
        json_type = "string"
    elif "nested data structure" in data_type:
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

    # Add Description if not empty
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

    # Check if the current field is required
    if pd.notna(requirement) and requirement.strip().lower() == 'required':
        parent_path = "/".join(field_path[:-1])
        child_name = field_path[-1]

        # Add the child name to the required fields for the parent path
        if parent_path not in required_fields_dict:
            required_fields_dict[parent_path] = []
        required_fields_dict[parent_path].append(child_name)

    # Create the nested dictionary for this field path, adding $id and title dynamically
    nested_dict = build_nested_dict(field_path, schema_object, "#")

    # Merge the nested dictionary into the base schema properties
    merge_dicts(json_schema['properties'], nested_dict)

# Assign required fields to the correct parent objects in the JSON schema
def assign_required_fields(schema, path=""):
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            current_path = f"{path}/{prop_name}".strip("/")
            if current_path in required_fields_dict:
                prop_value["required"] = required_fields_dict[current_path]
            assign_required_fields(prop_value, current_path)

assign_required_fields(json_schema)

# Output the generated JSON schema as a JSON file or print it out
with open('GCWG-RDA-maDMP-schema.json', 'w', encoding='utf-8') as f:
    json.dump(json_schema, f, indent=4, ensure_ascii=False)

# Or, print it out to see the result
print(json.dumps(json_schema, indent=4))
