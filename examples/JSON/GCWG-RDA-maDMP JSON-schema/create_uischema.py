import pandas as pd
import json
import urllib.parse

"""
create the ui schema based on the google sheet for the RDA maDMP JSON schema
"""

def create_nested_structure(schema, prop_path_list, prop_names):
    if prop_path_list[0] not in schema:
        schema[prop_path_list[0]] = {}

    if len(prop_path_list) == 1:
        schema[prop_path_list[0]]['ui:order'] = prop_names
        return
    
    create_nested_structure(schema[prop_path_list[0]], prop_path_list[1:], prop_names)

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
kept_columns = [ "Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)",
                "Logic order of subquestions under each chapter"]

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
ui_schema_draft = {
}

# A dictionary to track the cardinality fields at each level
array_list = []

# Iterate through each row and construct the schema
for _, row in df_sorted.iterrows():
    field_path = row['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].split('/')
    order = str(row['Logic order of subquestions under each chapter']).split('.')
    cardinality = row['Cardinality']

    # delete
    if "approval" not in field_path and "cost" not in field_path:
        continue

    parent_path = "/".join(field_path[:-1])
    child_name = field_path[-1]
    
    if parent_path not in ui_schema_draft:
        ui_schema_draft[parent_path] = []
    ui_schema_draft[parent_path].append(child_name)

    # Check if the current field is an array (cardinality = 1..n)
    if pd.notna(cardinality) and cardinality.strip().lower() == '1..n' or cardinality.strip().lower() == '0..n':
        # check if all of the parents are not in the array_fields_list
        array_path = "/".join(field_path)
        all_not_in_dict = all( item not in array_path for item in array_list)
        if all_not_in_dict:
            array_list.append(array_path)
    

# Output the generated JSON schema as a JSON file or print it out
#with open('ui-schema2_draft.json', 'w', encoding='utf-8') as f:
#    json.dump(ui_schema_draft, f, indent=4, ensure_ascii=False)


###### transform ui schema draft to ui schema
ui_schema = {}
for prop_path, prop_names in ui_schema_draft.items():
    if len(prop_names) == 0:
        continue
    
    prop_path_list = prop_path.split('/')
    create_nested_structure(ui_schema, prop_path_list, prop_names)
        

# add array layer in schemas (move the properties into the array layer)
def add_array_layer(schema, path=""):
    if isinstance(schema, dict):
        for prop_name, prop_value in schema.items():
            current_path = f"{path}/{prop_name}".strip("/")
            #print(current_path)

            ## newly added column
            # add array layer 
            if current_path in array_list:
                schema[prop_name] = {
                    'items': prop_value,
                }

            add_array_layer(prop_value, current_path)

#print(array_list)
add_array_layer(ui_schema)

with open('ui-schema2.json', 'w', encoding='utf-8') as f:
    json.dump(ui_schema, f, indent=4, ensure_ascii=False)


print("UI schema has been generated successfully!")