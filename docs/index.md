# UNDER DEVELOPMENT!
<ul><li id="DMP_tree"><a href="#DMP_table">DMP</a></li><ul><li id="contact_tree"><a href="#contact_table">contact</a></li><ul><li id="contact_id_tree"><a href="#contact_id">contact_id</a></li><li id="mail_tree"><a href="#mail">mail</a></li><li id="name_tree"><a href="#name">name</a></li></ul><li id="cost_tree"><a href="#cost_table">cost</a></li><ul><li id="description_tree"><a href="#description">description</a></li><li id="title_tree"><a href="#title">title</a></li><li id="type_tree"><a href="#type">type</a></li><li id="unit_tree"><a href="#unit">unit</a></li><li id="value_tree"><a href="#value">value</a></li></ul><li id="created_tree"><a href="#created">created</a></li><li id="dm_staff_tree"><a href="#dm_staff_table">dm_staff</a></li><ul><li id="contact_id_tree"><a href="#contact_id">contact_id</a></li><li id="mbox_tree"><a href="#mbox">mbox</a></li><li id="name_tree"><a href="#name">name</a></li><li id="role_tree"><a href="#role">role</a></li></ul><li id="dataset_tree"><a href="#dataset_table">dataset</a></li><ul><li id="data_quality_assurance_tree"><a href="#data_quality_assurance">data_quality_assurance</a></li><li id="dataset_id_tree"><a href="#dataset_id">dataset_id</a></li><li id="description_tree"><a href="#description">description</a></li><li id="distribution_tree"><a href="#distribution_table">distribution</a></li><ul><li id="access_url_tree"><a href="#access_url">access_url</a></li><li id="available_till_tree"><a href="#available_till">available_till</a></li><li id="byte_size_tree"><a href="#byte_size">byte_size</a></li><li id="data_access_tree"><a href="#data_access">data_access</a></li><li id="description_tree"><a href="#description">description</a></li><li id="download_url_tree"><a href="#download_url">download_url</a></li><li id="format_tree"><a href="#format">format</a></li><li id="host_tree"><a href="#host_table">host</a></li><ul><li id="availability_tree"><a href="#availability">availability</a></li><li id="backup__frequency_tree"><a href="#backup__frequency">backup__frequency</a></li><li id="backup_type_tree"><a href="#backup_type">backup_type</a></li><li id="certified_with_tree"><a href="#certified_with">certified_with</a></li><li id="description_tree"><a href="#description">description</a></li><li id="geo_location_tree"><a href="#geo_location">geo_location</a></li><li id="pid_system_tree"><a href="#pid_system">pid_system</a></li><li id="storage_type_tree"><a href="#storage_type">storage_type</a></li><li id="support_versioning_tree"><a href="#support_versioning">support_versioning</a></li><li id="title_tree"><a href="#title">title</a></li></ul><li id="license_tree"><a href="#license_table">license</a></li><ul><li id="license_ref_tree"><a href="#license_ref">license_ref</a></li><li id="start_date_tree"><a href="#start_date">start_date</a></li></ul><li id="media_type_tree"><a href="#media_type">media_type</a></li><li id="title_tree"><a href="#title">title</a></li></ul><li id="issued_tree"><a href="#issued">issued</a></li><li id="keyword_tree"><a href="#keyword">keyword</a></li><li id="language_tree"><a href="#language">language</a></li><li id="personal_data_tree"><a href="#personal_data">personal_data</a></li><li id="preservation_statement_tree"><a href="#preservation_statement">preservation_statement</a></li><li id="sensitive_data_tree"><a href="#sensitive_data">sensitive_data</a></li><li id="title_tree"><a href="#title">title</a></li><li id="type_tree"><a href="#type">type</a></li></ul><li id="description_tree"><a href="#description">description</a></li><li id="ethical_issues_description_tree"><a href="#ethical_issues_description">ethical_issues_description</a></li><li id="ethical_issues_exist_tree"><a href="#ethical_issues_exist">ethical_issues_exist</a></li><li id="ethical_issues_report_tree"><a href="#ethical_issues_report">ethical_issues_report</a></li><li id="metadata_tree"><a href="#metadata_table">metadata</a></li><ul><li id="description_tree"><a href="#description">description</a></li><li id="language_tree"><a href="#language">language</a></li><li id="metadata_id_tree"><a href="#metadata_id">metadata_id</a></li></ul><li id="modified_tree"><a href="#modified">modified</a></li><li id="project_tree"><a href="#project_table">project</a></li><ul><li id="description_tree"><a href="#description">description</a></li><li id="end_tree"><a href="#end">end</a></li><li id="funding_tree"><a href="#funding_table">funding</a></li><ul><li id="funder_id_tree"><a href="#funder_id">funder_id</a></li><li id="funding_status_tree"><a href="#funding_status">funding_status</a></li><li id="grant_id_tree"><a href="#grant_id">grant_id</a></li></ul><li id="start_tree"><a href="#start">start</a></li><li id="title_tree"><a href="#title">title</a></li></ul><li id="security_and_privacy_tree"><a href="#security_and_privacy_table">security_and_privacy</a></li><ul><li id="description_tree"><a href="#description">description</a></li><li id="title_tree"><a href="#title">title</a></li></ul><li id="technical_resource_tree"><a href="#technical_resource_table">technical_resource</a></li><ul><li id="description_tree"><a href="#description">description</a></li><li id="resource_id_tree"><a href="#resource_id">resource_id</a></li><li id="type_tree"><a href="#type">type</a></li></ul><li id="title_tree"><a href="#title">title</a></li></ul></ul>
<hr/>

<h2 id="DMP_table">Properties in 'DMP'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact" href="#contact_tree">contact</a></td><td>Contact person for a DMP</td><td>Nested Data Structure</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="cost" href="#cost_tree">cost</a></td><td>To list costs related to data management. Providing multiple instances of a 'Cost' allows to break down costs into details. Providing one 'Cost' instance allows to provide one aggregated sum.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="created" href="#created_tree">created</a></td><td>Date and time of the first version of a DMP. Must not be changed in subsequent DMPs.</td><td>DateTime</td><td>Exactly One</td><td>2019-03-13 13:13</td></tr>
<tr><td><a id="dm_staff" href="#dm_staff_tree">dm_staff</a></td><td>To list people that play role in data management related to this DMP, e.g. resoponsible for performing actions described in this DMP.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="dataset" href="#dataset_tree">dataset</a></td><td>To describe data on a non-technical level.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="description" href="#description_tree">description</a></td><td>To provide any free-form text information on a DMP</td><td>String</td><td>Zero or One</td><td>This DMP is for our new project</td></tr>
<tr><td><a id="ethical_issues_description" href="#ethical_issues_description_tree">ethical_issues_description</a></td><td>To describe ethical issues directly in a DMP</td><td>String</td><td>Zero or One</td><td>There are ethical issues, because...</td></tr>
<tr><td><a id="ethical_issues_exist" href="#ethical_issues_exist_tree">ethical_issues_exist</a></td><td>To indicate whether there are ethical issues related to data that this DMP describes. Value may be one of: 'yes'; 'no'; 'unknown'</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>yes</td></tr>
<tr><td><a id="ethical_issues_report" href="#ethical_issues_report_tree">ethical_issues_report</a></td><td>To indicate where a protocol from a meeting with an ethical commitee can be found</td><td>URI</td><td>Zero or One</td><td>http://report.location</td></tr>
<tr><td><a id="metadata" href="#metadata_tree">metadata</a></td><td>To describe metadata standards used. </td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="modified" href="#modified_tree">modified</a></td><td>Must be set each time DMP is modified. Indicates DMP version.</td><td>DateTime</td><td>Zero or One</td><td>2020-03-14 10:53</td></tr>
<tr><td><a id="project" href="#project_tree">project</a></td><td>Project related to a DMP</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="security_and_privacy" href="#security_and_privacy_tree">security_and_privacy</a></td><td>To list all issues and requirements related to security and privacy</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="technical_resource" href="#technical_resource_tree">technical_resource</a></td><td>To list all technical resources needed to implement a DMP</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title of a DMP</td><td>String</td><td>Zero or One</td><td>DMP for our new project</td></tr>
</tbody>
</table>

<h2 id="contact_table">Properties in 'contact'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact_id" href="#contact_id_tree">contact_id</a></td><td>Identifier for a contact person</td><td>String</td><td>Exactly One</td><td>http://orcid.org/0000-0000-0000-0000</td></tr>
<tr><td><a id="mail" href="#mail_tree">mail</a></td><td>E-mail address</td><td>String</td><td>Exactly One</td><td>cc@example.com</td></tr>
<tr><td><a id="name" href="#name_tree">name</a></td><td>Name of the contact person</td><td>String</td><td>Exactly One</td><td>Charlie Chaplin</td></tr>
</tbody>
</table>

<h2 id="cost_table">Properties in 'cost'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Costs for maintaining....</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Storage and backup</td></tr>
<tr><td><a id="type" href="#type_tree">type</a></td><td>Type</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>infrastructure</td></tr>
<tr><td><a id="unit" href="#unit_tree">unit</a></td><td>Unit</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>EUR</td></tr>
<tr><td><a id="value" href="#value_tree">value</a></td><td>Value</td><td>Number</td><td>Zero or One</td><td>1000</td></tr>
</tbody>
</table>

<h2 id="dm_staff_table">Properties in 'dm_staff'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="contact_id" href="#contact_id_tree">contact_id</a></td><td>Contact ID</td><td>String</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="mbox" href="#mbox_tree">mbox</a></td><td>Mail address</td><td>String</td><td>Zero or One</td><td>john@smith.com</td></tr>
<tr><td><a id="name" href="#name_tree">name</a></td><td>Name</td><td>String</td><td>Exactly One</td><td>John Smith</td></tr>
<tr><td><a id="role" href="#role_tree">role</a></td><td>Role</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>data steward</td></tr>
</tbody>
</table>

<h2 id="dataset_table">Properties in 'dataset'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="data_quality_assurance" href="#data_quality_assurance_tree">data_quality_assurance</a></td><td>Data Quality Assurance</td><td>String</td><td>Zero or More</td><td>We use file naming convention...</td></tr>
<tr><td><a id="dataset_id" href="#dataset_id_tree">dataset_id</a></td><td>Dataset ID</td><td>String</td><td>Zero or More</td><td>DOI</td></tr>
<tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Field observation</td></tr>
<tr><td><a id="distribution" href="#distribution_tree">distribution</a></td><td>To provide technical information on a specific instance of data.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="issued" href="#issued_tree">issued</a></td><td>Issued</td><td>Date</td><td>Zero or One</td><td>2019-06-30</td></tr>
<tr><td><a id="keyword" href="#keyword_tree">keyword</a></td><td>Keyword</td><td>String</td><td>Zero or More</td><td>keyword 1, keyword 2</td></tr>
<tr><td><a id="language" href="#language_tree">language</a></td><td>Language</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>english</td></tr>
<tr><td><a id="personal_data" href="#personal_data_tree">personal_data</a></td><td>Personal Data</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>unknown</td></tr>
<tr><td><a id="preservation_statement" href="#preservation_statement_tree">preservation_statement</a></td><td>Preservation Statement</td><td>String</td><td>Zero or One</td><td>Must be preserved to enable...</td></tr>
<tr><td><a id="sensitive_data" href="#sensitive_data_tree">sensitive_data</a></td><td>Sensitive Data</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>unknown</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Fast car images</td></tr>
<tr><td><a id="type" href="#type_tree">type</a></td><td>Type</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>images</td></tr>
</tbody>
</table>

<h2 id="distribution_table">Properties in 'distribution'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="access_url" href="#access_url_tree">access_url</a></td><td>Access URL</td><td>URI</td><td>Zero or One</td><td>http://some.repo...</td></tr>
<tr><td><a id="available_till" href="#available_till_tree">available_till</a></td><td>Indicates how long this distribution will be/ should be available</td><td>Date</td><td>Zero or One</td><td>2030-06-30</td></tr>
<tr><td><a id="byte_size" href="#byte_size_tree">byte_size</a></td><td>Byte Size</td><td>Number</td><td>Zero or One</td><td>690000</td></tr>
<tr><td><a id="data_access" href="#data_access_tree">data_access</a></td><td>Indicates access mode for data</td><td>Term from Controlled Vocabulary</td><td>Exactly One</td><td>open</td></tr>
<tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Best quality data before resizing</td></tr>
<tr><td><a id="download_url" href="#download_url_tree">download_url</a></td><td>Download URL</td><td>URI</td><td>Zero or One</td><td>http://some.repo.../download/...</td></tr>
<tr><td><a id="format" href="#format_tree">format</a></td><td>Format</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>image/tiff</td></tr>
<tr><td><a id="host" href="#host_tree">host</a></td><td>To provide information on quality of service provided by infrastructure (e.g. repository) where data is stored</td><td>Nested Data Structure</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="license" href="#license_tree">license</a></td><td>To list all licenses applied to a specific distribution of data.</td><td>Nested Data Structure</td><td>Zero or More</td><td> </td></tr>
<tr><td><a id="media_type" href="#media_type_tree">media_type</a></td><td>Media Type</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>vnd.sealed.tiff</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Full resolution images</td></tr>
</tbody>
</table>

<h2 id="host_table">Properties in 'host'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="availability" href="#availability_tree">availability</a></td><td>Availability</td><td>String</td><td>Zero or One</td><td>99,5</td></tr>
<tr><td><a id="backup__frequency" href="#backup__frequency_tree">backup__frequency</a></td><td>Backup  Frequency</td><td>String</td><td>Zero or One</td><td>weekly</td></tr>
<tr><td><a id="backup_type" href="#backup_type_tree">backup_type</a></td><td>Backup Type</td><td>String</td><td>Zero or One</td><td>tapes</td></tr>
<tr><td><a id="certified_with" href="#certified_with_tree">certified_with</a></td><td>Certified With</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>CoreTrusSeal</td></tr>
<tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Repository hosted by...</td></tr>
<tr><td><a id="geo_location" href="#geo_location_tree">geo_location</a></td><td>Geo Location</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>Europe</td></tr>
<tr><td><a id="pid_system" href="#pid_system_tree">pid_system</a></td><td>PID System</td><td>Term from Controlled Vocabulary</td><td>Zero or More</td><td>DOI, ARC, handle</td></tr>
<tr><td><a id="storage_type" href="#storage_type_tree">storage_type</a></td><td>Storage Type</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>hot</td></tr>
<tr><td><a id="support_versioning" href="#support_versioning_tree">support_versioning</a></td><td>Support Versioning</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>yes</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Super Repository</td></tr>
</tbody>
</table>

<h2 id="license_table">Properties in 'license'</h2>

<table>
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
<tr><td><a id="start_date" href="#start_date_tree">start_date</a></td><td>If date is set in the future, it indicates embargo period.</td><td>Date</td><td>Exactly One</td><td>2019-06-30</td></tr>
</tbody>
</table>

<h2 id="metadata_table">Properties in 'metadata'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>provides taxonomy for...</td></tr>
<tr><td><a id="language" href="#language_tree">language</a></td><td>Language</td><td>String</td><td>Exactly One</td><td>polish</td></tr>
<tr><td><a id="metadata_id" href="#metadata_id_tree">metadata_id</a></td><td>Metadata ID</td><td>String</td><td>Exactly One</td><td> </td></tr>
</tbody>
</table>

<h2 id="project_table">Properties in 'project'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="description" href="#description_tree">description</a></td><td>Project description</td><td>String</td><td>Zero or One</td><td>Project develops novel...</td></tr>
<tr><td><a id="end" href="#end_tree">end</a></td><td>Project end date</td><td>Date</td><td>Zero or One</td><td>2020-03-31</td></tr>
<tr><td><a id="funding" href="#funding_tree">funding</a></td><td>Funding related with a project</td><td>Nested Data Structure</td><td>Zero or One</td><td> </td></tr>
<tr><td><a id="start" href="#start_tree">start</a></td><td>Project start date</td><td>Date</td><td>Zero or One</td><td>2019-04-01</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Project title</td><td>String</td><td>Zero or One</td><td>Our New Project</td></tr>
</tbody>
</table>

<h2 id="funding_table">Properties in 'funding'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="funder_id" href="#funder_id_tree">funder_id</a></td><td>Funder ID</td><td>String</td><td>Zero or One</td><td>501100002428</td></tr>
<tr><td><a id="funding_status" href="#funding_status_tree">funding_status</a></td><td>To differentiate between states of a project, e.g. proposal vs finished</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>granted</td></tr>
<tr><td><a id="grant_id" href="#grant_id_tree">grant_id</a></td><td>Grant ID</td><td>String</td><td>Zero or One</td><td>1234567</td></tr>
</tbody>
</table>

<h2 id="security_and_privacy_table">Properties in 'security_and_privacy'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Server with data must be kept in a locked room</td></tr>
<tr><td><a id="title" href="#title_tree">title</a></td><td>Title</td><td>String</td><td>Exactly One</td><td>Physical access control</td></tr>
</tbody>
</table>

<h2 id="technical_resource_table">Properties in 'technical_resource'</h2>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Data Type</th>
      <th>Cardinality</th>
      <th>Example Value</th>
    </tr>
  </thead>
  <tbody><tr><td><a id="description" href="#description_tree">description</a></td><td>Description</td><td>String</td><td>Zero or One</td><td>Device needed to collect field data...</td></tr>
<tr><td><a id="resource_id" href="#resource_id_tree">resource_id</a></td><td>Resource ID</td><td>String</td><td>Exactly One</td><td> </td></tr>
<tr><td><a id="type" href="#type_tree">type</a></td><td>Type</td><td>Term from Controlled Vocabulary</td><td>Zero or One</td><td>infrastructure</td></tr>
</tbody>
</table>


this is the footer...