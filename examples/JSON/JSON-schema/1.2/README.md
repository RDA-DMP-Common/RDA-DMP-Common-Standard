# maDMP JSON schema - version 1.2

This is the JSON schema for the DMP common standard. Examples against the schema can be found [here](/examples/JSON/)

### Changes

- Fixed example `datetime` values (added timezone) and descriptions on `date`/`datetime` fields
- Fixed and improved descriptions and example values
- Fixed `uri` / `url` format
- Restructured JSON Schema using re-usable definitions
- Reworked identifier structures (change of multiplicities and relaxing identifier `type` to any string value, introducing `AlternateIdentifier` and `RelatedIdentifier` for `Dataset` and `DMP`)
- Allowed extra properties in the top-level object
- Added `issued` to `Distribution` object
- Added `is_reused` to `Dataset` object
- Added `creator` to `Dataset` object
- Added `affiliation` to `Contributor`, `Contact`, and `Creator`
- Changed `ethical_issues_report` type in `DMP` to string value (from URL)
