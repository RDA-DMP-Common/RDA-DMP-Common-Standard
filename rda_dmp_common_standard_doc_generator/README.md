# RDA DMP Common Standard Documentation Generator

A utility, written in `Go`, for generating the Web documentation of the GCWG-RDA maDMP Standard. This utility uses the sources held in a set of [5 Google Spreadsheets](https://docs.google.com/spreadsheets/d/e/2PACX-1vTLLFvV7jnRCAdef34_JgN6py7GPNQGZkizXr6dEUW-X2oEA_AZQXLjrQxHcHZZsIMWQCS3mqOPxlKx/pub?gid=750759343#) which are "published" in `CSV` format at the URLs listed in the config file: [config.yaml](config.yaml), and creates the resulting documentation as a file called "README.md" which is, by default, written into the `output` folder.

Written by Paul Walk (paul@paulwalk.net)\
Revised by Esther Liu (esther.liu@uwaterloo.ca), Emily Chu (ewchu@uwaterloo.ca)

## Prerequisites

1. A working [Go](https://golang.org) environment (with `GOPATH` environment variable set correctly)
2. This Github repository, checked out into a working copy
3. [GCC compiler 64-bit](https://jmeubank.github.io/tdm-gcc/) installed and found in the path 

## Instructions to compile and run this utility

These instruction work as written for VS Code. If using other editors or the Command Prompt, syntax may need to be slightly modified. 

### 1. Initialize the module and download required packages
```bash
go mod init github.com/FAIRERdata/maDMP-Standard/tree/tests/rda_dmp_common_standard_doc_generator

go get -u github.com/sirupsen/logrus@67a7fdcf741f4d5cee82cb9800994ccfd4393ad0
go get -u gopkg.in/yaml.v3
go get -u github.com/gocarina/gocsv@c6a9c812ac269510ec596e469aff422e694ec6fd
go get -u github.com/jinzhu/gorm
go get -u github.com/goki/ki/ki

go get -u github.com/jinzhu/gorm/dialects/sqlite@v1.9.16
```

### 2. Compile the sources

From a command line, change into the `src` sub-directory and run:

```bash
go build -o ../rda_dmp_common_standard_doc_generator
```

This will build an executable file called `rda_dmp_common_standard_doc_generator` in the main directory (the one containing this `README.md` file). If this does not build an executable file, add the extension `.exe` to the end of the code 
```bash
go build -o ../rda_dmp_common_standard_doc_generator.exe
```

### 3. Set up your configuration file

This utility uses a [single configuration file](config.yaml) for all of it's configuration (i.e. it takes no arguments). The configuration file must exist in the same directory as the executable. In most circumstances, you should be able to use the configuration file provided in this repository.

### 4. Run the utility

Use `cd ..` to go back to `rda_dmp_common_standard_doc_generator` folder and run: 

```bash
./rda_dmp_common_standard_doc_generator
```

This should create two new files, both in the `output` folder:

1. `db.sqlite`
2. `README.md`

Anytime you want to 'refresh' the local documentation file from the Google Spreadsheet sources, simply delete the `db.sqlite` file from the `output` folder, and re-run the utility. This will rebuild the database from the Google Spreadsheet data, and then rebuild the documentation file (`README.md`)in the `output` folder.


### 5. Publish the new documentation
Simply copy or move the `README.md` file from the `output` folder to the top level folder of this Github repository (replacing the one that is there).

## Styling Github Pages Website
After the `README.md` file is uploaded, the [website](https://fairerdata.github.io/maDMP-Standard/) is automatically deployed. 

The current website theme is the Jekyll theme [Cayman](https://github.com/pages-themes/cayman). 

If changes to the default styling of the website need to be made (e.g. changes to the width of tables, font-size, colours, etc.) to better suit the information presented, edit the `SCSS` styling sheet. 

Use the [style.scss](https://github.com/FAIRERdata/maDMP-Standard/blob/Master/assets/css/style.scss) sheet found in this repository path `maDMP-Standard/assets/css`. 
CSS code should be written underneath the comment 

```/* Following is css code to change the default styling of the Jekyll theme */```

Comparing with the default stylings of the Cayman theme [style sheet](https://github.com/pages-themes/cayman/blob/master/_sass/jekyll-theme-cayman.scss) and `style.scss` can determine the corresponding elements which need to be overrided/changed. Using Inspect Element on the website can also determine the corresponding elements to refer to in the CSS code.


