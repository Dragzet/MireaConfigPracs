.PHONY: run tests

run:
	go run main.go -repo=mux -output=files/output.md -file=files/input.txt
tests:
	cd utils && go test

.DEFAULT_GOAL := run