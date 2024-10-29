### Первое задание

![image](https://github.com/user-attachments/assets/db890f37-667e-46de-9bcd-da006e507f23)


```bash
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout in
```


### Второе задание 

```bash
C:\need>git init
Initialized empty Git repository in C:/need/.git/

C:\need>git config user.name "senyasha"

C:\need>git config user.email "example@gmail.com"

C:\need>touch prog.py
"touch" не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.

C:\need>echo "test gile" > prog.py

C:\need>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        prog.py

nothing added to commit but untracked files present (use "git add" to track)

C:\need>git add .

C:\need>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   prog.py


C:\need>git commit -m "test commit"
[master (root-commit) c6e2828] test commit
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

C:\need>git log --oneline
c6e2828 (HEAD -> master) test commit

C:\need>git log
commit c6e2828ffbd9cfa935450f318f390c44bc6c94db (HEAD -> master)
Author: senyasha <example@gmail.com>
Date:   Tue Oct 29 13:56:51 2024 +0300

    test commit

C:\need>
```

### Третье задание

```bash
senyasha@Senyasha:~/prac4$ git init --bare server.git
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/senyasha/prac4/server.git/
senyasha@Senyasha:~/prac4$ cd coder1/
senyasha@Senyasha:~/prac4/coder1$ git remote add server ../server.git/
senyasha@Senyasha:~/prac4/coder1$ git remote -v
server  ../server.git/ (fetch)
server  ../server.git/ (push)
senyasha@Senyasha:~/prac4/coder1$ git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 202 bytes | 202.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server.git/
 * [new branch]      master -> master
senyasha@Senyasha:~/prac4/coder1$ cd ..
senyasha@Senyasha:~/prac4$ git clone server.git coder2
Cloning into 'coder2'...
done.
senyasha@Senyasha:~/prac4$ cd coder1/
senyasha@Senyasha:~/prac4/coder1$ echo "INFO prog1" >> readme.md
senyasha@Senyasha:~/prac4/coder1$ git add readme.md
senyasha@Senyasha:~/prac4/coder1$ git commit -m "prog1 info"
[master 432ed13] prog1 info
 1 file changed, 1 insertion(+)
senyasha@Senyasha:~/prac4/coder1$ git push server master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 244 bytes | 244.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server.git/
   47a93b1..432ed13  master -> master
senyasha@Senyasha:~/prac4/coder1$ cd ../coder2
senyasha@Senyasha:~/prac4/coder2$ echo "\nINFO prog2" >> readme.md
senyasha@Senyasha:~/prac4/coder2$ git add readme.md
senyasha@Senyasha:~/prac4/coder2$ git config user.name "coder2"
senyasha@Senyasha:~/prac4/coder2$ git config user.email "coder2@gmail.com"
senyasha@Senyasha:~/prac4/coder2$ git commit -m "prog2 info"
[master fc2e8b1] prog2 info
 1 file changed, 1 insertion(+)
senyasha@Senyasha:~/prac4/coder2$ git push origin master
To /home/senyasha/prac4/server.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to '/home/senyasha/prac4/server.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
senyasha@Senyasha:~/prac4/coder2$ git pull --no-rebase origin master
From /home/senyasha/prac4/server
 * branch            master     -> FETCH_HEAD
Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.
senyasha@Senyasha:~/prac4/coder2$ git add readme.md
senyasha@Senyasha:~/prac4/coder2$ git commit -m "solve conflict"
[master 5509b2d] solve conflict
senyasha@Senyasha:~/prac4/coder2$ git push origin master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 552 bytes | 552.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To /home/senyasha/prac4/server.git
   432ed13..5509b2d  master -> master
senyasha@Senyasha:~/prac4/coder2$ git log --graph --all
*   commit 5509b2d340e1bb8353307b85cbe5e48088358e17 (HEAD -> master, origin/master, origin/HEAD)
|\  Merge: fc2e8b1 432ed13
| | Author: coder2 <coder2@gmail.com>
| | Date:   Tue Oct 29 14:39:09 2024 +0300
| |
| |     solve conflict
| |
| * commit 432ed13cf1499912200cbd507cc8a4f7048337df
| | Author: coder1 <coder1@gmail.com>
| | Date:   Tue Oct 29 14:36:03 2024 +0300
| |
| |     prog1 info
| |
* | commit fc2e8b1e238c6f846507cdfe5f31f428480d0a53
|/  Author: coder2 <coder2@gmail.com>
|   Date:   Tue Oct 29 14:37:00 2024 +0300
|
|       prog2 info
|
* commit 47a93b1025c478d7c18c77ba94a6a1a6864e2253
  Author: coder1 <coder1@gmail.com>
  Date:   Tue Oct 29 14:34:51 2024 +0300

      add readme
```

![image](https://github.com/user-attachments/assets/e588e20a-80bc-4b62-a172-51f9f1b30ffa)

### Задание 4

```python
import os
import subprocess

def get_git_objects():
    try:
        result = subprocess.run(
            ['git', 'rev-list', '--all'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        objects = result.stdout.splitlines()

        for obj in objects:
            print(f"Коммит: {obj}")
            try:
                content = subprocess.run(
                    ['git', 'cat-file', '-p', obj],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=True
                )
                print(content.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Ошибка {obj}: {e.stderr}")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e.stderr}")

if __name__ == "__main__":
    if not os.path.exists('.git'):
        print("Нет гита")
    else:
        get_git_objects()
```

![image](https://github.com/user-attachments/assets/2658981a-5f3c-4d72-9f0f-8a849a0e3c1c)

