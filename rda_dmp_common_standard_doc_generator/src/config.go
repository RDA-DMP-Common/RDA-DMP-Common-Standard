package main

import (
	"github.com/sirupsen/logrus"
	"gopkg.in/yaml.v3"
	"io/ioutil"
	"os"
)

func init() {
	logrus.SetFormatter(&logrus.TextFormatter{
		ForceColors:            false,
		DisableColors:          false,
		DisableTimestamp:       true,
		FullTimestamp:          false,
		TimestampFormat:        "",
		DisableSorting:         false,
		QuoteEmptyFields:       false,
		DisableLevelTruncation: true,
	})
	// Output to stdout instead of the default stderr
	logrus.SetOutput(os.Stdout)
}

type Config struct {
	DebugMode        bool              `yaml:"-"`
	DocTitle         string            `yaml:"document_title"`
	DocFooter        string            `yaml:"document_footer"`
	OutputFolderPath string            `yaml:"output_folder_path"`
	GoogleSheets     map[string]string `yaml:"google_sheets_csv_urls"`
}

func (config *Config) unmarshal(filePath string) error {
	config.DebugMode = false
	config.GoogleSheets = make(map[string]string)
	configData, err := ioutil.ReadFile(filePath)
	if err != nil {
		return err
	}
	err = yaml.Unmarshal([]byte(configData), config)
	if err != nil {
		return err
	}
	switch config.DebugMode {
	case true:
		logrus.SetLevel(logrus.DebugLevel)
		logrus.Info("Setting log level to 'DEBUG'")
	default:
		logrus.SetLevel(logrus.InfoLevel)
	}
	return err
}
