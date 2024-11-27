# GCWG-RDA-maDMP-JSON schema

## Intro

This folder stores JSON schemas and its corresponding uischema and table of content, and the scripts to create them. 

There are `2 scripts` and _3 files_ here that are important in the folder

1. `create_schema.py`: fetches the data from Orange Tab and transform it to machina actionable JSON schema, stored in _GCWG-RDA-maDMP-schema.json_.
   
2. `create_uischema.py`: also fetches data from Orange Tab and generates the uischema for JSON schema stored in _ui_schema.json_. (note: uischema is not offically used in JSON. It is introduced in RJSF to help render JSON schemas)

3. _schema_metadata.json_: this files contains the metadata needed for __maDMP-Generation-Form__ to switch between different schema verions. For now, it constains the schema name, uischema, and table of content for each schema. 


## Instructions to create a new version of maDMP

1. Install relevant libraries
   ```bash
   py -m pip install pandas numpy 
   ```
2. Ensure that that the sheet name is the same or updated to the relevant sheet name. For example, if <b>GC maDMP Master Sheet</b> is changed to a different name, please change the sheet name in the python code to reflect this. Additionally make sure that the input file has all columns in `kept_columns` variable in `create_schema.py`. If names are updated in the source sheet, please update the python code to reflect the changes.

3. Ensure that you have the correct ouput file names in the scripts.

4. Run the 2 Python scripts. If successfully completed, 2 JSON files should appear

5. Then you need to manual add the name and version of the maDMP and names of the 2 generated files to _schema_metadata.json_.


## Adding new keys to the JSON file
If you would like to add more keys for each field, the easiest method is to create a new column in the input file. And add these lines of code in the relevant locations of `create_schema.py`. 
In the `for _, row in df.iterrows():` loop
```python
new_key = row["new key"]
```
```python
if pd.notna(new_key):
   schema_object["newKeyName"] = new_key
```

## Differences between RDA Schema and GCWG-RDA-maDMP Schema
1. More fields
2. "question" key with the value being the front-end user-friendly question
3. "requiredWhen" key with the value being the neccessary nested data structures that are required. "requiredWhen" key is generated at the child level with the values being ancestors of the child.



