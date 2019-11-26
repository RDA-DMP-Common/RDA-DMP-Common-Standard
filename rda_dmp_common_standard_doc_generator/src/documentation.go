package main

import (
	"fmt"
	"github.com/goki/ki/ki"
	"github.com/sirupsen/logrus"
	"os"
	"path/filepath"
)

func generateDoc() {
	content := fmt.Sprintf("<h1>%s</h1>", config.DocTitle)
	content += "<table><tr><td valign=\"top\">"
	var entityDescriptions []EntityDescription
	db.Find(&entityDescriptions)
	for _, ed := range entityDescriptions {
		content += fmt.Sprintf("<h3>%s</h3>\n", ed.Title)
		content += fmt.Sprintf("%s\n\n", ed.Description)
	}
	content += "</td>"
	content += "<td valign=\"top\"><h3>Structure</h3>"
	content += generateHtmlTree()
	content += "</td></tr></table>\n"
	content += "\n<hr/>\n\n"
	for _, property := range properties {
		if property.HasChildren() {
			content += fmt.Sprintf("<h2 id=\"%s_table\">Properties in '%s'</h2>\n\n", property.ID, property.LabelMachine)
			content += generateTable(*property)
			content += "\n\n"
		}
	}
	documentFilePath := filepath.Join(config.OutputFolderPath, "README.md")
	f, err := os.Create(documentFilePath)
	if err != nil {
		logrus.Fatal(err)
	}
	defer f.Close()
	_, err = f.WriteString(content)
	if err != nil {
		logrus.Fatal(err)
	}
	logrus.Infof("Wrote documentation file to : '%s'", documentFilePath)
}

func generateTable(property Property) string {
	columns := [5]string{"Name", "Description", "Data Type", "Cardinality", "Example Value"}
	html := "<table style=\"width: 99%;\"><thead><tr>"
	for _, col := range columns {
		html += fmt.Sprintf("<th>%s</th>", col)
	}
	html += "</tr></thead>"
	html += "<tbody>"
	for _, node := range *property.Children() {
		html += getNodeAsHtmlTableRow(node)
	}
	html += "</tbody></table>"
	return html
}

func getNodeAsHtmlTableRow(node ki.Ki) string {
	property := findPropertyById(node.Name())
	description := property.Description
	var values []Value
	db.Where("property_id = ?", property.ID).Order("list_order asc").Find(&values)
	if len(values) > 0 {
		description += "<br/>Allowed Values:<ul>"
		for _, value := range values {
			description += fmt.Sprintf("<li>%s</li>", value.Label)
		}
		description += "</ul>"
	}
	html := fmt.Sprintf("<tr><td valign=\"top\"><a id=\"%s\" href=\"#%s_tree\">%s</a></td>", node.Name(), node.Name(), property.LabelMachine)
	html += fmt.Sprintf("<td valign=\"top\">%s</td>", processContentForTableCell(description))
	html += fmt.Sprintf("<td valign=\"top\">%s</td>", processContentForTableCell(property.DataType.Label))
	html += fmt.Sprintf("<td valign=\"top\">%s</td>", processContentForTableCell(property.Cardinality))
	html += fmt.Sprintf("<td valign=\"top\">%s</td>", processContentForTableCell(property.ExampleValue))
	html += "</tr>\n"
	return html
}

func processContentForTableCell(content string) string {
	if content == "" {
		return " "
	} else {
		return content
	}
}
