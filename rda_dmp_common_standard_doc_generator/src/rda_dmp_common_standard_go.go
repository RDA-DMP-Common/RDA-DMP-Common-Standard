package main

import (
	"github.com/jinzhu/gorm"
	"github.com/sirupsen/logrus"
	"os"
	"path/filepath"
)

const defaultConfigFilePath = "config.yaml"

var db *gorm.DB
var config = Config{}

func main() {
	err := (&config).unmarshal(defaultConfigFilePath)
	if err != nil {
		logrus.WithFields(logrus.Fields{"Config File Path": defaultConfigFilePath}).Errorln(err)
		logrus.Fatal("Halting execution")
	} else {
		logrus.Infof("Configured OK with configuration from file: '%s'", defaultConfigFilePath)
	}
	localDatabaseNeedsToBeCreatedAndPopulatedFromGoogle := false
	dbConnectString := filepath.Join(config.OutputFolderPath, "db.sqlite")
	logrus.Infof("Setting database path to: %s", dbConnectString)
	if _, err := os.Stat(dbConnectString); os.IsNotExist(err) {
		localDatabaseNeedsToBeCreatedAndPopulatedFromGoogle = true
	}
	db, err = gorm.Open("sqlite3", dbConnectString)
	if err != nil {
		logrus.WithFields(logrus.Fields{"Database URL": dbConnectString}).Errorln(err)
		logrus.Fatal("Halting execution")
	} else {
		logrus.Info("Connected to database OK")
	}
	defer db.Close()
	if localDatabaseNeedsToBeCreatedAndPopulatedFromGoogle {
		resetDatabase()
		err = populateDbFromGoogleSheets(db, config.GoogleSheets)
		if err != nil {
			logrus.Fatal(err)
		}
	}
	populateProperties()
	setRootProperty()
	generateDoc()

	logrus.Info("Execution completed")

}
