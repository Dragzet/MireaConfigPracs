import unittest
import os
from typing import List, Tuple
from main import *


class TestGitDependencyGraph(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.repo_path = "2ndCourse"
        self.test_commit_hash = "abc123"
        self.test_tree_hash = "def456"
        self.test_blob_hash = "123abc"
        self.test_filename = "app.logs"
        self.test_file_path = "target.txt"

    def test_resolve_head_commit(self):
        """Тест получения HEAD коммита"""
        head_commit = resolve_head_commit(self.repo_path)
        self.assertIsInstance(head_commit, str)
        self.assertEqual(len(head_commit), 40)


    def test_traverse_tree(self):
        """Тест обхода дерева Git"""
        results = traverse_tree(self.repo_path, self.test_tree_hash, self.test_commit_hash)
        self.assertIsInstance(results, list)
        for entry in results:
            self.assertIsInstance(entry, tuple)
            self.assertEqual(len(entry), 3)
            self.assertEqual(entry[2], self.test_commit_hash)

    def test_traverse_commits(self):
        """Тест обхода всех коммитов"""
        commit_tree = traverse_commits(self.repo_path)
        self.assertIsInstance(commit_tree, list)
        for entry in commit_tree:
            self.assertEqual(len(entry), 3)
            self.assertIsInstance(entry[0], str)
            self.assertIsInstance(entry[1], str)
            self.assertIsInstance(entry[2], str)


    def test_get_all_commits(self):
        """Тест получения всех коммитов для файла"""
        commit_tree = traverse_commits(self.repo_path)
        commit_list = get_all_commits(commit_tree, self.test_filename)
        self.assertIsInstance(commit_list, list)
        for commit in commit_list:
            self.assertIsInstance(commit, str)
            self.assertEqual(len(commit), 40)

    def test_buildMermaid(self):
        """Тест создания графа Mermaid"""
        commits = ['abc123', 'def456', '789abc']
        mermaid_code = buildMermaid(commits)
        self.assertIn("graph TD", mermaid_code)
        self.assertIn("abc123 --> def456", mermaid_code)
        self.assertIn("def456 --> 789abc", mermaid_code)

if __name__ == "__main__":
    unittest.main()
