# maDMP JSON schema - version 1.3

This is the JSON schema for the DMP common standard. Examples against the schema can be found [here](/examples/JSON/)

### Changes

- Recommended ROR instead of Crossref Funder Registry for `funder_id` in `Funding` ([#145](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/issues/145))
- Fixed descriptions of `backup_type` and `storage_type` in `Host` ([#153](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/issues/153))
- Clarified the difference between `host_id` and `url` in `Host` and extended suggested `host_id` types ([#144](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/issues/144))
- Added `restricted` as a value of `data_access` in `Distribution` and deprecated `shared` ([#150](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/pull/150))
- Clarified the use of `is_reused` together with `related_identifier` in `Dataset` for reused data ([#143](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/issues/143))
