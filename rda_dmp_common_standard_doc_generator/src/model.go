package main

import (
	"github.com/goki/ki/ki"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

var properties []*Property
var rootProperty *Property

type EntityDescription struct {
	ID          int    `gorm:"AUTO_INCREMENT"`
	Title       string `csv:"title"`
	Description string `csv:"description"`
}

type Property struct {
	ki.Node      `gorm:"-"`
	ID           string     `gorm:"primary_key" csv:"id"`
	ParentId     string     `csv:"parent_property"`
	LabelMachine string     `csv:"label_machine"`
	LabelHuman   string     `csv:"label_human"`
	Description  string     `csv:"description"`
	Uri          string     `csv:"uri"`
	ExampleValue string     `csv:"example_value"`
	Notes        string     `csv:"notes"`
	Cardinality  string     `csv:"cardinality"`
	VocabularyID string     `csv:"vocabulary"`
	Vocabulary   Vocabulary `gorm:"foreignkey:VocabularyID"`
	DataTypeID   string     `csv:"data_type"`
	DataType     DataType   `gorm:"foreignkey:DataTypeID"`
}

type Value struct {
	ID           string     `gorm:"primary_key" csv:"id"`
	Label        string     `csv:"label"`
	Uri          string     `csv:"uri"`
	Notes        string     `csv:"notes"`
	ListOrder    int        `csv:"list_order"`
	VocabularyID string     `csv:"vocabulary"`
	Vocabulary   Vocabulary `gorm:"foreignkey:VocabularyID"`
	PropertyID   string     `csv:"property"`
	Property     Property   `gorm:"foreignkey:PropertyID"`
}

type Vocabulary struct {
	ID         string `gorm:"primary_key" csv:"id"`
	Label      string `csv:"label"`
	Uri        string `csv:"uri"`
	Notes      string `csv:"notes"`
	Type       string `csv:"vocab_type"`
	Properties []Property
}

type DataType struct {
	ID         string `gorm:"primary_key" csv:"id"`
	Label      string `csv:"label"`
	Notes      string `csv:"notes"`
	Properties []Property
}

func findPropertyById(id string) *Property {
	for _, v := range properties {
		if v.ID == id {
			return v
		}
	}
	return nil
}
