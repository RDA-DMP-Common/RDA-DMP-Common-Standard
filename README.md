<h1>RDA DMP Common Standard for machine-actionable Data Management Plans</h1><table><tr><td valign="top"><h3>About this document</h3>
This is a metadata application profile to provide basic interoperability between systems producing or consuming machine-actionable data management plans (maDMPS). Further fields can be added in specific deployments, but they do not guarantee interoperability. DMP tools can use any other fields in their internal data models.

This application profile is intended to cover a wide range of use cases and does not set any business (e.g. funder specific) requirements. It represents information over the whole DMP lifecycle.

For more information see <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/master/examples/JSON">examples</a>, <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/FAQ.md">FAQ</a> and <a href="https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/links.md">useful links to consultations, documents, tools, prototypes, etc.</a> developed by the working group.

<img src="docs/diagrams/maDMP-diagram.png"/>


<h3>DMP</h3>
Provides high level information about the DMP, e.g. its title, modification date, etc. It is the root of this application profile. The majority of its fields are mandatory.

<h3>Project</h3>
Describes the project associated with the DMP, if applicable. It can be used to describe any type of project: that is, not only funded projects, but also internal projects, PhD theses, etc.

<h3>Funding</h3>
For specifying details on funded projects, e.g. NSF of EC funded projects.

<h3>Contact</h3>
Specifies the party which can provide any information on the DMP. This is not necessarily the DMP creator, and can be a person or an organisation.

<h3>Contributor</h3>
For listing all parties involved in the process of the data management described by this DMP, and those parties involved in the creation and management of the DMP itself.

<h3>Cost</h3>
Provides a list of costs related to data management.

<h3>Dataset</h3>
This follows the defintion of Dataset in the W3C DCAT specification. Dataset can be understood as a logical entity depicting data, e.g. raw data. It provides high level information about the data. The granularity of dataset depends on a specific setting. In edge cases it can be a file, but also a collection of files in different formats. See <a href=https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/FAQ.md>FAQ</a> for more details. 

<h3>Distribution</h3>
The term "distribution" used here is as defined by the very widely used W3C DCAT metadata application profile. It is used to mean a particular instance of a dataset that has been, or is intended to be, made available in some fashion. It is important to separates the logical notion of a "dataset" from its distributions, of which there may be several, especially to attach more specific metadata properties such as "size" and "license". The lifecycle of the DMP has no particular bearing on this, and a "distribution" may be defined even if the DMP is never actually realised.

<h3>License</h3>
Used to indicate the license under which data (each specific Distribution) will be made available. It also allows for modelling embargoes. See <a href=https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/FAQ.md>FAQ</a> for more details.

<h3>Host</h3>
Provides information on the system where data is stored. It can be used to provide details on a repository where data is deposited, e.g. a Core Trust Seal certified repository located in Europe that uses DOIs. It can also provide details on systems where data is stored and processed during research, e.g. a high performance computer that uses fast storage with two daily backups.

<h3>Security and Privacy</h3>
Used to indicate any specific requirements related to security and privacy of a specific dataset, e.g. to indicate that data is not anonymized.

<h3>Technical Resource</h3>
For specifying equipment needed/used to create or process the data, e.g. a microscope, etc.  

<h3>Metadata</h3>
Provides a pointer to a metadata standard used to describe the data. It does <b>not</b> contain any actual metadata relating to the dataset.

<h3>Affiliation</h3>
For specifying the organisation(s) to which a contact or contributor belongs.

<h3>Alternate Identifier</h3>
For specifying alternate identifiers for a DMP or a dataset, e.g. an internal identifier used by a DMP tool. This is in alignment with the <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/properties/alternateidentifier/">DataCite Metadata Schema</a>.

<h3>Related Identifier</h3>
For specifying related identifiers for a DMP or a dataset, e.g. a DOI of a publication that describes the data management described in this DMP. This is in alignment with the <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/properties/relatedidentifier/">DataCite Metadata Schema</a>.

</td><td valign="top"><h3>Structure</h3>
  
<ul>
  <li id="dmp_tree"><a href="#dmp_table">dmp</a></li>
  <ul>
    <li id="dmp_alternate_identifier_tree"><a href="#alternate_identifier_table">alternate_identifier</a></li>
    <li id="dmp_contact_tree"><a href="#dmp_contact_table">contact</a></li>
    <ul>
      <li id="contact_affiliation_tree"><a href="#contact_affiliation">affiliation</a></li>
      <li id="contact_id_tree"><a href="#contact_id_table">contact_id</a></li>
      <ul>
        <li id="contact_id_identifier_tree"><a href="#contact_id_identifier">identifier</a></li>
        <li id="contact_id_type_tree"><a href="#contact_id_type">type</a></li>
      </ul>
      <li id="dmp_contact_mbox_tree"><a href="#dmp_contact_mbox">mbox</a></li>
      <li id="dmp_contact_name_tree"><a href="#dmp_contact_name">name</a></li>
    </ul>
    <li id="dmp_contributor_tree"><a href="#dmp_contributor_table">contributor</a></li>
    <ul>
      <li id="contributor_affiliation_tree"><a href="#contributor_affiliation">affiliation</a></li>
      <li id="contributor_id_tree"><a href="#contributor_id_table">contributor_id</a></li>
      <ul>
        <li id="contributor_id_id_tree"><a href="#contributor_id_id">identifier</a></li>
        <li id="contributor_id_type_tree"><a href="#contributor_id_type">type</a></li>
      </ul>
      <li id="dmp_contributor_mbox_tree"><a href="#dmp_contributor_mbox">mbox</a></li>
      <li id="dmp_contributor_name_tree"><a href="#dmp_contributor_name">name</a></li>
      <li id="dmp_contributor_role_tree"><a href="#dmp_contributor_role">role</a></li>
    </ul>
    <li id="cost_tree"><a href="#cost_table">cost</a></li>
    <ul>
      <li id="cost_unit_tree"><a href="#cost_unit">currency_code</a></li>
      <li id="cost_description_tree"><a href="#cost_description">description</a></li>
      <li id="cost_title_tree"><a href="#cost_title">title</a></li>
      <li id="cost_value_tree"><a href="#cost_value">value</a></li>
    </ul>
    <li id="dmp_created_tree"><a href="#dmp_created">created</a></li>
    <li id="dataset_tree"><a href="#dataset_table">dataset</a></li>
    <ul>
      <li id="dataset_alternate_identifier_tree"><a href="#alternate_identifier_table">alternate_identifier</a></li>
      <li id="creator_tree"><a href="#creator_table">creator</a></li>
      <ul>
        <li id="creator_affiliation_tree"><a href="#creator_affiliation">affiliation</a></li>
        <li id="creator_id_tree"><a href="#creator_id_table">creator_id</a></li>
        <ul>
          <li id="creator_id_id_tree"><a href="#creator_id_id">identifier</a></li>
          <li id="creator_id_type_tree"><a href="#creator_id_type">type</a></li>
        </ul>
        <li id="creator_mbox_tree"><a href="#creator_mbox">mbox</a></li>
        <li id="creator_name_tree"><a href="#creator_name">name</a></li>
      </ul>
      <li id="dataset_quality_assurance_tree"><a href="#dataset_quality_assurance">data_quality_assurance</a></li>
      <li id="dataset_id_tree"><a href="#dataset_id_table">dataset_id</a></li>
      <ul>
        <li id="dataset_id_id_tree"><a href="#dataset_id_id">identifier</a></li>
        <li id="dataset_id_type_tree"><a href="#dataset_id_type">type</a></li>
      </ul>
      <li id="dataset_description_tree"><a href="#dataset_description">description</a></li>
      <li id="distribution_tree"><a href="#distribution_table">distribution</a></li>
      <ul>
        <li id="distribution_access_url_tree"><a href="#distribution_access_url">access_url</a></li>
        <li id="distribution_available_until_tree"><a href="#distribution_available_until">available_until</a></li>
        <li id="distribution_byte_size_tree"><a href="#distribution_byte_size">byte_size</a></li>
        <li id="distribution_data_access_tree"><a href="#distribution_data_access">data_access</a></li>
        <li id="distribution_description_tree"><a href="#distribution_description">description</a></li>
        <li id="distribution_download_url_tree"><a href="#distribution_download_url">download_url</a></li>
        <li id="distribution_format_tree"><a href="#distribution_format">format</a></li>
        <li id="host_tree"><a href="#host_table">host</a></li>
        <ul>
          <li id="host_availability_tree"><a href="#host_availability">availability</a></li>
          <li id="host_backup_frequency_tree"><a href="#host_backup_frequency">backup_frequency</a></li>
          <li id="host_backup_type_tree"><a href="#host_backup_type">backup_type</a></li>
          <li id="host_certified_with_tree"><a href="#host_certified_with">certified_with</a></li>
          <li id="host_description_tree"><a href="#host_description">description</a></li>
          <li id="host_geo_location_tree"><a href="#host_geo_location">geo_location</a></li>
          <li id="host_id_tree"><a href="#host_id_table">host_id</a></li>
          <ul>
            <li id="host_id_id_tree"><a href="#host_id_id">identifier</a></li>
            <li id="host_id_type_tree"><a href="#host_id_type">type</a></li>
          </ul>
          <li id="host_pid_system_tree"><a href="#host_pid_system">pid_system</a></li>
          <li id="host_storage_type_tree"><a href="#host_storage_type">storage_type</a></li>
          <li id="host_supports_versioning_tree"><a href="#host_supports_versioning">support_versioning</a></li>
          <li id="host_title_tree"><a href="#host_title">title</a></li>
          <li id="host_url_tree"><a href="#host_url">url</a></li>
        </ul>
        <li id="license_tree"><a href="#license_table">license</a></li>
        <ul>
          <li id="license_ref_tree"><a href="#license_ref">license_ref</a></li>
          <li id="license_start_date_tree"><a href="#license_start_date">start_date</a></li>
        </ul>
        <li id="distribution_title_tree"><a href="#distribution_title">title</a></li>
      </ul>
      <li id="dataset_is_reused_tree"><a href="#dataset_is_reused">is_reused</a></li>
      <li id="dataset_issued_tree"><a href="#dataset_issued">issued</a></li>
      <li id="dataset_keyword_tree"><a href="#dataset_keyword">keyword</a></li>
      <li id="dataset_language_tree"><a href="#dataset_language">language</a></li>
      <li id="metadata_tree"><a href="#metadata_table">metadata</a></li>
      <ul>
        <li id="metadata_description_tree"><a href="#metadata_description">description</a></li>
        <li id="metadata_language_tree"><a href="#metadata_language">language</a></li>
        <li id="metadata_standard_id_tree"><a href="#metadata_standard_id_table">metadata_standard_id</a></li>
        <ul>
          <li id="metadata_id_id_tree"><a href="#metadata_id_id">identifier</a></li>
          <li id="metadata_id_type_tree"><a href="#metadata_id_type">type</a></li>
        </ul>
      </ul>
      <li id="dataset_personal_data_tree"><a href="#dataset_personal_data">personal_data</a></li>
      <li id="dataset_preservation_tree"><a href="#dataset_preservation">preservation_statement</a></li>
      <li id="dataset_rights_tree"><a href="#dataset_rights">rights</a></li>
      <li id="dataset_related_identifier_tree"><a href="#related_identifier_table">related_identifier</a></li>
      <li id="security_privacy_tree"><a href="#security_privacy_table">security_and_privacy</a></li>
      <ul>
        <li id="sp_description_tree"><a href="#sp_description">description</a></li>
        <li id="sp_title_tree"><a href="#sp_title">title</a></li>
      </ul>
      <li id="dataset_sensitive_data_tree"><a href="#dataset_sensitive_data">sensitive_data</a></li>
      <li id="technical_resource_tree"><a href="#technical_resource_table">technical_resource</a></li>
      <ul>
        <li id="technical_resource_description_tree"><a href="#technical_resource_description">description</a></li>
        <li id="technical_resource_name_tree"><a href="#technical_resource_name">name</a></li>
        <li id="technical_resource_id_tree"><a href="#technical_resource_id_table">technical_resource_id</a></li>
        <ul>
          <li id="technical_resource_id_id_tree"><a href="#technical_resource_id_id">identifier</a></li>
          <li id="technical_resource_id_type_tree"><a href="#technical_resource_id_type">type</a></li>
        </ul>
      </ul>
      <li id="dataset_title_tree"><a href="#dataset_title">title</a></li>
      <li id="dataset_type_tree"><a href="#dataset_type">type</a></li>
    </ul>
    <li id="dmp_description_tree"><a href="#dmp_description">description</a></li>
    <li id="dmp_id_tree"><a href="#dmp_id_table">dmp_id</a></li>
    <ul>
      <li id="dmp_id_id_tree"><a href="#dmp_id_id">identifier</a></li>
      <li id="dmp_id_type_tree"><a href="#dmp_id_type">type</a></li>
    </ul>
    <li id="ethical_issues_description_tree"><a href="#ethical_issues_description">ethical_issues_description</a></li>
    <li id="ethical_issues_exist_tree"><a href="#ethical_issues_exist">ethical_issues_exist</a></li>
    <li id="ethical_issues_report_tree"><a href="#ethical_issues_report">ethical_issues_report</a></li>
    <li id="dmp_language_tree"><a href="#dmp_language">language</a></li>
    <li id="dmp_modified_tree"><a href="#dmp_modified">modified</a></li>
    <li id="project_tree"><a href="#project_table">project</a></li>
    <ul>
      <li id="project_description_tree"><a href="#project_description">description</a></li>
      <li id="project_end_tree"><a href="#project_end">end</a></li>
      <li id="funding_tree"><a href="#funding_table">funding</a></li>
      <ul>
        <li id="funder_id_tree"><a href="#funder_id_table">funder_id</a></li>
        <ul>
          <li id="funder_id_id_tree"><a href="#funder_id_id">identifier</a></li>
          <li id="funder_id_type_tree"><a href="#funder_id_type">type</a></li>
        </ul>
        <li id="funding_status_tree"><a href="#funding_status">funding_status</a></li>
        <li id="grant_id_tree"><a href="#grant_id_table">grant_id</a></li>
        <ul>
          <li id="grant_id_id_tree"><a href="#grant_id_id">identifier</a></li>
          <li id="grant_id_type_tree"><a href="#grant_id_type">type</a></li>
        </ul>
      </ul>
      <li id="project_id_tree"><a href="#project_id_table">project_id</a></li>
      <ul>
        <li id="project_id_id_tree"><a href="#project_id_id">identifier</a></li>
        <li id="project_id_type_tree"><a href="#project_id_type">type</a></li>
      </ul>
      <li id="project_start_tree"><a href="#project_start">start</a></li>
      <li id="project_title_tree"><a href="#project_title">title</a></li>
    </ul>
    <li id="dmp_related_identifier_tree"><a href="#related_identifier_table">related_identifier</a></li>
    <li id="dmp_title_tree"><a href="#dmp_title">title</a></li>
  </ul>
  <li id="affiliation_tree"><a href="#affiliation_table">affiliation</a></li>
  <ul>
    <li id="affiliation_name_tree"><a href="#affiliation_name">name</a></li>
    <li id="affiliation_id_tree"><a href="#affiliation_id_table">affiliation_id</a></li>
    <ul>
      <li id="affiliation_id_id_tree"><a href="#affiliation_id_id">identifier</a></li>
      <li id="affiliation_id_type_tree"><a href="#affiliation_id_type">type</a></li>
    </ul>
  </ul>
  <li id="alternate_identifier_tree"><a href="#alternate_identifier_table">alternate_identifier</a></li>
  <ul>
    <li id="alternate_identifier_id_tree"><a href="#alternate_identifier_id">identifier</a></li>
    <li id="alternate_identifier_type_tree"><a href="#alternate_identifier_type">type</a></li>
  </ul>
  <li id="related_identifier_tree"><a href="#related_identifier_table">related_identifier</a></li>
  <ul>
    <li id="related_identifier_id_tree"><a href="#related_identifier_id">identifier</a></li>
    <li id="related_identifier_type_tree"><a href="#related_identifier_type">type</a></li>
    <li id="related_identifier_relation_type_tree"><a href="#related_identifier_relation_type">relation_type</a></li>
    <li id="related_identifier_metadata_scheme_tree"><a href="#related_identifier_metadata_scheme">metadata_scheme</a></li>
    <li id="related_identifier_scheme_uri_tree"><a href="#related_identifier_scheme_uri">scheme_uri</a></li>
    <li id="related_identifier_scheme_type_tree"><a href="#related_identifier_scheme_type">scheme_type</a></li>
    <li id="related_identifier_resource_type_tree"><a href="#related_identifier_resource_type">resource_type</a></li>
  </ul>
</ul>

</td></tr></table>

<hr/>

<h2 id="affiliation_table">Properties in 'affiliation'</h2>

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
  <tbody>
    <tr>  
      <td valign="top"><a id="affiliation_id" href="#affiliation_id_tree">affiliation_id</a></td>
      <td valign="top">Identifier for an affiliation</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1</td>
      <td valign="top"></td>
    </tr>
    <tr>
      <td valign="top"><a id="affiliation_name" href="#affiliation_name_tree">name</a></td>
      <td valign="top">Name of an affiliation</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Some University</td>
    </tr>
  </tbody>
</table>

<h2 id="affiliation_id_table">Properties in 'affiliation_id'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="affiliation_id_id" href="#affiliation_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for an affiliation</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">03yrm5c26</td>
    </tr>
    <tr>
      <td valign="top"><a id="affiliation_id_type" href="#affiliation_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for an affiliation. Suggested Values: ror, grid, isni</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">ror</td>
    </tr>
  </tbody>

<h2 id="alternate_identifier_table">Properties in 'alternate_identifier'</h2>

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
  <tbody>
    <tr>  
      <td valign="top"><a id="alternate_identifier_id" href="#alternate_identifier_id_tree">identifier</a></td>
      <td valign="top">Value of the identifier</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">E-GEOD-34814</td>
    </tr>
    <tr>
      <td valign="top"><a id="alternate_identifier_type" href="#alternate_identifier_type_tree">type</a></td>
      <td valign="top">Type of the identifier</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Local accession number</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="contact_affiliation" href="#affiliation_tree">affiliation</a></td>
      <td valign="top">Affiliations of a contact</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>  
      <td valign="top"><a id="contact_id" href="#contact_id_tree">contact_id</a></td>
      <td valign="top">Identifier for a contact</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contact_mbox" href="#dmp_contact_mbox_tree">mbox</a></td>
      <td valign="top">E-mail address for a contact</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">cc@example.com</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contact_name" href="#dmp_contact_name_tree">name</a></td>
      <td valign="top">Name of a contact person or organisation</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Charlie Chaplin</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="contact_id_identifier" href="#contact_id_identifier_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a contact</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">0000-0000-0000-0000</td>
    </tr>
    <tr>
      <td valign="top"><a id="contact_id_type" href="#contact_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a contact. Suggested Values: orcid, isni, openid</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">orcid</td>
    </tr>
  </tbody>
</table>

<h2 id="dmp_contributor_table">Properties in 'contributor'</h2>

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
  <tbody>
    <tr>  
      <td valign="top"><a id="contributor_affiliation" href="#affiliation_tree">affiliation</a></td>
      <td valign="top">Affiliations of a contributor</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="contributor_id" href="#contributor_id_tree">contributor_id</a></td>
      <td valign="top">Identifier for a contributor</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td><td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contributor_mbox" href="#dmp_contributor_mbox_tree">mbox</a></td>
      <td valign="top">E-mail address for a contributor</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td><td valign="top">john@smith.com</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contributor_name" href="#dmp_contributor_name_tree">name</a></td>
      <td valign="top">Name of a contributor</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">John Smith</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contributor_role" href="#dmp_contributor_role_tree">role</a></td>
      <td valign="top">Contributors role(s) within the process of data management (incl. planning). It is recommended to use <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/contributorType/" target="_blank">contributor types of DataCite Metadata Schema</a>.</td>
      <td valign="top">String</td>
      <td valign="top">1..n</td>
      <td valign="top">DataManager, Researcher</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="contributor_id_id" href="#contributor_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a contributor</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">0000-0000-0000-0000</td>
    </tr>
    <tr>
      <td valign="top"><a id="contributor_id_type" href="#contributor_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a contributor. Suggested Values: orcid, isni, openid.</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">orcid</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="cost_unit" href="#cost_unit_tree">currency_code</a></td>
      <td valign="top">Allowed values defined by ISO 4217.</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td><td valign="top">EUR</td>
    </tr>
    <tr>
      <td valign="top"><a id="cost_description" href="#cost_description_tree">description</a></td>
      <td valign="top">To provide additional details about a cost, including specifying which activities or resources it relates to, such as making data FAIR, ensuring data accessibility, or enhancing its reusability.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">Storage and backup costs are calculated based on a 12-month storage period, daily incremental and weekly full backups, and a frequency of 4 restores per month, as outlined in the evaluation table at www.example-storagecostevaluation.com.</td>
    </tr>
    <tr>
      <td valign="top"><a id="cost_title" href="#cost_title_tree">title</a></td>
      <td valign="top">Title of a cost</td>
      <td valign="top">String</td>
      <td valign="top">1</td><td valign="top">Storage and backup</td>
    </tr>
    <tr>
      <td valign="top"><a id="cost_value" href="#cost_value_tree">value</a></td>
      <td valign="top">Cost value in the specified currency</td>
      <td valign="top">Number</td>
      <td valign="top">0..1</td>
      <td valign="top">1000</td>
    </tr>
  </tbody>
</table>

<h2 id="creator_table">Properties in 'creator'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="creator_affiliation" href="#affiliation_tree">affiliation</a></td>
      <td valign="top">Affiliations of a creator</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="creator_id" href="#creator_id_tree">creator_id</a></td>
      <td valign="top">Identifier for a creator</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="creator_mbox" href="#creator_mbox_tree">mbox</a></td>
      <td valign="top">E-mail address for a creator</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">john.doe@example.com</td>
    </tr>
    <tr>
      <td valign="top"><a id="creator_name" href="#creator_name_tree">name</a></td>
      <td valign="top">Name of a creator person or organisation</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">John Doe</td>
    </tr>
  </tbody>
</table>

<h2 id="creator_id_table">Properties in 'creator_id'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="creator_id_id" href="#creator_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a creator</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">s0000-0000-0000-0000</td>
    </tr>
    <tr>
      <td valign="top"><a id="creator_id_type" href="#creator_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a creator. <br/>Suggested Values: orcid, isni, openid, other</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">orcid</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="dataset_alternate_identifier" href="#dataset_alternate_identifier_tree">alternate_identifier</a></td>
      <td valign="top">To provide alternative identifiers for a dataset, which can be used to reference or cite the dataset in different contexts or systems. Alternative identifiers can include local accession numbers, internal database IDs, or other unique codes assigned to the dataset by various organizations or repositories.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="creator" href="#creator_tree">creator</a></td>
      <td valign="top">To specify the creators of the dataset.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_quality_assurance" href="#dataset_quality_assurance_tree">data_quality_assurance</a></td>
      <td valign="top">To describe any quality assurance processes applied to a dataset, such as, to ensure its accuracy, reliability, consistency, and usability for its intended purposes. This includes systematic practices, procedures, and policies designed to maintain high data quality throughout its lifecycle.</td>
      <td valign="top">String</td>
      <td valign="top">0..n</td>
      <td valign="top">We calibrate measuring equipment daily, run repeat samples to monitor consistency in measurements and results, and cross-check collected data with at least two colleagues for accuracy.</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_id" href="#dataset_id_tree">dataset_id</a></td>
      <td valign="top">Identifier for a dataset</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_description" href="#dataset_description_tree">description</a></td>
      <td valign="top">Description is a property in both Dataset and Distribution, in compliance with W3C DCAT. In some cases these might be identical, but in most cases the Dataset represents a more abstract concept, while the distribution can point to a specific file.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">The dataset includes detailed measurements of temperature, humidity, and soil moisture levels collected at various time intervals (every 30 minutes) across multiple locations. The dataset will also include metadata such as GPS coordinates, sensor calibration data, and environmental conditions. The primary objective of this dataset is to analyze the correlation between these variables and their impact on plant growth patterns over a 6-month period.</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution" href="#distribution_tree">distribution</a></td>
      <td valign="top">To provide technical information on a specific instance of data.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_is_reused" href="#dataset_is_reused_tree">is_reused</a></td>
      <td valign="top">Indication if the dataset is reused, i.e., not produced in project(s) covered by this DMP.</td>
      <td valign="top">Boolean</td>
      <td valign="top">0..1</td>
      <td valign="top">true</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_issued" href="#dataset_issued_tree">issued</a></td>
      <td valign="top">To indicate a date when a dataset was published or released. Encoded using the relevant ISO 8601 Date <a href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">Date</td>
      <td valign="top">0..1</td>
      <td valign="top">2019-06-30</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_keyword" href="#dataset_keyword_tree">keyword</a></td>
      <td valign="top">Keyword</td>
      <td valign="top">String</td>
      <td valign="top">0..n</td>
      <td valign="top">keyword 1, keyword 2</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_language" href="#dataset_language_tree">language</a></td>
      <td valign="top">Language of the dataset expressed using ISO 639-3</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td>
      <td valign="top">eng</td>
    </tr>
    <tr>
      <td valign="top"><a id="metadata" href="#metadata_tree">metadata</a></td>
      <td valign="top">To describe metadata standards used.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_personal_data" href="#dataset_personal_data_tree">personal_data</a></td>
      <td valign="top">To indicate whether a dataset contains personal data. Personal data refers to any data that can identify an individual (e.g. name, birthdate, address, voice recordings, etc.).<br/>Allowed Values: yes, no, unknown</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td>
      <td valign="top">unknown</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_preservation" href="#dataset_preservation_tree">preservation_statement</a></td>
      <td valign="top">To outline a plan for how and why a dataset will be preserved for long-term access, including for example storage redundancy, integrity checks (checksums, fixity checks), format migration,  and a sustainability plan ensuring institutional commitment and funding.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">All research data will be stored in the university's secure data repository, backed up daily to ensure redundancy and prevent data loss. The dataset will be preserved in a standardized format (e.g. CSV, JSON) and will include detailed metadata for clarity. It will be accessible to the public via the university’s open-access platform three months after the completion of the project, with ongoing access ensured for a minimum of 5 years. Regular checks will be performed every 6 months to confirm the integrity and readability of the data.</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_rights" href="#dataset_rights_tree">rights</a></td>
      <td valign="top">A statement that concerns all rights not addressed with license, such as copyright statements.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">This dataset incorporates third-party materials that are subject to additional rights and restrictions. Users must obtain permission from the original rights holders before reuse.</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_related_identifier" href="#dataset_related_identifier_tree">related_identifier</a></td>
      <td valign="top">To provide references to related resources, such as publications, datasets or software, that are associated with the dataset. This helps to establish connections between different research outputs and enhances the discoverability and context of the dataset.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="security_privacy" href="#security_privacy_tree">security_and_privacy</a></td>
      <td valign="top">To list all security and privacy measures applied to a dataset to protect sensitive information, for example encryption, anonymization, data masking, and compliance with data protection regulations (e.g. GDPR or HIPAA). It can also be used to express any security measures required for handling the dataset, e.g. only physical access, etc. </td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_sensitive_data" href="#dataset_sensitive_data_tree">sensitive_data</a></td>
      <td valign="top">To indicate whether a dataset contains sensitive data. Sensitive data refers to information that could pose risks to individuals or organizations for example  financial information, medical records, passwords and social security numbers.<br/>Allowed Values: yes, no, unknown</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td>
      <td valign="top">unknown</td>
    </tr>
    <tr>
      <td valign="top"><a id="technical_resource" href="#technical_resource_tree">technical_resource</a></td>
      <td valign="top">List all technical resources (e.g. tools or software) required for any stage of a dataset lifecycle (e.g. microscopes, sensors, Jupyter Notebook, Galaxy workflows, measuring devices)</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_title" href="#dataset_title_tree">title</a></td>
      <td valign="top">Title is a property in both Dataset and Distribution, in compliance with W3C DCAT. In some cases these might be identical, but in most cases the Dataset represents a more abstract concept, while the distribution can point to a specific file.</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Fast car images</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_type" href="#dataset_type_tree">type</a></td>
      <td valign="top">If appropriate, type according to: DataCite and/or COAR dictionary. Otherwise use the common name for the type, e.g. raw data, software, survey, etc. https://schema.datacite.org/meta/kernel-4.1/doc/DataCite-MetadataKernel_v4.1.pdf http://vocabularies.coar-repositories.org/pubby/resource_type.html</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">image</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="dataset_id_id" href="#dataset_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a dataset</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">11353/10.923628</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset_id_type" href="#dataset_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a dataset. Suggested Values: handle, doi, ark, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">handle</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="distribution_access_url" href="#distribution_access_url_tree">access_url</a></td>
      <td valign="top">A URL of the resource that gives access to a distribution of the dataset. e.g. landing page.</td>
      <td valign="top">URL</td>
      <td valign="top">0..1</td>
      <td valign="top">http://some.repo...</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_available_until" href="#distribution_available_until_tree">available_until</a></td>
      <td valign="top">Indicates how long this distribution will be/ should be available. Encoded using the relevant ISO 8601 Date <a href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">Date</td>
      <td valign="top">0..1</td>
      <td valign="top">2030-06-30</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_byte_size" href="#distribution_byte_size_tree">byte_size</a></td>
      <td valign="top">Size of a distribution in bytes</td>
      <td valign="top">Number</td>
      <td valign="top">0..1</td>
      <td valign="top">690000</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_data_access" href="#distribution_data_access_tree">data_access</a></td>
      <td valign="top">Indicates access mode for data.<br/>Allowed Values: open, shared, closed</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td>
      <td valign="top">open</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_description" href="#distribution_description_tree">description</a></td>
      <td valign="top">Description is a property in both Dataset and Distribution, in compliance with W3C DCAT. In some cases these might be identical, but in most cases the Dataset represents a more abstract concept, while the distribution can point to a specific file.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">This dataset contains measurements from a single research location at the University of California's Arboretum in Davis, California, collected every 30 minutes over a 6-month period from January 2024 until June 2024. Each file includes time-stamped data for temperature, humidity, and soil moisture, listed by date and time. The data is organized in CSV format, with each row representing a specific time point, including the location (UC Arboretum), timestamp, and the corresponding environmental variables.</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_download_url" href="#distribution_download_url_tree">download_url</a></td>
      <td valign="top">The URL of the downloadable file in a given format. E.g. CSV file or RDF file.</td>
      <td valign="top">URL</td>
      <td valign="top">0..1</td>
      <td valign="top">http://some.repo.../download/...</td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_format" href="#distribution_format_tree">format</a></td>
      <td valign="top">Format according to: https://www.iana.org/assignments/media-types/media-types.xhtml if appropriate, otherwise use the common name for this format</td>
      <td valign="top">String</td>
      <td valign="top">0..n</td>
      <td valign="top">image/tiff</td>
    </tr>
    <tr>
      <td valign="top"><a id="host" href="#host_tree">host</a></td>
      <td valign="top">To provide information on a system where data is stored. This can be all types of systems used within the whole data management lifecycle, i.e. temporary storage on networked hard drives, as well as, repository systems where data is shared with others.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..1</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="license" href="#license_tree">license</a></td>
      <td valign="top">To list all licenses applied to a specific distribution of data.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="distribution_title" href="#distribution_title_tree">title</a></td>
      <td valign="top">Title is a property in both Dataset and Distribution, in compliance with W3C DCAT. In some cases these might be identical, but in most cases the Dataset represents a more abstract concept, while the distribution can point to a specific file.</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Full resolution images</td>
    </tr>
  </tbody>
</table>

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
  <tbody>
    <tr>
      <td valign="top"><a id="dmp_alternate_identifier" href="#dmp_alternate_identifier_tree">alternate_identifier</a></td>
      <td valign="top">To provide alternative or secondary identifiers for a DMP, which can be used to reference or cite the dataset in different contexts or systems. Alternative identifiers can include other PIDs from DMP storage systems, internal database IDs, or other unique codes assigned to the DMP by various organizations or services.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contact" href="#dmp_contact_tree">contact</a></td>
      <td valign="top">Contact person for a DMP</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_contributor" href="#dmp_contributor_tree">contributor</a></td>
      <td valign="top">To list people that play role in data management related to this DMP, e.g. resoponsible for performing actions described in this DMP.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="cost" href="#cost_tree">cost</a></td>
      <td valign="top">To list costs related to data management. Providing multiple instances of a 'Cost' allows to break down costs into details. Providing one 'Cost' instance allows to provide one aggregated sum.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_created" href="#dmp_created_tree">created</a></td>
      <td valign="top">Date and time of the first version of a DMP. Must not be changed in subsequent DMPs. Encoded using the relevant ISO 8601 Date and Time (with timezone) <a href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">DateTime</td>
      <td valign="top">1</td>
      <td valign="top">2019-03-13T13:13:00Z</td>
    </tr>
    <tr>
      <td valign="top"><a id="dataset" href="#dataset_tree">dataset</a></td>
      <td valign="top">To describe data on a non-technical level.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_description" href="#dmp_description_tree">description</a></td>
      <td valign="top">Any text related to this DMP, optionally describing the project. It can include important information that doesn't fit elsewhere.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">This DMP is for our new project</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_id" href="#dmp_id_tree">dmp_id</a></td>
      <td valign="top">Identifier for the DMP itself</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="ethical_issues_description" href="#ethical_issues_description_tree">ethical_issues_description</a></td>
      <td valign="top">To describe considerations that require compliance with laws and regulations (e.g. GDPR, animal welfare) due to the involvement of humans, animals, or sensitive information. This includes ensuring informed consent from participants, protecting privacy and confidentiality, and adhering to applicable legal and ethical standards throughout the research.</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">There are ethical issues, because...</td>
    </tr>
    <tr>
      <td valign="top"><a id="ethical_issues_exist" href="#ethical_issues_exist_tree">ethical_issues_exist</a></td>
      <td valign="top">To indicate whether there are ethical issues related to data that this DMP describes.<br/>Allowed Values: yes, no, unknown</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td>
      <td valign="top">yes</td>
    </tr>
    <tr>
      <td valign="top"><a id="ethical_issues_report" href="#ethical_issues_report_tree">ethical_issues_report</a></td>
      <td valign="top">To indicate where a report/document that details all identified ethical issues (might be for example emit from a meeting with an ethical committee), preferably in URL format</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">http://report.location</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_language" href="#dmp_language_tree">language</a></td>
      <td valign="top">Language of the DMP expressed using ISO 639-3</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td><td valign="top">eng</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_modified" href="#dmp_modified_tree">modified</a></td>
      <td valign="top">Must be set each time DMP is modified. Indicates a DMP version. Encoded using the relevant ISO 8601 Date and Time (with timezone) <a href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">DateTime</td>
      <td valign="top">1</td>
      <td valign="top">2020-03-14T10:53:49Z</td>
    </tr>
    <tr>
      <td valign="top"><a id="project" href="#project_tree">project</a></td>
      <td valign="top">To list all project(s) for which the data and work are described in this DMP</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_related_identifier" href="#dmp_related_identifier_tree">related_identifier</a></td>
      <td valign="top">To provide identifiers of related resources, e.g. a project page, previous DMP versions, or a publication that describes this DMP.</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_title" href="#dmp_title_tree">title</a></td>
      <td valign="top">Title of a DMP</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">DMP for our new project</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="dmp_id_id" href="#dmp_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a DMP</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">10.1371/journal.pcbi.1006750</td>
    </tr>
    <tr>
      <td valign="top"><a id="dmp_id_type" href="#dmp_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a DMP. Suggested Values: handle, doi, ark, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">doi</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="funder_id_id" href="#funder_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a funder. It is recommended to use <a href="https://www.crossref.org/services/funder-registry/" target="_blank">CrossRef Funder Registry</a>.</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">501100002428</td>
    </tr>
    <tr>
      <td valign="top"><a id="funder_id_type" href="#funder_id_type_tree">type</a></td>
      <td valign="top">To specify a type of identifier for a funder. Suggested Values: fundref, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">fundref</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="funder_id" href="#funder_id_tree">funder_id</a></td>
      <td valign="top">Identifier of a funder</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="funding_status" href="#funding_status_tree">funding_status</a></td>
      <td valign="top">To express different phases of project lifecycle.<br/>Allowed Values: planned, applied, granted, rejected</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td>
      <td valign="top">granted</td>
    </tr>
    <tr>
      <td valign="top"><a id="grant_id" href="#grant_id_tree">grant_id</a></td>
      <td valign="top">Identifier of a grant</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..1</td>
      <td valign="top">1234567</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="grant_id_id" href="#grant_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a grant</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">http://example.com/grants/776242</td>
    </tr>
    <tr>
      <td valign="top"><a id="grant_id_type" href="#grant_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a grant. Suggested Values: doi, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="host_availability" href="#host_availability_tree">availability</a></td>
      <td valign="top">Availability of a host (preferably as a percentage)</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">99,5</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_backup_frequency" href="#host_backup_frequency_tree">backup_frequency</a></td>
      <td valign="top">Frequency of backups provided by a host</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">weekly</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_backup_type" href="#host_backup_type_tree">backup_type</a></td>
      <td valign="top">Location and/or type of the backup provided by a host</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">tapes</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_certified_with" href="#host_certified_with_tree">certified_with</a></td>
      <td valign="top">To indicate host trustworthiness via a standard repository certificate.<br/>Allowed Values: din31644, dini-zertifikat, dsa, iso16363, iso16919, trac, wds, coretrustseal</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td>
      <td valign="top">coretrustseal</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_description" href="#host_description_tree">description</a></td>
      <td valign="top">Description</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">Repository hosted by...</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_geo_location" href="#host_geo_location_tree">geo_location</a></td>
      <td valign="top">Physical location of a server (where the distribution is actually stored) expressed using ISO 3166-1 country code.</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td>
      <td valign="top">AT</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_id" href="#host_id_tree">host_id</a></td>
      <td valign="top">Identifier of Host</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="host_pid_system" href="#host_pid_system_tree">pid_system</a></td>
      <td valign="top">PID System used by a host.<br/>Allowed Values: ark, arxiv, bibcode, doi, ean13, eissn, handle, igsn, isbn, issn, istc, lissn, lsid, pmid, purl, upc, url, urn, other</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..n</td>
      <td valign="top">doi</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_storage_type" href="#host_storage_type_tree">storage_type</a></td>
      <td valign="top">To indicate whether a host supports versioning of data distributions. </td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">LTO-8 tape</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_supports_versioning" href="#host_supports_versioning_tree">support_versioning</a></td>
      <td valign="top"><br/>Allowed Values: yes, no, unknown</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">0..1</td>
      <td valign="top">yes</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_title" href="#host_title_tree">title</a></td>
      <td valign="top">Title</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Super Repository</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_url" href="#host_url_tree">url</a></td>
      <td valign="top">A URL of an infrastructure hosting a distribution of a dataset</td>
      <td valign="top">URL</td>
      <td valign="top">1</td>
      <td valign="top">https://zenodo.org</td>
    </tr>
  </tbody>
</table>

<h2 id="host_id_table">Properties in 'host_id'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="host_id_id" href="#host_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a host</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">https://example.org/repo</td>
    </tr>
    <tr>
      <td valign="top"><a id="host_id_type" href="#host_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a host.  Suggested Values: url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="license_ref" href="#license_ref_tree">license_ref</a></td>
      <td valign="top">Link to license document.</td>
      <td valign="top">URL</td>
      <td valign="top">1</td>
      <td valign="top">https://creativecommons.org/licenses/by/4.0/</td>
    </tr>
    <tr>
      <td valign="top"><a id="license_start_date" href="#license_start_date_tree">start_date</a></td>
      <td valign="top">If date is set in the future, it indicates embargo period. Encoded using the relevant ISO 8601 Date <a href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">Date</td>
      <td valign="top">1</td>
      <td valign="top">2019-06-30</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="metadata_description" href="#metadata_description_tree">description</a></td>
      <td valign="top">To provide any details on the choice of the metadata standard</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">The ISO 19115 Metadata Standard is applied to describe each geospatial dataset. Metadata includes the satellite's sensor type (e.g. Landsat 8 OLI), acquisition date, spatial resolution (30m), and cloud cover percentage.</td>
    </tr>
    <tr>
      <td valign="top"><a id="metadata_language" href="#metadata_language_tree">language</a></td>
      <td valign="top">Language of a metadata expressed using ISO 639-3</td>
      <td valign="top">Term from Controlled Vocabulary</td>
      <td valign="top">1</td><td valign="top">eng</td>
    </tr>
    <tr>
      <td valign="top"><a id="metadata_standard_id" href="#metadata_standard_id_tree">metadata_standard_id</a></td>
      <td valign="top">Identifier of Metadata Standard</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">1..n</td>
      <td valign="top"> </td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="metadata_id_id" href="#metadata_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a metadata standard</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">http://www.dublincore.org/specifications/dublin-core/dcmi-terms/</td>
    </tr>
    <tr>
      <td valign="top"><a id="metadata_id_type" href="#metadata_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a metadata standard. Suggested Values: doi, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="project_description" href="#project_description_tree">description</a></td>
      <td valign="top">Project abstract providing an overview of the project's goals and scope</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">This project aims to analyze the impact of urbanization on local biodiversity by collecting and assessing environmental data from multiple urban centers. Using remote sensing, field observations, and statistical modeling, the study will identify key factors influencing species diversity and habitat loss. The findings will support sustainable urban planning initiatives and inform conservation strategies.
      </td>
    </tr>
    <tr>
      <td valign="top"><a id="project_end" href="#project_end_tree">end</a></td>
      <td valign="top">Project end date. Encoded using the relevant ISO 8601 Date <a
          href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">Date</td>
      <td valign="top">0..1</td>
      <td valign="top">2020-03-31</td>
    </tr>
    <tr>
      <td valign="top"><a id="funding" href="#funding_tree">funding</a></td>
      <td valign="top">Funding related with a project</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"></td>
    </tr>
    <tr>
      <td valign="top"><a id="project_id" href="#project_id_tree">project_id</a></td>
      <td valign="top">Identifier of Project</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
    <tr>
      <td valign="top"><a id="project_start" href="#project_start_tree">start</a></td>
      <td valign="top">Project start date. Encoded using the relevant ISO 8601 Date <a
          href="https://www.w3.org/TR/NOTE-datetime">compliant string</a></td>
      <td valign="top">Date</td>
      <td valign="top">0..1</td>
      <td valign="top">2019-04-01</td>
    </tr>
    <tr>
      <td valign="top"><a id="project_title" href="#project_title_tree">title</a></td>
      <td valign="top">Project title</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Our New Project</td>
    </tr>
  </tbody>
</table>

<h2 id="project_id_table">Properties in 'project_id'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="project_id_id" href="#project_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a project</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">https://example.org/project</td>
    </tr>
    <tr>
      <td valign="top"><a id="project_id_type" href="#project_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a project. Suggested Values: doi, raid, url</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
  </tbody>
</table>

<h2 id="related_identifier_table">Properties in 'related_identifier'</h2>

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
  <tbody>
    <tr>  
      <td valign="top"><a id="related_identifier_id" href="#related_identifier_id_tree">identifier</a></td>
      <td valign="top">Value of the identifier</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">https://example.com/</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_metadata_scheme" href="#related_identifier_metadata_scheme_tree">metadata_scheme</a></td>
      <td valign="top">Name of the related metadata schema (if applicable)</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">DDI-L</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_relation_type" href="#related_identifier_relation_type_tree">relation_type</a></td>
      <td valign="top">Type of relation between the resource and the related resource, suggested values from DataCite <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/" target="_blank">relationType</a></td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">HasMetadata</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_resource_type" href="#related_identifier_resource_type_tree">resource_type</a></td>
      <td valign="top">Type of the related resource, suggested values from DataCite
        <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/resourceTypeGeneral/" target="_blank">resourceTypeGeneral</a></td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">Model</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_scheme_type" href="#related_identifier_scheme_type_tree">scheme_type</a></td>
      <td valign="top">Type of the related metadata scheme linked with scheme URI (if applicable)</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">XSD</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_scheme_uri" href="#related_identifier_scheme_uri_tree">scheme_uri</a></td>
      <td valign="top">Link to the scheme of the identifier (if applicable)</td>
      <td valign="top">URI</td>
      <td valign="top">0..1</td>
      <td valign="top">http://www.ddialliance.org/Specification/DDI-Lifecycle/3.1/XMLSchema/instance.xsd</td>
    </tr>
    <tr>
      <td valign="top"><a id="related_identifier_type" href="#related_identifier_type_tree">type</a></td>
      <td valign="top">Type of the identifier, suggested values from DataCite <a href="https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relatedIdentifierType/" target="_blank">relatedIdentifierType</a></td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <td valign="top"><a id="sp_description" href="#sp_description_tree">description</a></td>
      <td valign="top">Describe a security and privacy measure applied to a dataset to protect sensitive information</td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">The dataset undergoes anonymization by applying data masking techniques. Names, addresses, and phone numbers are replaced with pseudonyms or randomly generated identifiers. Specific details, such as exact birthdates, are generalized into age ranges.
      </td>
    </tr>
    <tr>
      <td valign="top"><a id="sp_title" href="#sp_title_tree">title</a></td>
      <td valign="top">Title a measure applied to a dataset</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Anonymization of Personally Identifiable Data</td>
    </tr>
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
  <tbody>
    <tr>
      <td valign="top"><a id="technical_resource_description" href="#technical_resource_description_tree">description</a>
      </td>
      <td valign="top">Describe a technical resource (e.g. tools or software) required for any stage of a dataset lifecycle (e.g. microscopes, sensors, Jupyter Notebook, Galaxy workflows, measuring devices)
      </td>
      <td valign="top">String</td>
      <td valign="top">0..1</td>
      <td valign="top">The Celestron 44102 Inverted Biological Microscope was used to examine biological samples, such as cells and microorganisms, with high-resolution optics.
      </td>
    </tr>
    <tr>
      <td valign="top"><a id="technical_resource_name" href="#technical_resource_name_tree">name</a></td>
      <td valign="top">Name a resource applied to a dataset</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">Celestron Microscope</td>
    </tr>
    <tr>
      <td valign="top"><a id="technical_resource_id" href="#technical_resource_id_tree">technical_resource_id</a></td>
      <td valign="top">Identifier of a technical resource</td>
      <td valign="top">Nested Data Structure</td>
      <td valign="top">0..n</td>
      <td valign="top"> </td>
    </tr>
  </tbody>
</table>

<h2 id="technical_resource_id_table">Properties in 'technical_resource_id'</h2>

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
  <tbody>
    <tr>
      <td valign="top"><a id="technical_resource_id_id" href="#technical_resource_id_id_tree">identifier</a></td>
      <td valign="top">To indicate the specific value of an identifier for a technical resource</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">https://example.org/resource</td>
    </tr>
    <tr>
      <td valign="top"><a id="technical_resource_id_type" href="#technical_resource_id_type_tree">type</a></td>
      <td valign="top">To specify a type of an identifier for a technical resource. Suggested Values: doi, url, other</td>
      <td valign="top">String</td>
      <td valign="top">1</td>
      <td valign="top">url</td>
    </tr>
  </tbody>
</table>

<h1>Cite as</h1>

Tomasz Miksa, Paul Walk, Peter Neish. RDA DMP Common Standard for Machine-actionable Data Management Plans. http://doi.org/10.15497/rda00039
