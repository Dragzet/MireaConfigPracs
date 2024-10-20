package main

import (
	"encoding/xml"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Element struct {
	XMLName xml.Name
	Attrs   []xml.Attr `xml:",any,attr"`
	Content []byte     `xml:",chardata"`
	Nodes   []Element  `xml:",any"`
}

var constants = make(map[string]float64)

func parseElement(e Element, indent string) string {
	result := ""

	if e.XMLName.Local == "comment" {
		return indent + ":: " + strings.TrimSpace(string(e.Content)) + "\n"
	}

	if e.XMLName.Local == "array" {
		result += indent + parseArray(e) + "\n"
		return result
	}

	if e.XMLName.Local == "dictionary" {
		result += indent + "{\n"
		for _, node := range e.Nodes {
			result += parseElement(node, indent+"  ")
		}
		result += indent + "}\n"
		return result
	}

	if e.XMLName.Local == "constant" {
		name := ""
		value := ""
		for _, attr := range e.Attrs {
			if attr.Name.Local == "name" {
				name = attr.Value
			}
		}
		value = parseValue(string(e.Content))
		constantValue, _ := strconv.ParseFloat(value, 64)
		constants[name] = constantValue
		result += indent + name + " is " + value + ";\n"
		return result
	}

	if e.XMLName.Local == "expression" {
		expression := parseExpression(e)
		_, evalResult := evaluateExpression(e)
		result += indent + expression + " => " + evalResult + "\n"

		return result
	}

	if len(e.Nodes) == 0 {
		result += indent + e.XMLName.Local + " = " + parseValue(string(e.Content)) + ";\n"
	} else {
		result += indent + e.XMLName.Local + " {\n"
		for _, node := range e.Nodes {
			result += parseElement(node, indent+"  ")
		}
		result += indent + "}\n"
	}
	return result
}

func parseArray(e Element) string {
	values := []string{}
	for _, node := range e.Nodes {
		values = append(values, strings.TrimSpace(string(node.Content)))
	}
	return "[" + strings.Join(values, " ") + "]"
}

func parseExpression(e Element) string {
	operator := ""
	operands := []string{}
	for _, node := range e.Nodes {
		if node.XMLName.Local == "operator" {
			operator = strings.TrimSpace(string(node.Content))
		} else {
			operands = append(operands, strings.TrimSpace(string(node.Content)))
		}
	}
	return "?( " + operator + " " + strings.Join(operands, " ") + " )"
}

func evaluateExpression(e Element) (bool, string) {
	operator := ""
	var operands []float64
	for _, node := range e.Nodes {
		if node.XMLName.Local == "operator" {
			operator = strings.TrimSpace(string(node.Content))
		} else if node.XMLName.Local == "operand" {
			operandStr := strings.TrimSpace(string(node.Content))
			if value, ok := constants[operandStr]; ok {
				operands = append(operands, value) // Если это константа
			} else {
				operand, err := strconv.ParseFloat(operandStr, 64)
				if err != nil {
					return false, "Ошибка: неверный операнд " + operandStr
				}
				operands = append(operands, operand)
			}
		}
	}
	if operator == "+" && len(operands) == 2 {
		return true, fmt.Sprintf("%.2f", operands[0]+operands[1])
	}

	if operator == "print" && len(operands) == 1 {
		return true, fmt.Sprintf("%.2f", operands[0])
	}

	return false, "Неподдерживаемая операция"
}

func parseValue(val string) string {
	val = strings.TrimSpace(val)
	if _, err := strconv.Atoi(val); err == nil {
		return val
	}
	return fmt.Sprintf(val)
}

func main() {
	decoder := xml.NewDecoder(os.Stdin)
	var root Element

	err := decoder.Decode(&root)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Ошибка при чтении XML: %v\n", err)
		os.Exit(1)
	}

	fmt.Println()

	result := parseElement(root, "")
	fmt.Print(result)
}
