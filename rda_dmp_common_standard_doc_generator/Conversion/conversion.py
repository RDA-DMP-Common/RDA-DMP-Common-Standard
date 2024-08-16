import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.parse

'''
Script name:    conversion.py
Date written:   8/15/2024
Software:       Python 3.11.0 64-bit 
                Visual Studio Code (1.92.1)

OS:             Windows 11 Enterprise (2/8/2024, Build 22631.3880)
Machine:        Dynabook Tecra
Author name:	Emily Chu, ORCID ID https://orcid.org/0009-0001-8417-0837
Validated by:  	Not validated
Data license:   None

Purpose:  	    - Takes the input sheet and formats the sheets to GC-RDA maDMP Application Profile format
Input:          - GC-RDA maDMP Excel Workbook Google spreadsheet
Output:         - GC-RDA maDMP Application Profile properties, values sheets updated on Google sheets
'''

# Read in the appropriate input google spreadsheet, make sure to clean the input file (i.e. remove all unnecessary rows)
google_sheet_id = '1OfY5dKEfbvFhlhBjRb4UfdPKqQiB9mjZwe_60R7mu-A'
worksheet_name = 'GC maDMP Master Sheet'
# URL-encode the worksheet name
encoded_worksheet_name = urllib.parse.quote(worksheet_name)
# Construct the URL for the CSV export
url = f'https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_worksheet_name}'

# Read the data into a pandas DataFrame
df = pd.read_csv(url)

# Check if column header names match with below print to variable column_header
# If they do not match, ctrl+f and replace the old column name with new one 
#print(df.columns.values.tolist())

column_header = ['New row numbers (sorted on fieldname)', 
                 'Row numbers (before sorting on fieldname)', 
                 'Old row numbers', 
                 'Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)', 
                 'Property ID', 'Description', 'Cardinality RDA', 'Cardinality', 
                 'GC DMP Requirement', ' "required IF/WHEN" dependency', 
                 'Front-end user-friendly question', 'Example value', 'Data type', 
                 'Allowed Values\n(controlled vocabulary)', 'Allowed Values\n(for JSON schema file)', 
                 'LAC requirement at time of transfer for archival datasets', 
                 'GC Open Data Metadata Mapping\n(Jessica & Dominique only)', 
                 'DataCite Record for DMP (Mandatory, Optional, Recommended)', 
                 'Corresponding DataCite field(s)', 'DataCite Record for Dataset (M, O, R)', 
                 'Corresponding DataCite field(s).1']

# Checks if the column header names are the same
if (df.columns.values.tolist() == column_header):
    print("Column names are the same")
else:
    raise ValueError('Column names are not the same')

# drop columns by column name if they exist 
drop_columns = ['New row numbers (sorted on fieldname)', 'Row numbers (before sorting on fieldname)', 
         'Old row numbers', 'Allowed Values\n(for JSON schema file)',
         'LAC requirement at time of transfer for archival datasets', 'GC Open Data Metadata Mapping\n(Jessica & Dominique only)',
         'DataCite Record for DMP (Mandatory, Optional, Recommended)', 'Corresponding DataCite field(s)',
         'DataCite Record for Dataset (M, O, R)', 'Corresponding DataCite field(s).1']
df_drop = df.drop(drop_columns, axis=1, errors='ignore')

'''
properties sheet 
'''
# creates new column 'id_without_slash' for fieldname without slash as the last character
df_drop['id_without_slash'] = df_drop['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)'].str.rstrip('/')

# creates new column 'label_machine' which is the name of the child (string after last slash)
df_drop['label_machine'] = df_drop['id_without_slash'].str.split('/').str[-1]

# creates new column 'label_human' 
df_drop['label_human'] = df_drop['label_machine'].str.replace('_', ' ').str.title()

# creates new column 'vocabulary' if newly added vocabulary is gc_rda_dmp_extension
# otherwise is part of original RDA 
df_drop['vocabulary'] = df_drop['Cardinality RDA'].apply(lambda x: 'gc_rda_dmp_extension' if pd.isna(x) else 'rda_dmp_common')

# rename entries in Data type: controlled vocabulary to term, nested data structure to complex, DateTime to date_time, Date to date,
# URI to uri
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('controlled vocabulary', case=True, na=False), "term", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('nested data structure', case=True, na=False), "complex", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('DateTime.', case=True, na=False), "date_time", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('Date.', case=True, na=False), "date", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('number', case=True, na=False), "number", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('URI', case=True, na=False), "uri", df_drop["Data type"])
df_drop["Data type"] = np.where(df_drop["Data type"].str.contains('string', case=False, na=False), "string", df_drop["Data type"])

# rename column headers
df_drop.rename(columns={'Property ID': 'id',
                        'Data type': 'data_type', 
                        'Example value':'example_value',
                        'Description':'description',
                        'Front-end user-friendly question': 'question',
                        'Cardinality':'cardinality',
                        'GC DMP Requirement':'dependency_type',
                        ' "required IF/WHEN" dependency':'dependency_reason'}, inplace=True)

# add new columns uri, notes
df_drop[['uri', 'notes']] = np.nan
df_drop = df_drop.fillna('')

# add row for dmp ("root property")
dmp_row = pd.DataFrame([{'Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)':'dmp','id': 'dmp', 'vocabulary':'rda_dmp_common', 'label_human':'DMP', 'label_machine':'dmp', 
           'data_type':'complex', 'cardinality':1, 'description':'Basic information on a DMP',
           'dependency_type':'required', 'notes':"the 'root' 'property'", "id_without_slash":"dmp"}])
df_drop = pd.concat([df_drop, dmp_row], ignore_index=True)

# input: s => string
# output: string
# gets the parent property id of the string 
# Example: dmp/approval/by_mbox => approval
def get_parent_property(s):
    s = str(s)
    slash_num = s.count('/')
    direct_parent = s.split('/')[slash_num-1].strip()
    if (s == "dmp"):
        return ""
    elif (df_drop['id'] == direct_parent).any():
        return direct_parent
    else:
        return s.split('/')[slash_num-2].strip() + "_" + direct_parent

# apply the function to the entire column
df_drop['parent_property'] = df_drop['id_without_slash'].apply(get_parent_property)

# drops columns for the properties sheet for the application profile
df_prop = df_drop.drop(['Common standard fieldname\n(click on blue hyperlinks for RDA core maDMP field descriptions)',
                        'Cardinality RDA', 'Allowed Values\n(controlled vocabulary)','id_without_slash'], axis=1)
# header order of the properties sheet in application profile
header_list = ['id','vocabulary','label_human', 'label_machine', 'data_type', 'parent_property',
                         'cardinality', 'description', 'example_value', 'question', 'uri', 'dependency_type','dependency_reason','notes']
# rearrange dataframe to suit the header order
df_prop = df_prop.reindex(columns = header_list) 

# fill NA with empty spaces
df_prop = df_prop.fillna('')

'''
values sheet
'''
# use properties sheet as a base
df_val_base = df_prop
# bring back Allow Values from original input as a column
allowed_vals = df["Allowed Values\n(controlled vocabulary)"]
df_val_base = pd.concat([df_val_base, allowed_vals], axis = 1)

# drop NA rows
df_val_base.dropna(axis='rows', inplace=True)
# subset for only rows with controlled vocabularies/term
df_val_base = df_val_base[(df_val_base["data_type"] == "term")]

# initialize empty list
result_list = []

# Iterate over rows in the DataFrame to build rows for values sheet
for index, row in df_val_base.iterrows():
    position = 1 # determines the list_order
    id_value = row['id']
    vocab = row['vocabulary']
    label_lst = row["Allowed Values\n(controlled vocabulary)"].split(',')
    label_lst = [x.strip(' ') for x in label_lst]
    # Create new rows by concatenating cat with each value
    for label in label_lst:
        concatenated_value = f"{id_value}_{label}"
        result_list.append([concatenated_value, vocab, id_value, label, position])
        position += 1

# create new dataframe df_values 
df_values = pd.DataFrame(result_list, columns=['id', 'vocabulary','property', 'label','list_order'])
# add new columns uri, notes
df_values[['uri', 'notes']] = np.nan
df_values = df_values.fillna('')

'''
export pandas dataframes for properties and values sheet into Application Profile on Google
Spreadsheets

requires credentials.json to be in the folder
'''
# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open a Google Sheet
spreadsheet = client.open("GC-RDA maDMP Application Profile")

# Open the newly created worksheet
properties_sheet = spreadsheet.worksheet("properties")
values_sheet = spreadsheet.worksheet("values")

# Update the Google Sheet with the DataFrame data
properties_sheet.update(range_name='A1', values=[df_prop.columns.tolist()] + df_prop.values.tolist())
values_sheet.update(range_name="A1", values=[df_values.columns.tolist()] + df_values.values.tolist())

'''
manual to excel if needed
'''
#df_prop.to_excel('output/properties.xlsx', index=False)
#df_values.to_excel('output/values.xlsx', index=False)




