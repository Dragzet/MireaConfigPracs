all: conf1 conf2 tests

conf1:
	@cat "Zconfig1.xml" | go run main.go

conf2:
	@cat "Zconfig2.xml" | go run main.go

tests:
	go test -v