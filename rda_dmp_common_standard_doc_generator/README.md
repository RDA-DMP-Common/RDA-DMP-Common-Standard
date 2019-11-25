# RDA DMP Common Standard Documentation Generator

A utility, written in `Go`, for generating the Web documentation of the RDA DMP Common Standard. This utility uses the sources held in a set of [5 Google Spreadsheets](https://docs.google.com/spreadsheets/u/1/d/1UatNC3r3skKjy2vGK1sysk6vKGD1F9v8YgdinyGMx7U/edit#gid=1487393314) which are "published" in `CSV` format at the URLs listed in the config file: [config.yaml](config.yaml), and creates the resulting documentation as a file called "README.md" which is, by default, written into the `output` folder.

Written by Paul Walk (paul@paulwalk.net)

## Prerequisites

1. A working [Go](https://golang.org) environment (with `GOPATH` environment variable set correctly)
2. This Github repository, checked out into a working copy

## Instructions to compile and run this utility

### 1. Download required packages
```bash
go get -u github.com/sirupsen/logrus
go get -u gopkg.in/yaml.v3
go get -u github.com/gocarina/gocsv
go get -u github.com/jinzhu/gorm
go get -u github.com/goki/ki/ki
```

### 2. Compile the sources

From a command line, change into the `src` sub-directory and run:

```bash
go build -o ../rda_dmp_common_standard_doc_generator
```

This will build an executable file called `rda_dmp_common_standard_doc_generator` in the main directory (the one containing this `README.md` file)

### 3. Set up your configuration file

This utility uses a [single configuration file](config.yaml) for all of it's configuration (i.e. it takes no arguments). The configuration file must exist in the same directory as the executable. In most circumstances, you should be able to use the configuration file provided in this repository.

### 4. Run the utility

```bash
./rda_dmp_common_standard_doc_generator
```

This should create two new files, both in the `output` folder:

1. `db.sqlite`
2. `README.md`

Anytime you want to 'refresh' the local documentation file from the Google Spreadsheet sources, simply delete the `db.sqlite` file from the `output` folder, and re-run the utility. This will rebuild the database from the Google Spreadsheet data, and then rebuild the documentation file (`README.md`)in the `output` folder.


### 5. Publish the new documentation
Simply copy or move the `README.md` file from the `output` folder to the top level folder of this Github repository (replacing the one that is there).