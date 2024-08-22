# GC-RDA JSON-schema

## Instructions for create_schema.py

1. Install relevant libraries
   ```bash
   py -m pip install pandas numpy 
   ```

2. Ensure that the input has structure as shown in input `dmp_structure.csv` with the same column names
3. Run the Python code. If successfully completed, a json file should appear, this is the GC-RDA JSON-schema that is generated.

## Differences between RDA Schema and GC-RDA Schema
1. More fields in general
2. question key with the value being the front-end user-friendly question
3. requiredWhen key with the value being the neccessary nested data structures that are required



