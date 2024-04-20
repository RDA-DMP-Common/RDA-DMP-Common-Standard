import os
import pandas as pd
import xlwings as xw

# Change the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the Excel file using pandas
df = pd.read_excel("GC-RDA maDMP Excel Workbook.xlsx", sheet_name="Git test sort orange tab")

# Remove trailing slashes from the 'Fieldname' column
df['Fieldname'] = df['Fieldname'].str.rstrip('/')

# Define a function to split the "Fieldname" column
def split_fieldname(fieldname):
    parts = fieldname.split('/')
    id = parts[-1]
    parent_property = parts[-2] if len(parts) > 1 else None
    return pd.Series([parent_property, id])

def map_data_type(data_type):
    if pd.isna(data_type):
        return data_type
    elif 'string' in data_type:
        return 'string'
    elif 'controlled vocabulary' in data_type:
        return 'term'
    elif 'number' in data_type:
        return 'number'
    elif 'DateTime.' in data_type:
        return 'date_time'
    elif 'Date.' in data_type:
        return 'Date'
    elif 'uri' in data_type:
        return 'uri'
    elif 'nested data structure' in data_type:
        return 'complex'
    else:
        return data_type

# Apply the function to the DataFrame
df[['parent_property', 'id']] = df['Fieldname'].apply(split_fieldname)

# Apply the function to the 'Data type' column
df['Data type'] = df['Data type'].apply(map_data_type)

# Create the 'label_human' column
df['label_human'] = df['id'].str.replace('_', ' ').str.title()

# Create the 'label_machine' column
df['label_machine'] = df['id']

# Create a new column 'vocabulary'
df['vocabulary'] = df['Data type'].apply(lambda x: 'gc_rda_dmp_extension' if x != 'term' else '')

# Keep only the specified columns
df = df[['Fieldname', 'Added GitHub Application Profile', 'id', 'vocabulary', 'label_human', 'label_machine', 'Data type', 'parent_property', 'Cardinality', 'Example response']]

# Define a function to process each group
def process_group(group):
    if len(group) > 1:  # If there are duplicates
        for idx, row in group.iterrows():
            if row['parent_property'] != 'dmp':
                group.loc[idx, 'id'] = str(row['parent_property']) + "_" + str(row['id'])
    return group

# Apply the function to each group
df = df.groupby('id').apply(process_group)

# Create the 'parent_fieldname' column
df['parent_fieldname'] = df['Fieldname'].apply(lambda x: '/'.join(x.split('/')[:-1]))

# Create the mapping from 'Fieldname' to 'id'
fieldname_to_id = df.set_index('Fieldname')['id'].to_dict()

# Create the 'parent_property' column
df['parent_property'] = df['parent_fieldname'].map(fieldname_to_id).fillna(df['parent_property'])

# Drop the 'parent_fieldname' column
df = df.drop(columns=['parent_fieldname'])

# Save the modified DataFrame to a new Excel file
df.to_excel("Application Profile.xlsx", index=False)
