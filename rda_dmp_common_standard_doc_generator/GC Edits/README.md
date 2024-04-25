# GC-RDA maDMP Data Migration Guide

## Overview

This guide outlines the process of migrating data from the GC-RDA maDMP Excel Workbook into the GC-RDA maDMP Application Profile. The Excel Workbook contains two relevant sheets: "Git test sort orange tab" and "GC maDMP Master Sheet". The "GC maDMP Master Sheet" serves as the primary source for updates and changes, while the "Git test sort orange tab" serves as the connection between the master sheet and the application profile.

## Application Profile Overview

The GC-RDA maDMP Application Profile is composed of five sheets:

- **data_types:** This sheet defines the types of data expected in the application profile.
- **vocabularies:** Contains controlled vocabularies used in the application profile.
- **properties:** Defines the properties or fields used in the application profile.
- **values:** Provides allowable values for specific properties.
- **entity_descriptions:** Describes entities within the application profile, which are only updated when relevant information changes.

## Updating the Application Profile

When updating the application profile due to changes in standards or requirements, follow these guidelines:

- **Data Types and Entity Descriptions:** Only update these sheets when relevant information changes.
- **Vocabularies, Properties, and Values:**
  - If a new row or field name is introduced from the standard, the **vocabularies**, **properties**, and **values** sheets may need updating.
  - If the new field is of a controlled vocabulary data type, update all three sheets accordingly.
  - If the new field is of other data types, only the **properties** sheet needs updating.

Please note the following guidelines for handling changes:

- **Row Changes (Adding or Removing Fields):**
  - Row changes, such as adding or removing fields from the "Git test sort orange tab" (i.e., to include more or fewer fields), should be performed directly in the Google Sheets.
  
- **Column Changes (Adding or Removing Information):**
  - Column changes, such as adding or removing information (fields) from the application profile, require modifications in the Go code. Refer to the [maDMP Standard GitHub repository](https://github.com/FAIRERdata/maDMP-Standard/blob/Tests/rda_dmp_common_standard_doc_generator/README.md) for instructions on updating the Go code to reflect these changes.

Always perform checks from random sampling after mapping to ensure correctness. Please note that there is an overall "dmp" field in the application profile, while it might not exist in the "Git test sort orange tab".

## Conversion Workflow

1. **Alignment Check:**
   - Before initiating any data migration, ensure that the "Git test sort orange tab" is aligned with the information in the "GC maDMP Master Sheet" inside the workbook file.

2. **Mapping from Master Sheet to Git Sort Sheet:**
   - To map data from the "GC maDMP Master Sheet" to the "Git test sort orange tab", sort the "Git test sort orange tab" based on the "Sort order in orange tab" column.

3. **Mapping from Git Sort Sheet to Application Profile Properties Sheet:**
   - To map data from the "Git test sort orange tab" to the properties sheet of the application profile, sort both files on the "Property ID" column.

---

This comprehensive guide provides an overview of the conversion process, details the structure of the application profile, guidelines for updating it, and finally, the step-by-step conversion workflow.
