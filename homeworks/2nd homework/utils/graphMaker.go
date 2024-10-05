package utils

import (
	"fmt"
	"os/exec"
	"strings"
)

type GraphMake struct {
	commits []string
}

func (g *GraphMake) GetCommits(repoPath string) error {
	cmd := exec.Command("git", "-C", repoPath, "rev-list", "--all")
	output, err := cmd.Output()
	if err != nil {
		return err
	}
	commits := strings.Split(strings.TrimSpace(string(output)), "\n")
	g.commits = commits
	return nil
}

func (g *GraphMake) GetNameOfFileByHisHash(target, repoPath string) (string, error) {
	cmd := exec.Command("git", "-C", repoPath, "ls-tree", "-r", "HEAD")
	outputs, err := cmd.Output()
	if err != nil {
		return "", err
	}
	part := strings.Split(strings.TrimSpace(string(outputs)), "\n")
	for _, output := range part {
		parts := strings.Fields(output)
		if parts[2] == target {
			return parts[3], nil
		}
	}
	return "", nil
}

func (g *GraphMake) GetFileHashInCommit(commit, filePath, repoPath string) (string, error) {
	cmd := exec.Command("git", "-C", repoPath, "ls-tree", commit, filePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	parts := strings.Split(string(output), " ")
	if len(parts) < 3 {
		return "", fmt.Errorf("unexpected ls-tree output: %s", output)
	}
	return strings.TrimSpace(parts[2]), nil
}

func (g *GraphMake) FilterCommitsByFileHash(filePath, targetFileHash, repoPath string) ([]string, error) {
	var filteredCommits []string
	for _, commit := range g.commits {
		fileHash, err := g.GetFileHashInCommit(commit, filePath, repoPath)
		if err != nil {
			continue
		}
		if fileHash != "" {
			filteredCommits = append(filteredCommits, commit)
		}
	}
	return filteredCommits, nil
}

func (g *GraphMake) GetParentCommits(commit, repoPath string) ([]string, error) {
	cmd := exec.Command("git", "-C", repoPath, "rev-list", "--parents", "-n", "1", commit)
	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}
	parts := strings.Split(strings.TrimSpace(string(output)), " ")
	if len(parts) < 2 {
		return []string{}, nil
	}
	return parts[1:], nil
}

func (g *GraphMake) BulidGraph() string {
	var graph strings.Builder
	graph.WriteString("graph TD\n")
	for i := 0; i < len(g.commits)-1; i++ {
		graph.WriteString(g.commits[i] + " --> " + g.commits[i+1] + "\n")
	}
	return graph.String()
}

func (g *GraphMake) BuildDependencyGraph(filteredCommits []string, repoPath string) (map[string][]string, error) {
	graph := make(map[string][]string)
	commitSet := make(map[string]bool)
	for _, commit := range filteredCommits {
		commitSet[commit] = true
	}

	for _, commit := range filteredCommits {
		parents, err := g.GetParentCommits(commit, repoPath)
		if err != nil {
			return nil, err
		}
		for _, parent := range parents {
			if commitSet[parent] {
				graph[commit] = append(graph[commit], parent)
			}
		}
	}
	return graph, nil
}

func (g *GraphMake) GenerateMermaid(graph map[string][]string) string {
	var mermaid strings.Builder
	mermaid.WriteString("graph TD\n")
	for child, parents := range graph {
		for _, parent := range parents {
			mermaid.WriteString(fmt.Sprintf("    %s --> %s\n", parent, child))
		}
	}
	return mermaid.String()
}
