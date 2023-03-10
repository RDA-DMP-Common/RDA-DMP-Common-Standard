# maDMP JSON schema - version 1.2
This is the JSON schema for the DMP common standard. Examples against the schema can be found [here](/examples/JSON/)

### Changes
1. Addition of `affiliation` object to `contact` and `contributor`

  Example:
  ```
  "affiliation": {
    "name": "Research Data Alliance",
    "affiliation_id": {
      "identifier": "https://ror.org/05dc6w374",
      "type": "ror"
    }
  }
  ```
