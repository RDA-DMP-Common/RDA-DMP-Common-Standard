package main

import (
	"fmt"
	"github.com/goki/ki/ki"
	"github.com/sirupsen/logrus"
)

func generateHtmlTree() string {
	logrus.Debugf("Generating tree")
	html := "<ul>"
	treeDepth := 0
	finalNodeDepth := 0
	var treeFunction ki.Func
	treeFunction = func(k ki.Ki, level int, data interface{}) bool {
		var property = Property{ID: k.Name()}
		db.First(&property)
		finalNodeDepth = level
		if level > treeDepth {
			html += "<ul>"
		} else if level < treeDepth {
			stepsBack := treeDepth - level
			for i := 1; i <= stepsBack; i++ {
				html += "</ul>"
			}
		}
		treeDepth = level
		if k.HasChildren() {
			html += fmt.Sprintf("<li id=\"%s_tree\"><a href=\"#%s_table\">%s</a></li>", k.Name(), k.Name(), property.LabelMachine)
			//html+= fmt.Sprintf("<li>%s %s %s</li>",k.Name(),strconv.Itoa(level),strconv.Itoa(treeDepth))
		} else {
			html += fmt.Sprintf("<li id=\"%s_tree\"><a href=\"#%s\">%s</a></li>", k.Name(), k.Name(), property.LabelMachine)
			//html+= fmt.Sprintf("<li>%s %s %s</li>",k.Name(),strconv.Itoa(level),strconv.Itoa(treeDepth))
		}
		return true
	}
	rootProperty.FuncDownMeFirst(treeDepth, rootProperty, treeFunction)
	for i := 0; i <= finalNodeDepth; i++ {
		html += "</ul>"
	}
	return html
}

//
//func generateHtmlTree_OLD() string {
//	htmlTree := "<ul>"
//	treeDepth := 0
//	finalNodeDepth := 0
//	var treeFunction ki.Func
//	treeFunction = func(k ki.Ki,level int, data interface{}) bool {
//		logrus.Debugf("Processing node %s",k.Name())
//		for _,childNode := range *k.Children() {
//			var property = Property{ID: childNode.Name()}
//			db.First(&property)
//			finalNodeDepth = childNode.Depth()
//			if childNode.Depth() > treeDepth {
//				htmlTree += "<ul>"
//			} else if childNode.Depth() < treeDepth {
//				stepsBack := treeDepth - childNode.Depth()
//				for i:= 1; i<= stepsBack; i++ {
//					htmlTree += "</ul>"
//				}
//			}
//			treeDepth = childNode.Depth()
//			if childNode.HasChildren() {
//				htmlTree += fmt.Sprintf("<li id=\"%s_tree\"><a href=\"#%s_table\">%s</a></li>",childNode.Name(),childNode.Name(),property.LabelMachine)
//			} else {
//				htmlTree += fmt.Sprintf("<li id=\"%s_tree\"><a href=\"#%s\">%s</a></li>",childNode.Name(),childNode.Name(),property.LabelMachine)
//			}
//		}
//		for i:=0; i <= finalNodeDepth; i++ {
//			htmlTree += "</ul>"
//		}
//		return k.HasChildren()
//	}
//	rootProperty.FuncDownMeFirst(0,rootProperty,treeFunction)
//	return htmlTree
//}
