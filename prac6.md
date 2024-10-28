## Задание 0

![image](https://github.com/user-attachments/assets/a3117572-359c-4d37-99f1-1504d84b7e21)

## Визуализация графа

Для визуализации напишем скрипт на python:

```python
from graphviz import Source

file_path = 'civgraph.txt'

with open(file_path, 'r') as f:
    dot_data = f.read()

src = Source(dot_data)
src.render('civgraph', format='png')
```

```Make
run:
        python3 need.py
```

![image](https://github.com/user-attachments/assets/5715fb21-f4ff-4058-865e-8b89e481a2af)

## Задание 1

```python
import json

def generate_makefile(graph):
    with open('Makefile', 'w') as f:
        for target, deps in graph.items():
            deps_str = ' '.join(deps)
            f.write(f'{target}: {deps_str}\n')
            f.write(f'\t@echo "Building {target}"\n\n')

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    generate_makefile(graph)
    print("Makefile создан.")
```

```
{
    "mathematics": ["drama_poetry", "mysticism"],
    "drama_poetry": ["foreign_trade"],
    "foreign_trade": ["code_of_laws"],
    "mysticism": ["early_empire"],
    "early_empire": ["pottery"],
    "pottery": [],
    "code_of_laws": [],
    "mining": [],
    "bronze_working": ["mining"],
    "sailing": ["astrology"],
    "astrology": [],
    "celestial_navigation": ["sailing"],
    "writing": ["pottery"],
    "irrigation": [],
    "currency": [],
    "masonry": []
}
```

![image](https://github.com/user-attachments/assets/a70e23f1-6782-457f-b913-76e3ebefb028)

## Задание 2

```python
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends

def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        allString = ""
        for target in depends:
            if target not in tasks:
                allString += " " + target
                tasks.add(target)
                tempString = " ".join([i for i in graph[target] if i not in tasks])
                result_string += f'{target}: {tempString}\n'
                result_string += f'\t@echo "Building {target}"\n\n'
        if result_string != "":
            allString+="\n\n"
            f.write("all:" + allString)
            f.write(result_string)
            f.write(".PHONY:" + allString)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    generate_makefile(graph, target)
    print("Makefile создан.")

```

![image](https://github.com/user-attachments/assets/9b35c3bc-99c0-44cb-8821-2bc45e706c67)

## Задание 3

```python
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends

def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        allString = ""
        for target in depends:
            if target not in tasks:
                allString += " " + target
                tasks.add(target)
                tempString = " ".join([i for i in graph[target] if i not in tasks])
                result_string += f'{target}: {tempString}\n'
                result_string += f'\t@echo "Building {target}"\n\n'
        if result_string != "":
            allString+="\n\n"
            f.write("all:" + allString)
            f.write(result_string)
            f.write(".PHONY:" + allString)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

def clean():
    if os.path.exists(completed_tasks_file):
        os.remove(completed_tasks_file)
        print("Cleaned completed tasks.")

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    if target == "clean":
        clean()
    else:
        generate_makefile(graph, target)
        print("Makefile создан.")

```

Сгенерированныый файл:

```make
all: masonry early_empire pottery drama_poetry writing astrology code_of_laws foreign_trade irrigation currency sailing mysticism mining celestial_navigation bronze_working

masonry: mining
	@echo "Building masonry"

early_empire: foreign_trade
	@echo "Building early_empire"

pottery: 
	@echo "Building pottery"

drama_poetry: astrology irrigation masonry early_empire mysticism
	@echo "Building drama_poetry"

writing: pottery
	@echo "Building writing"

astrology: 
	@echo "Building astrology"

code_of_laws: 
	@echo "Building code_of_laws"

foreign_trade: code_of_laws
	@echo "Building foreign_trade"

irrigation: pottery
	@echo "Building irrigation"

currency: writing foreign_trade
	@echo "Building currency"

sailing: 
	@echo "Building sailing"

mysticism: foreign_trade
	@echo "Building mysticism"

mining: 
	@echo "Building mining"

celestial_navigation: sailing astrology
	@echo "Building celestial_navigation"

bronze_working: mining
	@echo "Building bronze_working"

.PHONY: masonry early_empire pottery drama_poetry writing astrology code_of_laws foreign_trade irrigation currency sailing mysticism mining celestial_navigation bronze_working

```

![image](https://github.com/user-attachments/assets/355b9321-852f-4758-824a-f6edb2b87fd4)

## Задание 4

prod.go:

```golang
package main

import "fmt"

func main() {
	fmt.Println(GetMessage())
}
```

data.go:

```golang
package main

func GetMessage() string {
	return "Привет из data.go!"
}
```

Makefile:

```make
SRC = prod.go data.go
OUT = prod
ARCHIVE = archive.zip

all: $(OUT) $(ARCHIVE)

$(OUT): $(SRC)
	go build -o $(OUT) $(SRC)
	@echo "$(OUT) builded."

$(ARCHIVE): $(OUT)
	powershell Compress-Archive -Path *.* -DestinationPath $(ARCHIVE) -Force
	@echo "Archived in $(ARCHIVE)."

clean:
	del $(OUT) $(ARCHIVE)
	@echo "Cleaned."

.PHONY: all clean
```

![image](https://github.com/user-attachments/assets/4dabf487-14ce-4536-b7eb-638e19743983)


