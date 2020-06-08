# DCSO Core

The DCSO Core represents the core elements of the DCSO. It includes terms that from the [W3C DCAT Specification](https://www.w3.org/ns/dcat), [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), and [FOAF Vocabulary Specification 0.99](http://xmlns.com/foaf/spec/).

```bash
├── dcso:Cost
├── dcso:DMP
├── dcso:Funding
├── dcso:Host
├── dcso:Licence
├── dcso:Metadata
├── dcso:Project
├── dcso:SecurityPrivacy
├── dcso:TechnicalResource
├── dcso:Id
│   ├── dcso:ContactId
│   ├── dcso:ContributorId
│   ├── dcso:DatasetId
│   ├── dcso:DMPId
│   ├── dcso:FunderId
│   ├── dcso:GrantId
│   └── dcso:MetadataStandardId
├── dcat:Dataset
│   └── dcso:Dataset
├── dcat:Distribution
│   └── dcso:Distribution
├── dcsx:Country
├── dcsx:CurrencyCode
├── dcsx:Language
└── foaf:Agent
    ├── dcso:Contact
    └── dcso:Contributor
```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

Versions available:

* v1.0.0 [2019.05.09] - Initial release, modelling the [DMP Common Standard model 2019.03.25](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/blob/master/docs/diagrams/RDA-DMP-Common-Model-Diagram-190325.pdf).
* v1.1.1 [2019.09.12] - Fixed some consistency issues. Added cross references to the foaf, dcat and dct data properties.
* v1.1.2 [2019.09.19] - Added the hostID object property, that now allows Host entities to be identified through TypeIdentifier entities.
* v2.0.0 [2020.04.22] - Compliant with the published version of the RDA's DMP Common Standard. Namespaces fixed to allow for URL opening.
* v2.0.1 [2020.05.01] - Corrected the lack of certain datatype entity associations.
* v2.0.2 [2020.05.07] - Corrected the hasFunder_id object property, and changed the namespace to be compliant with the w3id.
* v3.0.0 [2020.05.28] - RDA Hackathon version. Imported third party ontologies into the dcso.
* v3.0.1 [2020.05.28] - RDA Hackathon version. All properties have been annotated.
* v3.0.2 [2020.05.28] - RDA Hackathon final version.
