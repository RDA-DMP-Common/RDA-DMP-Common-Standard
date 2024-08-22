## Full details in [conversion.docx](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FFAIRERdata%2FmaDMP-Standard%2FMaster%2Frda_dmp_common_standard_doc_generator%2FConversion%2Fdocumentation%2Fconversion.docx&wdOrigin=BROWSELINK)
## Introduction 

The <b>GC-RDA maDMP Excel Workbook</b> contains information such as fieldnames, property ids, descriptions, example values, user-friendly questions, data types, allowed values, cardinalities, requirements, and dependencies. 
The information is specifically present in the worksheet, GC maDMP Master sheet; which is commonly referred to as the “orange tab.” The information serves as an input to creating the GC-RDA maDMP Application Profile. 

The GC-RDA maDMP Excel Workbook contains all relevant information for the <b>GC-RDA maDMP Application Profile</b>; however, changes to formatting must be made to create the user-friendly Application Profile visible on [GitHub pages](https://fairerdata.github.io/maDMP-Standard/). 
The following below documents the process on converting the <b>GC-RDA maDMP Excel Workbook</b> into the <b>GC-RDA maDMP Application Profile</b>. 
The <b>GC-RDA maDMP Application Profile</b> serves as the input for Go code in folder `rda_dmp_common_standard_doc_generator` which creates the GitHub pages README.md output. 

## GC-RDA maDMP Application Profile Sheets
The GC-RDA maDMP Application Profile contains 5 different sheets. 
<ul>
 <li> <b>data_types</b>: This sheet defines the types of data expected in the application profile.</li>
  <li>	<b>vocabularies</b>: Contains controlled vocabularies used in the application profile.</li>
  <li> <b>properties</b>: Defines the properties or fields used in the application profile.</li>
  <li><b>values</b>: Provides allowable values for specific properties.</li>
  <li><b>entity_descriptions</b>: Describes entities within the application profile, which are only updated when relevant information changes.</li>
</ul>

Only two of the sheets are relevant for changing the GitHub website: the properties sheet and the values sheet. The conversion code specifically focuses on these two sheets; all other sheets will be unchanged. Note that running the Python code requires a Google Service Account because the service account allows for Python to use Google Sheets API to update the Google Sheets. 

## Updating Application Profile Guide:
1.	Download the maDMP repository and open the Conversion folder, this will be the relevant working folder for the code
2.	Ensure that worksheet_name variable in the Python code is set to the correct sheet in the GC maDMP Excel Workbook
3.	Set the relevant excel sheet to be plain text, particularly for column “Example Value.” This will prevent Python from automatically interpreting certain cells as Datetimes/Dates
4.	Ensure that credentials.json is present in the main work folder. If credentials.json is not present, read [How to set up a Google Service Account](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FFAIRERdata%2FmaDMP-Standard%2FMaster%2Frda_dmp_common_standard_doc_generator%2FConversion%2Fdocumentation%2Fconversion.docx&wdOrigin=BROWSELINK) section in the documentation <b> conversion.docx </b>.
5.	Install relevant libraries on your Python IDE of choice:
   ```bash
 py -m pip install pandas numpy gspread oauth2client
```
6.	Ensure that the relevant column header names (those in kept_columns variable) are the same in the Python script and input file (examples: Property ID, Description, etc.). If they are not, a print message will show up in the terminal and say that the “Column names are not the same.” When this happens, there is a possibility that the outputs will not be correct. Please change the Python code to have the updated names in the variable kept_columns 
7.	Run the Python code. If ran successfully, the properties and values sheet in the Application Profile will have been updated. Note that the number of rows in the properties sheet should be number of rows in the input sheet + 1. The extra row is to account for the root ("dmp").

<b>NOTE</b>: If there is trouble with the Google Service Account not functioning, manual outputs of the properties and values sheet can be done with the last two lines of code.

