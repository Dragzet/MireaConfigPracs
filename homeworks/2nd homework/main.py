import os
import sys
import zlib
from typing import List, Tuple, Optional

def parse_tree(data: bytes) -> List[Tuple[str, str, str]]:
    """Парсит объект типа tree и возвращает список записей в формате (mode, имя файла, хэш объекта)."""
    entries = []
    index = 0
    while index < len(data):
        mode_end = data.index(b' ', index)
        mode = data[index:mode_end].decode('utf-8')
        index = mode_end + 1

        name_end = data.index(b'\x00', index)
        filename = data[index:name_end].decode('utf-8')
        index = name_end + 1

        object_hash = data[index:index + 20].hex()
        index += 20

        entries.append((mode, filename, object_hash))
    return entries

def read_git_object(repo_path: str, object_hash: str) -> Tuple[Optional[str], Optional[bytes]]:
    """Читает объект Git и возвращает его тип и содержимое."""
    object_path = os.path.join(repo_path, '.git', 'objects', object_hash[:2], object_hash[2:])

    try:
        with open(object_path, 'rb') as f:
            compressed_contents = f.read()
            decompressed_contents = zlib.decompress(compressed_contents)

            header, data = decompressed_contents.split(b'\x00', 1)
            obj_type = header.split(b' ')[0].decode('utf-8')
            return obj_type, data
    except FileNotFoundError:
        return None, None
    except Exception as e:
        print(f"Error reading object {object_hash}: {e}")
        return None, None

def get_commit_parents(commit_data: str) -> List[str]:
    """Извлекает родительские коммиты из данных коммита."""
    parents = []
    for line in commit_data.splitlines():
        if line.startswith("parent "):
            parents.append(line.split(" ")[1])
    return parents

def traverse_tree(repo_path: str, tree_hash: str, commit_hash: str, path: str = "") -> List[Tuple[str, str, str]]:
    """Рекурсивно обходит дерево и возвращает записи в формате (filename, blob_hash, commit_hash)."""
    results = []
    obj_type, tree_data = read_git_object(repo_path, tree_hash)
    if obj_type != 'tree':
        return results

    for mode, filename, object_hash in parse_tree(tree_data):
        full_path = os.path.join(path, filename)
        if mode == '40000':  # Подкаталог (другое дерево)
            results.extend(traverse_tree(repo_path, object_hash, commit_hash, full_path))
        elif mode == '100644':  # Файл (blob)
            results.append((full_path, object_hash, commit_hash))
    return results


def resolve_head_commit(repo_path: str) -> str:
    """Разрешает HEAD до хэша последнего коммита."""
    head_path = os.path.join(repo_path, '.git', 'HEAD')
    with open(head_path, 'r') as f:
        ref = f.readline().strip()

        if ref.startswith('ref:'):
            ref_path = os.path.join(repo_path, '.git', *ref.split()[1].split('/'))
            with open(ref_path, 'r') as ref_file:
                commit_hash = ref_file.readline().strip()
        else:
            commit_hash = ref
    return commit_hash


def traverse_commits(repo_path: str) -> List[Tuple[str, str, str]]:
    """Проходит по всем коммитам в репозитории и возвращает список [файл, хэш, коммит]."""
    all_files = []
    visited_commits = set()
    stack = [resolve_head_commit(repo_path)]

    while stack:
        commit_hash = stack.pop()
        if commit_hash in visited_commits:
            continue
        visited_commits.add(commit_hash)

        obj_type, commit_data = read_git_object(repo_path, commit_hash)
        if obj_type != 'commit':
            continue

        tree_hash = None
        for line in commit_data.decode('utf-8').splitlines():
            if line.startswith("tree "):
                tree_hash = line.split(" ")[1]
                break

        if tree_hash:
            all_files.extend(traverse_tree(repo_path, tree_hash, commit_hash))

        stack.extend(get_commit_parents(commit_data.decode('utf-8')))

    return all_files

def get_hash_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.readline()

def get_filename_from_hash(commitTree, targetPath: str) -> str:
    targetHash = get_hash_from_file(targetPath)
    for filename, blob_hash, commit_hash in commitTree:
        if blob_hash == targetHash:
            return filename
    return ""

def get_all_commits(commitTree, target: str) -> List[str]:
    result = []
    for filename, blob_hash, commit_hash in commitTree:
        if filename == target:
            result.append(commit_hash)
    return result

def buildMermaid(commits: List[str]) -> str:
    mermaid_code = "graph TD\n"
    if len(commits) == 1:
        mermaid_code += f"\t{commits[0]} --> {commits[0]}\n"
    else:
        for i in range(1, len(commits)):
            mermaid_code += f"\t{commits[i-1]} --> {commits[i]}\n"
    return mermaid_code

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Git Dependency Graph Generator")
    parser.add_argument("repo_path", help="Path to the Git repository")
    parser.add_argument("file_hash_path", help="Hash of the file to track dependencies")
    parser.add_argument("output_path", help="Path to save the Mermaid graph")

    args = parser.parse_args()

    commit_tree = traverse_commits(args.repo_path)

    target_filename = get_filename_from_hash(commit_tree, args.file_hash_path)
    if target_filename == "":
        print("Нет такого файла!")
        sys.exit()

    commitArray = get_all_commits(commit_tree, target_filename)

    mermaid = buildMermaid(commitArray)

    with open(args.output_path, "w") as file:
        file.write(mermaid)

    print("Dependency graph generated and saved to:", args.output_path)
