# maDMP JSON schema - version 1.1
This is the JSON schema for the DMP common standard. Examples against the schema can be found [here](/examples/JSON/)

### Changes
1. Updated cardinality of following properties:
    * `end`  (_dmp/project/end_) from required to optional
    * `grant_id`  (_dmp/project/funding/grant_id_) from required to optional
    * `start`  (_dmp/project/start_) from required to optional
    
2. Updated description of following properties:
    * `available_until`  (_dmp/dataset/distribution/available_until_)
    * `created`  (_dmp/created_)
    * `end`  (_dmp/project/end_)
    * `issued`  (_dmp/dataset/issued_)
    * `modified`  (_dmp//modified_)
    * `start`  (_dmp/project/start_)
    * `start_date`  (_dmp/dataset/distribution/license/start_date_)

3. Removed all `minItems` restrictions to arrays.

    Example:  
    This will now pass validation:  
    ```
    "license": []
    ```
