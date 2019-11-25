package main

import (
	"github.com/sirupsen/logrus"
)

func resetDatabase() {
	logrus.Debug("Dropping RDB tables....")
	db.DropTableIfExists(Value{})
	db.DropTableIfExists(Property{})
	db.DropTableIfExists(Vocabulary{})
	db.DropTableIfExists(DataType{})
	db.DropTableIfExists(EntityDescription{})
	logrus.Info("RDB tables dropped OK")

	logrus.Debug("Migrating RDB schema....")
	db.AutoMigrate(&EntityDescription{})
	db.AutoMigrate(&DataType{})
	db.AutoMigrate(&Vocabulary{})
	db.AutoMigrate(&Property{})
	db.AutoMigrate(&Value{})
	logrus.Info("RD reset OK")
}

func setRootProperty() {
	logrus.Debug("Setting root property....")
	for _, p := range properties {
		if p.ParentId == "" {
			rootProperty = p
			break
		}
	}
	logrus.Infof("Root property set to '%s'", rootProperty.ID)
}

func populateProperties() {
	db.Order("label_machine asc").Find(&properties)
	for _, p := range properties {
		p.InitName(p, p.ID)
		for _, child := range properties {
			child.InitName(child, child.ID)
			if child.ParentId == p.ID {
				p.AddChild(child)
			}
		}
		datatype := DataType{ID: p.DataTypeID}
		db.First(&datatype)
		p.DataType = datatype
	}
}
