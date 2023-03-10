package main

import (
	"github.com/gocarina/gocsv"
	"github.com/jinzhu/gorm"
	"io/ioutil"
	"net/http"
)

func getCsvFromGoogleSheet(url string) ([]byte, error) {
	var bytes []byte
	resp, err := http.Get(url)
	if err != nil {
		return bytes, err
	}
	defer resp.Body.Close()
	bytes, err = ioutil.ReadAll(resp.Body)
	if err != nil {
		return bytes, err
	}
	return bytes, err
}

func populateDbFromGoogleSheets(db *gorm.DB, googleSheets map[string]string) error {
	var err error
	for modelName, url := range googleSheets {
		err = populateTableFromGoogleSheets(db, modelName, url)
	}
	return err
}

func populateTableFromGoogleSheets(db *gorm.DB, modelName string, url string) error {
	bytes, err := getCsvFromGoogleSheet(url)
	if err != nil {
		return err
	}
	switch modelName {
	case "Property":
		err = populatePropertiesFromCsv(db, bytes)
	case "Value":
		err = populateValuesFromCsv(db, bytes)
	case "Vocabulary":
		err = populateVocabulariesFromCsv(db, bytes)
	case "DataType":
		err = populateDataTypesFromCsv(db, bytes)
	case "EntityDescription":
		err = populateEntityDescriptionsFromCsv(db, bytes)
	}
	return err
}

func populatePropertiesFromCsv(db *gorm.DB, bytes []byte) error {
	var records []*Property
	err := gocsv.UnmarshalBytes(bytes, &records)
	if err == nil {
		for _, record := range records {
			db.Create(&record)
		}
	}
	return err
}

func populateValuesFromCsv(db *gorm.DB, bytes []byte) error {
	var records []*Value
	err := gocsv.UnmarshalBytes(bytes, &records)
	if err == nil {
		for _, record := range records {
			db.Create(&record)
		}
	}
	return err
}

func populateVocabulariesFromCsv(db *gorm.DB, bytes []byte) error {
	var records []*Vocabulary
	err := gocsv.UnmarshalBytes(bytes, &records)
	if err == nil {
		for _, record := range records {
			db.Create(&record)
		}
	}
	return err
}

func populateDataTypesFromCsv(db *gorm.DB, bytes []byte) error {
	var records []*DataType
	err := gocsv.UnmarshalBytes(bytes, &records)
	if err == nil {
		for _, record := range records {
			db.Create(&record)
		}
	}
	return err
}

func populateEntityDescriptionsFromCsv(db *gorm.DB, bytes []byte) error {
	var records []*EntityDescription
	err := gocsv.UnmarshalBytes(bytes, &records)
	if err == nil {
		for _, record := range records {
			db.Create(&record)
		}
	}
	return err
}
