package main

import (
	"2ndTask/utils"
	"flag"
	"fmt"
	"log"
	"os"
)

func parseHashFromFile(repo string) string {
	result, _ := os.ReadFile(repo)
	return string(result)
}

func saveHashToFile(content, path string) error {
	return os.WriteFile(path, []byte(content), 0644)
}

func main() {
	repoPath := flag.String("repo", "", "Path to the Git repository")
	outputPath := flag.String("output", "", "Path to the result file")
	filePath := flag.String("file", "", "Hash of the file to track")
	flag.Parse()

	targetHash := parseHashFromFile(*filePath)
	fmt.Println(targetHash)

	if *repoPath == "" || *outputPath == "" || *filePath == "" {
		fmt.Println("Флаги пустые")
		return
	}

	grapgMaker := utils.GraphMake{}

	err := grapgMaker.GetCommits(*repoPath)
	if err != nil {
		log.Fatal(err)
	}

	targetFile, err := grapgMaker.GetNameOfFileByHisHash(targetHash, *repoPath)
	if err != nil {
		log.Fatal(err)
	}

	filteredCommits, err := grapgMaker.FilterCommitsByFileHash(targetFile, targetHash, *repoPath)
	if err != nil {
		log.Fatal(err)
	}

	if len(filteredCommits) == 0 {
		fmt.Println("Не найдено коммитов с заданным хэш-значением файла.")
		return
	}

	graph, err := grapgMaker.BuildDependencyGraph(filteredCommits, *repoPath)
	if err != nil {
		fmt.Println("Ошибка при построении графа зависимостей:", err)
		os.Exit(1)
	}

	mermaidCode := grapgMaker.GenerateMermaid(graph)

	err = saveHashToFile(mermaidCode, *outputPath)
	if err != nil {
		fmt.Println("Ошибка при сохранении файла:", err)
		os.Exit(1)
	}

	fmt.Println("Граф зависимостей успешно сохранён в", *outputPath)
}
