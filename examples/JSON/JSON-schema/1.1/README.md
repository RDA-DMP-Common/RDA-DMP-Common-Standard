# maDMP JSON schema - version 1.1
This is the JSON schema for the DMP common standard. Examples against the schema can be found [here](..)

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

<br>

---
**NOTE**

Certain properties, which may contain multiple objects or values, have `minItems` set to 1.  
This ensures that an empty array is not provided. These properties can still be omitted (if not required).  
If they are specified however, they have to have at least one object or value contained.

Example:  
This will not pass validation:  
```
"license": []
```

But this will:  
```
"license": [
    {
        "license_ref": "https://creativecommons.org/licenses/by/4.0/",
		"start_date": "2020-01-01"
    }
]
```

---
