# DCSO Extensions - DCSX

The DCSO extensions (DCSX) aim to be a support to the DCSO core. The objective is to collect into a single ontology the controlled vocabularies that are in use in the DMP Common Standard.

The controlled vocabularies that are represented are:

* dcs-lang - [ISO 639-3](http://www.sil.org/iso639-3/)
* dcs-geo  - [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)
* dcs-cur  - [ISO 4217](http://www.currency-iso.org/en/home/tables/table-a1.html)

The structure of the elements is:

```bash
├── dcsx:Country
├── dcsx:CurrencyCode
└── dcsx:Language
```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

Versions available:

* dcsx.1.0.0 [2020.05.28] - Created all individuals.
* dcsx.1.0.1 [2020.05.28] - RDA Hackathon final version. Changed the identifiers and namespaces.
