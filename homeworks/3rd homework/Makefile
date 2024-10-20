all: conf1 conf2 tests

conf1:
	@type "Zconfig1.xml" | go run main.go

conf2:
	@type "Zconfig2.xml" | go run main.go

tests:
	go test -v