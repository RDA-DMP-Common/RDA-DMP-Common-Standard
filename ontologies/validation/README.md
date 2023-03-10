# DCSO Validation

We use validation approaches, currently [Shape Expressions (ShEx)](http://shexspec.github.io/primer/) only, to check for data constraints on DMP described with DCSO.

If you want to see it in action, you will need a ShEx validation platform such as [ShEx.io](http://shex.io/webapps/shex.js/doc/shex-simple.html) or [RDFShape](http://rdfshape.weso.es/shExValidate). You will need to copy and paste a ShEx file, for instance [dcso-dmp.3.0.2.shex](./dcso-dmp.3.0.2.shex), and its corresponding example, for instance [./valid-example_dcso.3.0.2.ttl](./valid-example_dcso.3.0.2.ttl). You can play by removing or changing some property values and see whether it is still valid or not. Using the already mentioned ShEx file, and the failing example [./failing-example_dcso.3.0.2.ttl](./failing-example_dcso.3.0.2.ttl), you should get an error message regarding the value used for the property _ethicalIssuesExist_.

## Versioning

We use [SemVer](http://semver.org/) for versioning. However, in order to make the correlation between DCSO and its validation easier, our validation file versioning does not evolve on its own. Rather, it takes the same version of the DCSO it is validating. For instance, the DCSO vr. 3.0.2 is validated via dcso-dmp.3.0.2.shex. 

Versions available:
* [dcso-dmp.3.0.2.shex](./dcso-dmp.3.0.2.shex): Validation for DMPs exluding Dataset class and those directly related to it, a validating example is provided at [./valid-example_dcso.3.0.2.ttl](./valid-example_dcso.3.0.2.ttl), a failing example is provided at [./failing-example_dcso.3.0.2.ttl](./failing-example_dcso.3.0.2.ttl)
* Soon to come dcso-dataset.3.0.2.shex: Validation for DMP associated datasets

## Examples

We use [Shaclex/RDFShape](http://shaclex.herokuapp.com/shExValidate) as validation service. If you experience any trouble with the validation, please try again later as the server might be busy.
* A [DMP valid example](./valid-example_dcso.3.0.2.ttl) validated against the [DMP shape](dcso-dmp.3.0.2.shex), available at https://tinyurl.com/dcso-shex-valid
* A [DMP failing example](./failing-example_dcso.3.0.2.ttl) validated against the [DMP shape](dcso-dmp.3.0.2.shex), available at https://tinyurl.com/dcso-shex-failing
* A [Dataset valid example](./valid-dataset-example_dcso.3.0.2.ttl) validated against the [Dataset shape](dcso-dataset.3.0.2.shex), available at https://tinyurl.com/dcso-shex-dataset-valid
* A [Dataset failing example](./failing-dataset-example_dcso.3.0.2.ttl) validated against the [Dataset shape](dcso-dataset.3.0.2.shex), available at https://tinyurl.com/dcso-shex-dataset-failing

## Work in progress
* Getting a permalink on the validation platforms so people can go directly to the validation without needing to copy & paste
* Adding the validation for DCSO dataset
* Adding some restrictions regarding lower/uppercase, language, currency and dates
