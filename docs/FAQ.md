<h1> Frequently Asked Questions </h1>


Index:
* [When to use the model?](#when-to-use-the-model)
* [How versioning works?](#how-versioning-works)
* [How to express something is planned?](#how-to-express-something-is-planned)
* How to indicate actions that were performed?
* How to model embargoes?
* Do I have to list all datasets?
* Why Metadata is referenced from a Dataset?
* What is a difference between Dataset and a Distribution?
* [How do you know it is the same dataset first stored here and then archived?](#how-do-you-know-it-is-the-same-dataset-first-stored-here-and-then-archived)

* [Are there any other serialisations planned different than JSON?](#are-there-any-other-serialisations-planned-different-tham-json)

* [Is there a JSON Schema?](#is-there-a-json-schema)

* [Is there a model validator?](#is-there-a-model-validator)

### When to use the model?

### How versioning works?
Each DMP has a [creation date](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_created) and a [modification timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree). The modification date contains a timestamp of the last modification of the DMP. Having two DMPs with different modification dates, one can identify which is newer by comparing timestamps. The same creation date indicates that we consider different versions of the same DMP. 

The model itself does not have any mechanisms to model different versions of data - if information is overwritten, then previous information is not kept in the model. Systems processing DMPs must have suitable versioning mechanisms, if needed. For example, each update to a DMP can be commited to GitHub. Thus, GitHub allows to retrieve different versions of a DMP over time, while the DMP itself contains the modification date allowing to identify/distinguish/refer to a specifc DMP versions. The modification date must be set automatically by a tool that modified the DMP.

### How to express something is planned?
We use dates to indicate planned actions. DMP has a [modificiation timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree) that contains a timestamp of the last DMP modification. Dataset contains [issue](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dataset_issued) date that indicates whether the actions are planned or already performed:
- if the issue date is set in the future (compared to DMP modification date), then the actions are planned,
- if the issue date is set in the past (compared to DMP modification date), the the actions were performed.

See also [example 2](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex2-dataset-planned.json).

### How to indicate actions that were performed?
In a similar way as for the actions that were planned. We use DMP [modificiation timestamp](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dmp_modified_tree) and [issue date] (https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#dataset_issued) of a dataset. If the issue date is set in the future (compared to DMP modification timestamp), then the actions are planned. If the issue date is set in the past (compared to DMP modification date), the the actions were performed.

See also [example 3](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex3-dataset-finished.json).


### How to model embargoes?
Embargo for data sharing means that data will be made available using a license, but not immediately after deposition of data in a repository. 

For each [distribution](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#distribution_table), one can assign a [license](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#license_table). If the license is assigned, then it means that a distribution at some point will become available. [Start date](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/index.md#license_start_date) set for the license indicates from when on it becomes binding - in other words, when the distribution becomes available under this license.

[Example 4](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/examples/JSON/ex4-dataset-embargo.json) shows a situation in which dataset will be created on 2019-06-30 (planned) - see Dataset issue date. However, the dataset will become available on 2021-06-30 - see license start date.

### Do I have to list all datasets?

### Why Metadata is referenced from a Dataset?

### What is a difference between Dataset and a Distribution?

### How do you know it is the same dataset first stored here and then archived?

### Are there any other serialisations planned different than JSON?
Yes, depending on the demand. The common model can be serialised to XML, OWL, JSON-LD, etc. if needed. If you're interested in it, please contact us.

### Is there a JSON Schema?
It is planned. Comming soon.

### Is there a model validator?
Apart from the JSON schema that validates the model instances syntactically. We're planning a tool that would check it semantically, e.g. whether fields requiring terms from controlled vocabularies are field with those and not arbitrary strings.
