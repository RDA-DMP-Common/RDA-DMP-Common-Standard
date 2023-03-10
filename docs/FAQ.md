<h1> Frequently Asked Questions </h1>
Index:

* [When to use this standard?](#when-to-use-the-model)
* [Do I need to populate all fields?](#do-i-need-to-populate-all-fields)
* [What is the granularity of a Dataset?](#what-is-the-granularity-of-a-dataset)
* [What is a difference between Dataset and a Distribution?](#what-is-a-difference-between-dataset-and-a-distribution)
* [How versioning works?](#how-versioning-works)
* [How to express something is planned?](#how-to-express-something-is-planned)
* [How to indicate actions that were performed?](#how-to-indicate-actions-that-were-performed)
* [How to model embargoes?](#how-to-model-embargoes)
* [Why Metadata is referenced from a Dataset?](#why-metadata-is-referenced-from-a-dataset)
* [Are there any other serialisations planned different than JSON?](#are-there-any-other-serialisations-planned-different-tham-json)
* [Is there a JSON schema?](#is-there-a-JSON-schema)

### When to use this standard?
The standard is meant for exchange of machine-actionable DMPs between systems. It is independent of any internal data organisation used by these systems. The standard also does not prescribe how information must be presented to the end user and do not enforce any specific logic on how this information must be collected or used. The standard is an information carrier and the full machine-actionability can only be achieved when systems using the standard implement appropriate logic.

### Do I need to populate all fields?
No. Only those fields for which the cardinality is set to "exactly one" or "one to many". Further fields defined in the standard may be set if required (by business constraints), or when the information becomes available.

The standard aims to be flexible and for this reason many fields are optional. In specific deployments requirements may be stricter, for example: DMP must contain information on a project number (funder requirement), while in the standard specification this is optional.

All tools compliant to the standard, must expect to receive both obligatory and optional fields.

[Here](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex8-dmp-minimal-content.json) you can find an example of a minimum DMP.

### What is the granularity of a Dataset?
It depends on a specific setting in which the standard is used.

If a DMP contains only one Dataset (the most generic setting), it can denote that all data, for which the DMP is created, is considered jointly. For example, if a DMP is a short document created before a project begins and contains only an outline of planned actions.

If a DMP contains more than one Dataset, then each dataset can represent a logical group of data, e.g. raw data, software, publication, etc. Thus, the standard allows to express that different data is handled in a different way. For example, software is deposited in a source code repository under embargo, while a publication is instantly available from a pre-print server.

### What is a difference between Dataset and a Distribution?
Dataset and Distribution are defined as in W3C DCAT specification.

Dataset can be understood as a logical entity depicting data, e.g. raw data, software, publication, etc. Distribution points to a specific instance of a dataset. Hence, distribution contains information like format and size of files.

A dataset can have several distributions. For example, a publication can be both available as PDF and DOCX.

Furthermore, dataset can have many distributions to indicate where the data is kept temporarily, for example during a project, and where the data is going to be published/archived at the end of a project.

### How versioning works?
Each DMP has a [creation date](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_created) and a [modification timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree). The modification date contains a timestamp of the last modification of the DMP. Having two DMPs with different modification dates, one can identify which is newer by comparing timestamps. The same creation date indicates that we consider different versions of the same DMP. 

The standard itself does not have any mechanisms to model different versions of data - if information is overwritten, then previous information is not kept in the model. Systems processing DMPs must have suitable versioning mechanisms, if needed. For example, each update to a DMP can be committed to GitHub. Thus, GitHub allows to retrieve different versions of a DMP over time, while the DMP itself contains the modification date allowing to identify/distinguish/refer to a specific DMP versions. The modification date must be set automatically by a tool that modified the DMP.

### How to express something is planned?
We use dates to indicate planned actions. DMP has a [modification timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree) that contains a timestamp of the last DMP modification. Dataset contains [issue](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dataset_issued) date that indicates whether the actions are planned or already performed:
- if the issue date is set in the future (compared to DMP modification date), then the actions are planned,
- if the issue date is set in the past (compared to DMP modification date), the actions were performed.

See also [example 2](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex2-dataset-planned.json).

### How to indicate actions that were performed?
In a similar way as for the actions that were planned. We use DMP [modification timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree) and [issue date](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dataset_issued) of a dataset. If the issue date is set in the future (compared to DMP modification timestamp), then the actions are planned. If the issue date is set in the past (compared to DMP modification date), the actions were performed.

See also [example 3](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex3-dataset-finished.json).

### How to express embargoes?
Embargo for data sharing means that data will be made available using a license, but not immediately after deposition of data in a repository. 

For each [distribution](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#distribution_table), one can assign a [license](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#license_table). If the license is assigned, then it means that a distribution at some point will become available. [Start date](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#license_start_date) set for the license indicates from when on it becomes binding - in other words, when the distribution becomes available under this license.

[Example 4](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex4-dataset-embargo.json) shows a situation in which dataset will be created on 2019-06-30 (planned) - see Dataset issue date. However, the dataset will become available on 2021-06-30 - see license start date.



### Why Metadata is referenced from a Dataset?
Standard assumes that one can define what metadata standards will be used, once he/she knows what data will be used. 
If a DMP contains only one Dataset and one or more Metadata elements assigned to it, then this expresses in a generic way what metadata standards will be used in a project. However, if more datasets are instantiated and metadata is attributed to one of them, then this denotes that the specific metadata standard will be used for the specific dataset. 

### Are there any other serialisations planned different than JSON?
All the examples provided so far are in JSON, because of its popularity. The standard can be serialised to any other representation, e.g. XML, OWL, JSON-LD, etc. if needed. If you're interested in it, please contact us.

### Is there a JSON schema?
Yes, you can find it [here](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/master/examples/JSON/JSON-schema)

