package utils

import (
	"reflect"
	"testing"
)

func TestGraphMake_BuildDependencyGraph(t *testing.T) {
	tests := []struct {
		name            string
		filteredCommits []string
		repoPath        string
		want            map[string][]string
		wantErr         bool
	}{
		{
			name:            "Empty commit list",
			filteredCommits: []string{},
			repoPath:        "/path/to/repo",
			want:            map[string][]string{},
			wantErr:         false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{}
			got, err := g.BuildDependencyGraph(tt.filteredCommits, tt.repoPath)
			if (err != nil) != tt.wantErr {
				t.Errorf("BuildDependencyGraph() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("BuildDependencyGraph() got = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGraphMake_BulidGraph(t *testing.T) {
	tests := []struct {
		name    string
		commits []string
		want    string
	}{
		{
			name:    "Simple linear history",
			commits: []string{"commit1", "commit2", "commit3"},
			want:    "graph TD\ncommit1 --> commit2\ncommit2 --> commit3\n",
		},
		{
			name:    "Empty commit list",
			commits: []string{},
			want:    "graph TD\n",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{
				commits: tt.commits,
			}
			if got := g.BulidGraph(); got != tt.want {
				t.Errorf("BulidGraph() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGraphMake_FilterCommitsByFileHash(t *testing.T) {
	tests := []struct {
		name           string
		commits        []string
		filePath       string
		targetFileHash string
		repoPath       string
		want           []string
		wantErr        bool
	}{
		{
			name:           "Valid commits",
			commits:        []string{"commit1", "commit2"},
			filePath:       "file.txt",
			targetFileHash: "abc123",
			repoPath:       "/path/to/repo",
			want:           nil,
			wantErr:        false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{
				commits: tt.commits,
			}
			got, err := g.FilterCommitsByFileHash(tt.filePath, tt.targetFileHash, tt.repoPath)
			if (err != nil) != tt.wantErr {
				t.Errorf("FilterCommitsByFileHash() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FilterCommitsByFileHash() got = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGraphMake_GenerateMermaid(t *testing.T) {
	tests := []struct {
		name  string
		graph map[string][]string
		want  string
	}{
		{
			name: "Simple graph",
			graph: map[string][]string{
				"commit2": {"commit1"},
			},
			want: "graph TD\n    commit1 --> commit2\n",
		},
		{
			name:  "Empty graph",
			graph: map[string][]string{},
			want:  "graph TD\n",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{}
			if got := g.GenerateMermaid(tt.graph); got != tt.want {
				t.Errorf("GenerateMermaid() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGraphMake_GetCommits(t *testing.T) {
	tests := []struct {
		name     string
		repoPath string
		wantErr  bool
	}{
		{
			name:     "Invalid repo",
			repoPath: "/invalid/path",
			wantErr:  true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{}
			if err := g.GetCommits(tt.repoPath); (err != nil) != tt.wantErr {
				t.Errorf("GetCommits() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestGraphMake_GetFileHashInCommit(t *testing.T) {
	tests := []struct {
		name     string
		commit   string
		filePath string
		repoPath string
		want     string
		wantErr  bool
	}{
		{
			name:     "File not in commit",
			commit:   "commit1",
			filePath: "nonexistent.txt",
			repoPath: "/path/to/repo",
			want:     "",
			wantErr:  true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			g := &GraphMake{}
			got, err := g.GetFileHashInCommit(tt.commit, tt.filePath, tt.repoPath)
			if (err != nil) != tt.wantErr {
				t.Errorf("GetFileHashInCommit() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("GetFileHashInCommit() got = %v, want %v", got, tt.want)
			}
		})
	}
}
