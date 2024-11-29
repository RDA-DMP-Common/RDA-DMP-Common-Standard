import pandas as pd
import json
import numpy as np
import urllib.parse
import re


"""
Python script to generate a JSON schema from a Orange Tab

need to add title to general_info
"""

# Function to build a nested dictionary for a given path
def build_nested_dict(keys, value, parent_path):
    if len(keys) == 1:
        # Add the $id and title for the field
        value["$id"] = f"{parent_path}/properties/{keys[0]}"
        value["title"] = f"{keys[0].capitalize()}"
        return {keys[0]: value}

    # Create an intermediate object for nested data structure
    nested_object = {
        "$id": f"{parent_path}/properties/{keys[0]}",
        "type": "object",
        "title": f"{keys[0].capitalize()}",
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
old_copy_google_sheet_id = '1rVqYqZzZU_W4qR3C3ea8PVVIakCFP40jFI6rAsTGeQA'
worksheet_name = 'GC maDMP Master Sheet'
# URL-encode the worksheet name
encoded_worksheet_name = urllib.parse.quote(worksheet_name)
# Construct the URL for the CSV export
url = f'https://docs.google.com/spreadsheets/d/{old_copy_google_sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_worksheet_name}'
#url = f'https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_worksheet_name}'

# Read the data into a pandas DataFrame
df = pd.read_csv(url, encoding='utf-8')

# Columns that are necessary to generate the schema
kept_columns = ["Data type", "Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)",
                'Allowed Values\n(for JSON schema file)', 'Example value', 'Description', 
                'Front-end user-friendly question', 'GC DMP Requirement', 'required when',
                ## newly added column
                '"required IF/WHEN" dependency', 'Cardinality', 'conditional appear prerequisite path', 
                'conditional appear prerequisite value', 'Logic order of subquestions under each chapter'
                ]

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

# sort the dataframe based on the 'logic order of subquestions under each chapter' column
# Define a function to split the string into a list of integers
def sort_key(value):
    if pd.isna(value):
        return [100]
    #print(value)
    return [int(x.strip()) for x in str(value).split('.')]
# Sort the column by the parsed numeric values
df_sorted = df.sort_values(by='Logic order of subquestions under each chapter', key=lambda col: col.map(sort_key))
# Reset index if necessary
df_sorted = df_sorted.reset_index(drop=True)


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
## newly added column
conditional_appear_dict = {}
one_to_n_array_list = []
zero_to_n_array_list = []
require_when_nested_structure_exist = {}
chapter_1_dict = {}

# Iterate through each row and construct the schema
for _, row in df_sorted.iterrows():
    
    # filter out the rows with empty values
    if pd.isna(row['Data type']) or pd.isna(row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)']) or pd.isna(row['Logic order of subquestions under each chapter']):
        continue 

    field_path = row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].split('/')
    data_type = row['Data type'].lower()  # Convert to lowercase for easier matching
    allowed_values = row['Allowed Values\n(for JSON schema file)']
    example_value = row['Example value']
    description = row['Description']
    question = row['Front-end user-friendly question']
    format = row['format']
    requirement = row['GC DMP Requirement']  # New column for requirement
    required_when = row['required when']
    ## newly added column
    required_IF_dependency = row['"required IF/WHEN" dependency']
    cardinality = row['Cardinality']
    prerequisite_path = row['conditional appear prerequisite path']
    prerequisite_values = row['conditional appear prerequisite value']
    order = str(row['Logic order of subquestions under each chapter']).split('.')


    # delete filters certain fields
    # filters level 2 fields
    """
    if "dataset" in field_path:
        if len(field_path) != 2:
            if "dataset_documentation" not in field_path: # and "cost" not in field_path:
                continue
    else:
        continue
    """
    # filters level 1 fields
    #if "dataset_documentation" not in field_path: # and "cost" not in field_path:
    #    continue
    #if order[0] > '2':
    #    continue

    parent_path = "/".join(field_path[:-1])
    child_name = field_path[-1]

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
        if parent_path not in require_when_nested_structure_exist:
            require_when_nested_structure_exist[parent_path] = []
        require_when_nested_structure_exist[parent_path].append(child_name)

    # find the chapter 1 properties
    if order[0] == '1' and len(order) == 2:
        if parent_path not in chapter_1_dict:
            chapter_1_dict[parent_path] = []
        chapter_1_dict[parent_path].append(child_name)
    

    # Check if the current field is required
    if pd.notna(requirement) and requirement.strip().lower() == 'required':
        #parent_path = "/".join(field_path[:-1])
        #child_name = field_path[-1]

        # Add the child name to the required fields for the parent path
        if parent_path not in required_fields_dict:
            required_fields_dict[parent_path] = []
        required_fields_dict[parent_path].append(child_name)

    ## newly added column
    # build dependencies, check "required IF" condition
    if pd.notna(required_IF_dependency) and requirement.strip().lower() == 'required if':
        if pd.notna(prerequisite_path) and pd.notna(prerequisite_values):
            prerequisite = prerequisite_path.split('/')[-1]
            prerequisite_values = [x.strip() for x in prerequisite_values.split(',')]

            if parent_path not in conditional_appear_dict:
                conditional_appear_dict[parent_path] = []
            conditional_appear_dict[parent_path].append((child_name, prerequisite, prerequisite_values))
        else:
            print("Error: the required_IF_dependency is not in the correct format")

    
    # Check if the current field is an array (cardinality = 1..n)
    if pd.notna(cardinality) and cardinality.strip().lower() == '1..n':
        array_path = "/".join(field_path)
        one_to_n_array_list.append(array_path)
    
    # Check if the current field is an array (cardinality = 0..n)
    if pd.notna(cardinality) and cardinality.strip().lower() == '0..n':
        array_path = "/".join(field_path)
        zero_to_n_array_list.append(array_path)

            
    # Create the nested dictionary for this field path, adding $id and title dynamically
    nested_dict = build_nested_dict(field_path, schema_object, "#")

    # Merge the nested dictionary into the base schema properties
    merge_dicts(json_schema['properties'], nested_dict)

def convert_links_to_html(paragraph):
    """
    Detects https links in a paragraph and converts them to HTML format.
    Preserves links already in HTML format.
    
    :param paragraph: Input text containing links.
    :return: Text with links converted to HTML.
    """
    def replace_link(match):
        url = match.group(1)
        # Customize link content here
        content = url.split("/")[2]  # Use domain as content
        return f'<a href="{url}">{content}</a>'
    
    regex = r'(?<!<a href=")(https://[^\s<]+)(?!">)'
    return re.sub(regex, replace_link, paragraph)

# Assign required fields to the correct parent objects in the JSON schema
def assign_required_fields(schema, path=""):
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            current_path = f"{path}/{prop_name}".strip("/")
            if current_path in required_fields_dict:
                prop_value["required"] = required_fields_dict[current_path]

            ## newly added column
            # add requiredWhen fields
            if current_path in require_when_nested_structure_exist:
                if "required" not in prop_value:
                    prop_value["required"] = []
                prop_value["required"].extend(require_when_nested_structure_exist[current_path])

            # convert https to http links in the description
            if "description" in prop_value:
                prop_value["description"] = convert_links_to_html(prop_value["description"])

            assign_required_fields(prop_value, current_path)

def apply_conditionals_appear(schema, path=""):
    """
    for now, conditions are all required IF
    1. some options are chosen in the prerequisite fields
    2. some values are entered into the prerequisite fields
    """
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            current_path = f"{path}/{prop_name}".strip("/")
            # add conditional appear fields
            if current_path in conditional_appear_dict:
                #print(current_path)
                temp_list= []
                for child_name_pair in conditional_appear_dict[current_path]:
                    child_name = child_name_pair[0]
                    prerequisite = child_name_pair[1]
                    prerequisite_values = child_name_pair[2]

                    if prerequisite_values[0] == "special!!!": # condition2
                        appearing_sub_schemas = {
                                            "if": {
                                                "properties": {
                                                    prerequisite: {
                                                    prerequisite_values[1]: int(prerequisite_values[2])
                                                    }
                                                }
                                            },
                                            "then": {
                                                "properties": {
                                                    child_name: prop_value["properties"].pop(child_name)
                                                },
                                                "required": [
                                                    child_name
                                                ]
                                            }
                                        }
                        temp_list.append(appearing_sub_schemas)
                    else: # condition1
                        appearing_sub_schemas = {
                                            "if": {
                                                "properties": {
                                                    prerequisite: {
                                                    "enum": prerequisite_values
                                                    }
                                                }
                                            },
                                            "then": {
                                                "properties": {
                                                    child_name: prop_value["properties"].pop(child_name)
                                                },
                                                "required": [
                                                    child_name
                                                ]
                                            }
                                        }
                        temp_list.append(appearing_sub_schemas)
                #print(json.dumps(temp_list, indent=4))
                if "allOf" not in prop_value:
                    prop_value["allOf"] = []
                prop_value["allOf"].extend(temp_list)

            # add requiredWhen fields
            #if current_path in require_when_nested_structure_exist:
            #    if "required" not in prop_value:
            #        prop_value["required"] = []
            #    prop_value["required"].extend(require_when_nested_structure_exist[current_path])


            apply_conditionals_appear(prop_value, current_path)

# add array layer in schemas (move the properties into the array layer)
def add_array_layer(schema, path=""):
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            current_path = f"{path}/{prop_name}".strip("/")

            ## newly added column
            # add array layer 
            if current_path in one_to_n_array_list:
                schema["properties"][prop_name] = {
                    'type': 'array',
                    'items': prop_value,
                    'minItems': 1
                }

            if current_path in zero_to_n_array_list:
                schema["properties"][prop_name] = {
                    'type': 'array',
                    'items': prop_value
                }

            add_array_layer(prop_value, current_path)

# move chapter 1 properties to under chapter 1 (general info) level
def move_to_chapter_1(schema, path=""):
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            current_path = f"{path}/{prop_name}".strip("/")
            if current_path in chapter_1_dict:

                chapter_1_properties = {}
                chapter_1_required_list = []
                for property in chapter_1_dict[current_path]:
                    chapter_1_properties[property] = prop_value["properties"].pop(property)

                    # remove the required fields from the parent object
                    if property in schema["properties"][prop_name]["required"]:
                        schema["properties"][prop_name]["required"].remove(property)
                        chapter_1_required_list.append(property)

                schema["properties"][prop_name]["properties"]["general_info"]= {
                    "type": "object",
                    "properties": chapter_1_properties,
                    "required": chapter_1_required_list
                }



            move_to_chapter_1(prop_value, current_path)

assign_required_fields(json_schema)
apply_conditionals_appear(json_schema)
add_array_layer(json_schema)
move_to_chapter_1(json_schema)

# move the chapter 1 properties to the top level
temp_dmp = json_schema["properties"]["dmp"]["properties"]
temp_reordered_dmp = {"general_info": temp_dmp.pop("general_info"), **temp_dmp}
json_schema["properties"]["dmp"]["properties"] = temp_reordered_dmp
#print(json.dumps(chapter_1_dict, indent=4))


# Output the generated JSON schema as a JSON file or print it out
with open('GCWG-RDA-maDMP-schema.json', 'w', encoding='utf-8') as f:
    json.dump(json_schema, f, indent=4, ensure_ascii=False)

print("JSON schema has been generated successfully!")
"""
# Or, print it out to see the result
print(json.dumps(json_schema, indent=4))
"""
