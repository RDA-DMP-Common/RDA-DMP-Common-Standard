<style>
td {
  vertical-align: top;
}
</style>

# RDA DMP Common Standard for machine-actionable Data Management Plans


<table>
<tr>
<td>
<h3>About this document</h3>
This is a metadata application profile to provide basic interoperability between systems producing or consuming machine-actionable data management plans (maDMPS). Further fields can be added in specific deployments, but they do not guarantee interoperability. DMP tools can use any other fields in their internal data models.

This standard allows modelling a wide range of use cases and does not set any business (e.g. funder specific) requirements. It allows modelling information over the whole DMP lifecycle.

For more information see <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/master/examples/JSON">examples</a>, <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/FAQ.md">FAQ</a> or <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/master/docs/diagrams">diagrams</a>.
</td>
<td>
  <h3>Structure</h3>

<ul><li id="dmp_tree"><a href="#dmp_table">dmp</a></li><ul><li id="dmp_contact_tree"><a href="#dmp_contact_table">contact</a></li><ul><li id="contact_id_tree"><a href="#contact_id_table">contact_id</a></li><ul><li id="contact_id_identifier_tree"><a href="#contact_id_identifier">identifier</a></li><li id="contact_id_type_tree"><a href="#contact_id_type">type</a></li></ul><li id="dmp_contact_mbox_tree"><a href="#dmp_contact_mbox">mbox</a></li><li id="dmp_contact_name_tree"><a href="#dmp_contact_name">name</a></li></ul><li id="cost_tree"><a href="#cost_table">cost</a></li><ul><li id="cost_unit_tree"><a href="#cost_unit">currency_code</a></li><li id="cost_description_tree"><a href="#cost_description">description</a></li><li id="cost_title_tree"><a href="#cost_title">title</a></li><li id="cost_value_tree"><a href="#cost_value">value</a></li></ul><li id="dmp_created_tree"><a href="#dmp_created">created</a></li><li id="dm_contributor_tree"><a href="#dm_contributor_table">dm_contributor</a></li><ul><li id="contributor_id_tree"><a href="#contributor_id_table">contributor_id</a></li><ul><li id="contributor_id_id_tree"><a href="#contributor_id_id">identifier</a></li><li id="contributor_id_type_tree"><a href="#contributor_id_type">type</a></li></ul><li id="dm_contributor_mbox_tree"><a href="#dm_contributor_mbox">mbox</a></li><li id="dm_contributor_name_tree"><a href="#dm_contributor_name">name</a></li><li id="dm_contributor_role_tree"><a href="#dm_contributor_role">role</a></li></ul><li id="dmp_id_tree"><a href="#dmp_id_table">dmp_id</a></li><ul><li id="dmp_id_id_tree"><a href="#dmp_id_id">identifier</a></li><li id="dmp_id_type_tree"><a href="#dmp_id_type">type</a></li></ul><li id="dataset_tree"><a href="#dataset_table">dataset</a></li><ul><li id="dataset_quality_assurance_tree"><a href="#dataset_quality_assurance">data_quality_assurance</a></li><li id="dataset_id_tree"><a href="#dataset_id_table">dataset_id</a></li><ul><li id="dataset_id_id_tree"><a href="#dataset_id_id">identifier</a></li><li id="dataset_id_type_tree"><a href="#dataset_id_type">type</a></li></ul><li id="dataset_description_tree"><a href="#dataset_description">description</a></li><li id="distribution_tree"><a href="#distribution_table">distribution</a></li><ul><li id="distribution_access_url_tree"><a href="#distribution_access_url">access_url</a></li><li id="distribution_available_till_tree"><a href="#distribution_available_till">available_till</a></li><li id="distribution_byte_size_tree"><a href="#distribution_byte_size">byte_size</a></li><li id="distribution_data_access_tree"><a href="#distribution_data_access">data_access</a></li><li id="distribution_description_tree"><a href="#distribution_description">description</a></li><li id="distribution_download_url_tree"><a href="#distribution_download_url">download_url</a></li><li id="distribution_format_tree"><a href="#distribution_format">format</a></li><li id="host_tree"><a href="#host_table">host</a></li><ul><li id="host_availability_tree"><a href="#host_availability">availability</a></li><li id="host_backup_frequency_tree"><a href="#host_backup_frequency">backup__frequency</a></li><li id="host_backup_type_tree"><a href="#host_backup_type">backup_type</a></li><li id="host_certified_with_tree"><a href="#host_certified_with">certified_with</a></li><li id="host_description_tree"><a href="#host_description">description</a></li><li id="host_geo_location_tree"><a href="#host_geo_location">geo_location</a></li><li id="host_pid_system_tree"><a href="#host_pid_system">pid_system</a></li><li id="storage_type_tree"><a href="#storage_type">storage_type</a></li><li id="host_supports_versioning_tree"><a href="#host_supports_versioning">support_versioning</a></li><li id="host_title_tree"><a href="#host_title">title</a></li><li id="host_url_tree"><a href="#host_url">url</a></li></ul><li id="license_tree"><a href="#license_table">license</a></li><ul><li id="license_ref_tree"><a href="#license_ref">license_ref</a></li><li id="license_start_date_tree"><a href="#license_start_date">start_date</a></li></ul><li id="distribution_title_tree"><a href="#distribution_title">title</a></li></ul><li id="dataset_issued_tree"><a href="#dataset_issued">issued</a></li><li id="dataset_keyword_tree"><a href="#dataset_keyword">keyword</a></li><li id="dataset_language_tree"><a href="#dataset_language">language</a></li><li id="metadata_tree"><a href="#metadata_table">metadata</a></li><ul><li id="metadata_description_tree"><a href="#metadata_description">description</a></li><li id="metadata_language_tree"><a href="#metadata_language">language</a></li><li id="metadata_standard_id_tree"><a href="#metadata_standard_id_table">metadata_standard_id</a></li><ul><li id="metadata_id_id_tree"><a href="#metadata_id_id">identifier</a></li><li id="metadata_id_type_tree"><a href="#metadata_id_type">type</a></li></ul></ul><li id="dataset_personal_data_tree"><a href="#dataset_personal_data">personal_data</a></li><li id="dataset_preservation_tree"><a href="#dataset_preservation">preservation_statement</a></li><li id="security_privacy_tree"><a href="#security_privacy_table">security_and_privacy</a></li><ul><li id="sp_description_tree"><a href="#sp_description">description</a></li><li id="sp_title_tree"><a href="#sp_title">title</a></li></ul><li id="dataset_sensitive_data_tree"><a href="#dataset_sensitive_data">sensitive_data</a></li><li id="technical_resource_tree"><a href="#technical_resource_table">technical_resource</a></li><ul><li id="tr_description_tree"><a href="#tr_description">description</a></li><li id="tr_id_tree"><a href="#tr_id">technical_reosurce_id</a></li><li id="tr_id_type_tree"><a href="#tr_id_type">technical_reosurce_id_type</a></li></ul><li id="dataset_title_tree"><a href="#dataset_title">title</a></li><li id="dataset_type_tree"><a href="#dataset_type">type</a></li></ul><li id="dmp_description_tree"><a href="#dmp_description">description</a></li><li id="ethical_issues_description_tree"><a href="#ethical_issues_description">ethical_issues_description</a></li><li id="ethical_issues_exist_tree"><a href="#ethical_issues_exist">ethical_issues_exist</a></li><li id="ethical_issues_report_tree"><a href="#ethical_issues_report">ethical_issues_report</a></li><li id="dmp_language_tree"><a href="#dmp_language">language</a></li><li id="dmp_modified_tree"><a href="#dmp_modified">modified</a></li><li id="project_tree"><a href="#project_table">project</a></li><ul><li id="project_description_tree"><a href="#project_description">description</a></li><li id="project_end_tree"><a href="#project_end">end</a></li><li id="funding_tree"><a href="#funding_table">funding</a></li><ul><li id="funder_id_tree"><a href="#funder_id_table">funder_id</a></li><ul><li id="funder_id_id_tree"><a href="#funder_id_id">identifier</a></li><li id="funder_id_type_tree"><a href="#funder_id_type">type</a></li></ul><li id="funding_status_tree"><a href="#funding_status">funding_status</a></li><li id="grant_id_tree"><a href="#grant_id_table">grant_id</a></li><ul><li id="grant_id_id_tree"><a href="#grant_id_id">identifier</a></li><li id="grant_id_type_tree"><a href="#grant_id_type">type</a></li></ul></ul><li id="project_start_tree"><a href="#project_start">start</a></li><li id="project_title_tree"><a href="#project_title">title</a></li></ul><li id="dmp_title_tree"><a href="#dmp_title">title</a></li></ul></ul></td></tr></table>

<hr/>

<h2 id="dmp_table">Properties in 'dmp'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="dmp_contact" href="#dmp_contact_tree">contact</a></td><td>Contact person for a DMP</td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="cost" href="#cost_tree">cost</a></td><td>To list costs related to data management. Providing multiple instances of a 'Cost' allows to break down costs into details. Providing one 'Cost' instance allows to provide one aggregated sum.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dmp_created" href="#dmp_created_tree">created</a></td><td>Date and time of the first version of a DMP. Must not be changed in subsequent DMPs.</td><td>DateTime</td><td>Exactly One</td><td>2019-03-13 13:13</td></tr>
<tr><td><a id="dm_contributor" href="#dm_contributor_tree">dm_contributor</a></td><td>To list people that play role in data management related to this DMP, e.g. resoponsible for performing actions described in this DMP.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dmp_id" href="#dmp_id_tree">dmp_id</a></td><td>Identifier for the DMP itself</td><td>Nested Data Structure</td><td>Exactly One</td><td>DOI</td></tr>
<tr><td><a id="dataset" href="#dataset_tree">dataset</a></td><td>To describe data on a non-technical level.</td><td>Nested Data Structure</td><td>One or More</td><td> </td></tr>
<tr><td><a id="dmp_description" href="#dmp_description_tree">description</a></td><td>To provide any free-form text information on a DMP</td><td>String</td><td>Zero or One</td><td>This DMP is for our new project</td></tr>
<tr><td><a id="ethical_issues_description" href="#ethical_issues_description_tree">ethical_issues_description</a></td><td>To describe ethical issues directly in a DMP</td><td>String</td><td>Zero or One</td><td>There are ethical issues, because...</td></tr>
<tr><td><a id="ethical_issues_exist" href="#ethical_issues_exist_tree">ethical_issues_exist</a></td><td>To indicate whether there are ethical issues related to data that this DMP describes. Allowed values: yes / no / unknown</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>yes</td></tr>
<tr><td><a id="ethical_issues_report" href="#ethical_issues_report_tree">ethical_issues_report</a></td><td>To indicate where a protocol from a meeting with an ethical commitee can be found</td><td>URI</td><td>Zero or One</td><td>http://report.location</td></tr>
<tr><td><a id="dmp_language" href="#dmp_language_tree">language</a></td><td>Language of the DMP expressed using ISO 6391-1 two letter country code.</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>en</td></tr>
<tr><td><a id="dmp_modified" href="#dmp_modified_tree">modified</a></td><td>Must be set each time DMP is modified. Indicates DMP version.</td><td>DateTime</td><td>Exactly One</td><td>2020-03-14 10:53</td></tr>
<tr><td><a id="project" href="#project_tree">project</a></td><td>Project related to a DMP</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dmp_title" href="#dmp_title_tree">title</a></td><td>Title of a DMP</td><td>String</td><td>Exactly One</td><td>DMP for our new project</td></tr>
</tbody>
</table>

<h2 id="dmp_contact_table">Properties in 'contact'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact_id" href="#contact_id_tree">contact_id</a></td><td>Identifier for a contact person</td><td>Nested Data Structure</td><td>Exactly One</td><td>http://orcid.org/0000-0000-0000-0000</td></tr>
<tr><td><a id="dmp_contact_mbox" href="#dmp_contact_mbox_tree">mbox</a></td><td>E-mail address</td><td>String</td><td>Exactly One</td><td>cc@example.com</td></tr>
<tr><td><a id="dmp_contact_name" href="#dmp_contact_name_tree">name</a></td><td>Name of the contact person</td><td>String</td><td>Exactly One</td><td>Charlie Chaplin</td></tr>
</tbody>
</table>

<h2 id="contact_id_table">Properties in 'contact_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact_id_identifier" href="#contact_id_identifier_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="contact_id_type" href="#contact_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>ORCID</li><li>ISNI</li><li>OpenID</li><li>Email</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>ORCID</td></ul>
</td></tr></tbody>
</table>

<h2 id="cost_table">Properties in 'cost'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="cost_unit" href="#cost_unit_tree">currency_code</a></td><td>Allowed values defined by ISO 4217.</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>EUR</td></tr>
<tr><td><a id="cost_description" href="#cost_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Costs for maintaining....</td></tr>
<tr><td><a id="cost_title" href="#cost_title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Storage and backup</td></tr>
<tr><td><a id="cost_value" href="#cost_value_tree">value</a></td><td>Value</td><td>Number</td><td>Zero or One</td><td>1000</td></tr>
</tbody>
</table>

<h2 id="dm_contributor_table">Properties in 'dm_contributor'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contributor_id" href="#contributor_id_tree">contributor_id</a></td><td> </td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="dm_contributor_mbox" href="#dm_contributor_mbox_tree">mbox</a></td><td>Mail address</td><td>String</td><td>Zero or One</td><td>john@smith.com</td></tr>
<tr><td><a id="dm_contributor_name" href="#dm_contributor_name_tree">name</a></td><td>Name</td><td>String</td><td>Exactly One</td><td>John Smith</td></tr>
<tr><td><a id="dm_contributor_role" href="#dm_contributor_role_tree">role</a></td><td>Contributor Type. Allowed values as defined by DataCite. See: https://schema.datacite.org/meta/kernel-4.1/doc/DataCite-MetadataKernel_v4.1.pdf</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>Data Manager</td></tr>
</tbody>
</table>

<h2 id="contributor_id_table">Properties in 'contributor_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contributor_id_id" href="#contributor_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td>0000-0000-0000-0000</td></tr>
<tr><td><a id="contributor_id_type" href="#contributor_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>ORCID</li><li>ISNI</li><li>OpenID</li><li>Email</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>ORCID</td></ul>
</td></tr></tbody>
</table>

<h2 id="dmp_id_table">Properties in 'dmp_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="dmp_id_id" href="#dmp_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="dmp_id_type" href="#dmp_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>DOI</li><li>URL</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>DOI</td></ul>
</td></tr></tbody>
</table>

<h2 id="dataset_table">Properties in 'dataset'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="dataset_quality_assurance" href="#dataset_quality_assurance_tree">data_quality_assurance</a></td><td>Data Quality Assurance</td><td>String</td><td>Zero or More</td><td>We use file naming convention...</td></tr>
<tr><td><a id="dataset_id" href="#dataset_id_tree">dataset_id</a></td><td>Dataset ID</td><td>Nested Data Structure</td><td>Exactly One</td><td>http://doi.org/10.5281/zenodo.1172673</td></tr>
<tr><td><a id="dataset_description" href="#dataset_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Field observation</td></tr>
<tr><td><a id="distribution" href="#distribution_tree">distribution</a></td><td>To provide technical information on a specific instance of data.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dataset_issued" href="#dataset_issued_tree">issued</a></td><td>Issued</td><td>Date</td><td>Zero or One</td><td>2019-06-30</td></tr>
<tr><td><a id="dataset_keyword" href="#dataset_keyword_tree">keyword</a></td><td>Keyword</td><td>String</td><td>Zero or More</td><td>keyword 1, keyword 2</td></tr>
<tr><td><a id="dataset_language" href="#dataset_language_tree">language</a></td><td>Language of the dataset expressed using ISO 6391-1 two letter country code.</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>en</td></tr>
<tr><td><a id="metadata" href="#metadata_tree">metadata</a></td><td>To describe metadata standards used. </td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dataset_personal_data" href="#dataset_personal_data_tree">personal_data</a></td><td>Allowed values: yes / no / unknown</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>unknown</td></tr>
<tr><td><a id="dataset_preservation" href="#dataset_preservation_tree">preservation_statement</a></td><td>Preservation Statement</td><td>String</td><td>Zero or One</td><td>Must be preserved to enable...</td></tr>
<tr><td><a id="security_privacy" href="#security_privacy_tree">security_and_privacy</a></td><td>To list all issues and requirements related to security and privacy</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dataset_sensitive_data" href="#dataset_sensitive_data_tree">sensitive_data</a></td><td>Allowed values: yes / no / unknown</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>unknown</td></tr>
<tr><td><a id="technical_resource" href="#technical_resource_tree">technical_resource</a></td><td>To list all technical resources needed to implement a DMP</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dataset_title" href="#dataset_title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Fast car images</td></tr>
<tr><td><a id="dataset_type" href="#dataset_type_tree">type</a></td><td>Type according to: http://vocabularies.coar-repositories.org/pubby/resource_type.html</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>image</td></tr>
</tbody>
</table>

<h2 id="dataset_id_table">Properties in 'dataset_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="dataset_id_id" href="#dataset_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="dataset_id_type" href="#dataset_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>Handle</li><li>DOI</li><li>ARK</li><li>URL</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>DOI</td></ul>
</td></tr></tbody>
</table>

<h2 id="distribution_table">Properties in 'distribution'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="distribution_access_url" href="#distribution_access_url_tree">access_url</a></td><td>Access URL</td><td>URI</td><td>Zero or One</td><td>http://some.repo...</td></tr>
<tr><td><a id="distribution_available_till" href="#distribution_available_till_tree">available_till</a></td><td>Indicates how long this distribution will be/ should be available</td><td>Date</td><td>Zero or One</td><td>2030-06-30</td></tr>
<tr><td><a id="distribution_byte_size" href="#distribution_byte_size_tree">byte_size</a></td><td>Byte Size</td><td>Number</td><td>Zero or One</td><td>690000</td></tr>
<tr><td><a id="distribution_data_access" href="#distribution_data_access_tree">data_access</a></td><td>Indicates access mode for data. Allowed values: open / shared / closed</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>open</td></tr>
<tr><td><a id="distribution_description" href="#distribution_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Best quality data before resizing</td></tr>
<tr><td><a id="distribution_download_url" href="#distribution_download_url_tree">download_url</a></td><td>Download URL</td><td>URI</td><td>Zero or One</td><td>http://some.repo.../download/...</td></tr>
<tr><td><a id="distribution_format" href="#distribution_format_tree">format</a></td><td>Format according to: https://www.iana.org/assignments/media-types/media-types.xhtml if appropriate, otherwise use the common name for this format</td><td>String</td><td>Zero or More</td><td>image/tiff</td></tr>
<tr><td><a id="host" href="#host_tree">host</a></td><td>To provide information on quality of service provided by infrastructure (e.g. repository) where data is stored</td><td>Nested Data Structure</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="license" href="#license_tree">license</a></td><td>To list all licenses applied to a specific distribution of data.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="distribution_title" href="#distribution_title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Full resolution images</td></tr>
</tbody>
</table>

<h2 id="host_table">Properties in 'host'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="host_availability" href="#host_availability_tree">availability</a></td><td>Availability</td><td>String</td><td>Zero or One</td><td>99,5</td></tr>
<tr><td><a id="host_backup_frequency" href="#host_backup_frequency_tree">backup__frequency</a></td><td>Backup  Frequency</td><td>String</td><td>Zero or One</td><td>weekly</td></tr>
<tr><td><a id="host_backup_type" href="#host_backup_type_tree">backup_type</a></td><td>Backup Type</td><td>String</td><td>Zero or One</td><td>tapes</td></tr>
<tr><td><a id="host_certified_with" href="#host_certified_with_tree">certified_with</a></td><td>Repository certified to a recognised standard<br/>Allowed Values:<ul><li>DIN31644</li><li>DINI-Zertifikat</li><li>DSA</li><li>ISO16363</li><li>ISO16919</li><li>TRAC</li><li>WDS</li><li>CoreTrustSeal</li><ul/><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>CoreTrustSeal</td></ul>
<tr><td><a id="host_description" href="#host_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Repository hosted by...</td></tr>
<tr><td><a id="host_geo_location" href="#host_geo_location_tree">geo_location</a></td><td>Physical location of the data expressed using ISO 3166-1 country code.</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>AT</td></tr>
<tr><td><a id="host_pid_system" href="#host_pid_system_tree">pid_system</a></td><td>PID System: ark, doi, hdl, purl, urn, other, none</td><td>Term from Controlled Vocabulary</td><td>Zero or More</td><td>DOI</td></tr>
<tr><td><a id="storage_type" href="#storage_type_tree">storage_type</a></td><td>The type of storage required</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="host_supports_versioning" href="#host_supports_versioning_tree">support_versioning</a></td><td>Allowed values: yes / no / unknown</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>yes</td></tr>
<tr><td><a id="host_title" href="#host_title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Super Repository</td></tr>
<tr><td><a id="host_url" href="#host_url_tree">url</a></td><td>The URL of the system hosting a distribution of a dataset</td><td>URI</td><td>Exactly One</td><td> </td></tr>
</td></tr></tbody>
</table>

<h2 id="license_table">Properties in 'license'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="license_ref" href="#license_ref_tree">license_ref</a></td><td>Link to license document.</td><td>URI</td><td>Exactly One</td><td>https://creativecommons.org/licenses/by/4.0/</td></tr>
<tr><td><a id="license_start_date" href="#license_start_date_tree">start_date</a></td><td>If date is set in the future, it indicates embargo period.</td><td>Date</td><td>Exactly One</td><td>2019-06-30</td></tr>
</tbody>
</table>

<h2 id="metadata_table">Properties in 'metadata'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="metadata_description" href="#metadata_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>provides taxonomy for...</td></tr>
<tr><td><a id="metadata_language" href="#metadata_language_tree">language</a></td><td>Language</td><td>String</td><td>Exactly One</td><td>polish</td></tr>
<tr><td><a id="metadata_standard_id" href="#metadata_standard_id_tree">metadata_standard_id</a></td><td>Metadata Standard ID</td><td>Nested Data Structure</td><td>Exactly One</td><td>http://www.dublincore.org/specifications/dublin-core/dcmi-terms/</td></tr>
</tbody>
</table>

<h2 id="metadata_standard_id_table">Properties in 'metadata_standard_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="metadata_id_id" href="#metadata_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="metadata_id_type" href="#metadata_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>URL</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>URL</td></ul>
</td></tr></tbody>
</table>

<h2 id="security_privacy_table">Properties in 'security_and_privacy'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="sp_description" href="#sp_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Server with data must be kept in a locked room</td></tr>
<tr><td><a id="sp_title" href="#sp_title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Physical access control</td></tr>
</tbody>
</table>

<h2 id="technical_resource_table">Properties in 'technical_resource'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="tr_description" href="#tr_description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Device needed to collect field data...</td></tr>
<tr><td><a id="tr_id" href="#tr_id_tree">technical_reosurce_id</a></td><td>Technical Reosurce ID</td><td>String</td><td>Exactly One</td><td>123/45/43/AT</td></tr>
<tr><td><a id="tr_id_type" href="#tr_id_type_tree">technical_reosurce_id_type</a></td><td>Identifier type</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>custom</td></tr>
</tbody>
</table>

<h2 id="project_table">Properties in 'project'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="project_description" href="#project_description_tree">description</a></td><td>Project description</td><td>String</td><td>Zero or One</td><td>Project develops novel...</td></tr>
<tr><td><a id="project_end" href="#project_end_tree">end</a></td><td>Project end date</td><td>Date</td><td>Exactly One</td><td>2020-03-31</td></tr>
<tr><td><a id="funding" href="#funding_tree">funding</a></td><td>Funding related with a project</td><td>Nested Data Structure</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="project_start" href="#project_start_tree">start</a></td><td>Project start date</td><td>Date</td><td>Exactly One</td><td>2019-04-01</td></tr>
<tr><td><a id="project_title" href="#project_title_tree">title</a></td><td>Project title</td><td>String</td><td>Exactly One</td><td>Our New Project</td></tr>
</tbody>
</table>

<h2 id="funding_table">Properties in 'funding'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="funder_id" href="#funder_id_tree">funder_id</a></td><td>Funder ID, recommended to use CrossRef Funder Registry. See: https://www.crossref.org/services/funder-registry/</td><td>Nested Data Structure</td><td>Exactly One</td><td>501100002428</td></tr>
<tr><td><a id="funding_status" href="#funding_status_tree">funding_status</a></td><td>To express different phases of project lifecycle. Allowed values are: planned / applied / granted / rejected</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>granted</td></tr>
<tr><td><a id="grant_id" href="#grant_id_tree">grant_id</a></td><td> </td><td>Nested Data Structure</td><td>Exactly One</td><td>1234567</td></tr>
</tbody>
</table>

<h2 id="funder_id_table">Properties in 'funder_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="funder_id_id" href="#funder_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="funder_id_type" href="#funder_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>Fundref</li><li>URL</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>FundRef</td></ul>
</td></tr></tbody>
</table>

<h2 id="grant_id_table">Properties in 'grant_id'</h2>

<table style="width: 99%;">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="grant_id_id" href="#grant_id_id_tree">identifier</a></td><td> </td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="grant_id_type" href="#grant_id_type_tree">type</a></td><td>Identifier type<br/>Allowed Values:<ul><li>URL</li><li>Other</li><ul/><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>Other</td></ul>
</td></tr></tbody>
</table>

Published by [RDA DMP Common Standards WG](https://www.rd-alliance.org/groups/dmp-common-standards-wg).
