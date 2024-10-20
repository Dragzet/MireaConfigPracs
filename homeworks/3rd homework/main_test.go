package main

import (
	"encoding/xml"
	"testing"
)

func TestParseElement(t *testing.T) {
	input := `<comment>Это комментарий</comment>`
	var elem Element
	xml.Unmarshal([]byte(input), &elem)
	expected := ":: Это комментарий\n"
	result := parseElement(elem, "")
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}

	input = `<array><item>1</item><item>2</item><item>3</item></array>`
	xml.Unmarshal([]byte(input), &elem)
	expected = "[1 2 3]\n"
	result = parseElement(elem, "")
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}
}

func TestParseExpression(t *testing.T) {
	input := `<expression>
		<operator>+</operator>
		<operand>2</operand>
		<operand>3</operand>
	</expression>`
	var elem Element
	xml.Unmarshal([]byte(input), &elem)
	expected := "?( + 2 3 )"
	result := parseExpression(elem)
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}
}

func TestEvaluateExpression(t *testing.T) {
	input := `<expression>
		<operator>+</operator>
		<operand>2</operand>
		<operand>3</operand>
	</expression>`
	var elem Element
	xml.Unmarshal([]byte(input), &elem)
	expected := "5.00"
	_, result := evaluateExpression(elem)
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}
}

func TestParseValue(t *testing.T) {
	value := "42"
	expected := "42"
	result := parseValue(value)
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}

	value = "Hello"
	expected = "Hello"
	result = parseValue(value)
	if result != expected {
		t.Errorf("Ожидалось '%s', но получено '%s'", expected, result)
	}
}

func TestConstantAssignment(t *testing.T) {
	input := `<constant name="pi">3.14</constant>`
	var elem Element
	xml.Unmarshal([]byte(input), &elem)
	parseElement(elem, "")
	expected := 3.14
	result := constants["pi"]
	if result != expected {
		t.Errorf("Ожидалось '%f', но получено '%f'", expected, result)
	}
}
