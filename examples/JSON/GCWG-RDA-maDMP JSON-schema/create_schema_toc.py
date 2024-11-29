import pandas as pd
import json
import numpy as np
import urllib.parse

"""
Depreciated: This script is no longer used. The TOC is now generated in the maDMP-Generation-Form.
"""

'''
This script generates the Table of Contents (TOC) in for the maDMP schema based on the Orange Tab. 
- The TOC is in the form of html, and can be immediately used in the form at https://github.com/FAIRERdata/maDMP-Generation-Form.
- The file is saved as table_of_contents.html in the current directory. Its information should be added to the metadata file.
'''

# Function to build a nested dictionary for a given path
def build_nested_dict(keys, value, parent_path):
    if len(keys) == 1:
        # Add the $id and title for the field
        value["$id"] = f"{parent_path}_{keys[0]}"
        value["title"] = f"{keys[0]}"
        value["array"] = False
        return {keys[0]: value}

    # Create an intermediate object for nested data structure
    nested_object = {
        "$id": f"{parent_path}_{keys[0]}",
        "type": "object",
        "title": f"{keys[0]}",
        "array": False,
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
#df = pd.read_csv(url, encoding='utf-8')
df = pd.read_excel('GC-RDA maDMP Excel Workbook.xlsx', sheet_name='GC maDMP Master Sheet')

# Columns that are necessary to generate the schema
kept_columns = [ "Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)",
                "Logic order of subquestions under each chapter", 'Cardinality']

# Adjust data types based on patterns
df["Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)"] = df["Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)"].str.rstrip("/")

# Set the format based on data type
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


# Initialize the draft of ui schema
toc_draft = {
}

chapter_1_list = []
array_list = []

# Iterate through each row and construct the schema
for _, row in df_sorted.iterrows():
    
    # filter out the rows with empty values
    if pd.isna(row['Data type']) or pd.isna(row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)']) or pd.isna(row['Logic order of subquestions under each chapter']):
        continue 

    field_path = row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].split('/')
    order = str(row['Logic order of subquestions under each chapter']).split('.')
    cardinality = str(row['Cardinality'])


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


    # Build the schema object for the current field
    schema_object = {
    }


    # find the chapter 1 properties
    if order[0] == '1' and len(order) == 2:
        chapter_1_list.append(child_name) 

    # Check if the current field is an array (cardinality = 1..n)
    if pd.notna(cardinality) and cardinality.strip().lower() == '1..n' or cardinality.strip().lower() == '0..n':
        array_path = "/".join(field_path)
        array_list.append(array_path)

            
    # Create the nested dictionary for this field path, adding $id and title dynamically
    nested_dict = build_nested_dict(field_path, schema_object, "root")

    # Merge the nested dictionary into the base schema properties
    merge_dicts(toc_draft, nested_dict)

# move chapter 1 properties to under chapter 1 (general info) level
def move_to_chapter_1(schema, path=""):

    chapter_1_properties = {}
    for property in chapter_1_list:
        chapter_1_properties[property] = schema.pop(property)

    temp_schema = {}
    temp_schema["general_info"]= {
        "$id": "root_dmp_general_info",
        "title": "general info",
        "type": "object",
        "properties": chapter_1_properties,
    }
    temp_schema.update(schema)

    return temp_schema

# add array layer in schemas (move the properties into the array layer)
def add_array_layer(schema, path="dmp"):
    if isinstance(schema, dict):
        if "properties" in schema:
            for prop_name, prop_value in schema["properties"].items():
                current_path = f"{path}/{prop_name}".strip("/")
                #print(current_path)

                # add array layer 
                if current_path in array_list:
                    print(prop_name)
                    schema["properties"][prop_name]["array"] = True

                add_array_layer(prop_value, current_path)

def add_general_info_2_id(schema, path='root_dmp_general_info'):
    if "properties" in schema:
        for prop_name, prop_value in schema["properties"].items():
            prop_value["$id"] = f"{path}_{prop_name}"

            add_general_info_2_id(prop_value, f"{path}_{prop_name}")

add_array_layer(toc_draft["dmp"])
toc_draft["dmp"]["properties"] = move_to_chapter_1(toc_draft["dmp"]["properties"])
add_general_info_2_id(toc_draft["dmp"]["properties"]["general_info"])

# Output the generated JSON schema as a JSON file or print it out
with open('toc_draft1.json', 'w', encoding='utf-8') as f:
    json.dump(toc_draft, f, indent=4, ensure_ascii=False)

### Generate HTML Table of Contents from JSON Schema
def generate_html_toc(schema, level=0):
    """
    Recursively generates an HTML Table of Contents from a nested schema.
    """
    html = ""
    indent = "  " * level
    for key, value in schema.items():
        if isinstance(value, dict):
            # Add the current level as a list item
            title = value.get("title", key)
            element_id = value.get("$id", key)
            html += f'{indent}<li><a href="#{element_id}">{title}</a></li>\n'
            # Process nested "properties" if they exist
            if "properties" in value:
                html += f'{indent}<ul>\n'
                html += generate_html_toc(value["properties"], level + 1)
                html += f'{indent}</ul>\n'
    return html

# Generate the Table of Contents HTML
toc_html = f"<ul>\n{generate_html_toc(toc_draft)}\n</ul>"

# Save the output to an HTML file (optional)
with open("test_table_of_contents.html", "w") as file:
    file.write(toc_html)

# Print the output for verification
#print(toc_html)
