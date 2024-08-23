# GCWG-RDA-maDMP-JSON schema

## Instructions for create_schema.py

1. Install relevant libraries
   ```bash
   py -m pip install pandas numpy 
   ```

2. Ensure that that the sheet name is the same or updated to the relevant sheet name. For example, if <b>GC maDMP Master Sheet</b> is changed to a different name, please change the sheet name in the python code to reflect this. Additionally make sure that the input has all columns in `kept_columns` variable in `create_schema.py`. If names are updated in the source sheet, please update the python code to reflect the changes.
3. Run the Python code. If successfully completed, a json file should appear, this is the GCWG-RDA-maDMP JSON-schema that is generated.

## Adding new keys to the JSON file
If you would like to add more keys for each field, the easiest method is to create a new column in the input file. And add these lines of code in the relevant locations. 
In the `for _, row in df.iterrows():` loop
```bash
new_key = row["new key"]
```
```bash
if pd.notna(new_key):
   schema_object["newKeyName"] = new_key
```

## Differences between RDA Schema and GCWG-RDA-maDMP Schema
1. More fields
2. "question" key with the value being the front-end user-friendly question
3. "requiredWhen" key with the value being the neccessary nested data structures that are required. "requiredWhen" key is generated at the child level with the values being ancestors of the child.



