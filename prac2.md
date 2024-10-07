### Задание 1

Для того, чтобы получить служебную инфрормацию пакета надо воспользоваться командой ```pip show <package_name>```.

**Решение**:

```bash
pip show matplotlib
```

В качестве ответа получаем служебную информацию:
```bash
Name: matplotlib
Version: 3.9.2
Summary: Python plotting package
Home-page: 
Author: John D. Hunter, Michael Droettboom
Author-email: Unknown <matplotlib-users@python.org>
License: License agreement for matplotlib versions 1.3.0 and later
```

Для того, чтобы получить пакет, не используя пакетный менеджер, можно клонировать репозиторий к себе, а затем прописать ```python setup.py install```.

### Задание 2

Для того, чтобы получить служебную информацию пакета надо воспользоваться командой ```npm info <package_name>```.

**Решение**:

```bash
npm info express
```

В качестве ответа получим служебную информацию:
```bash
express@4.19.2 | MIT | deps: 31 | versions: 276
Fast, unopinionated, minimalist web framework
http://expressjs.com/

keywords: express, framework, sinatra, web, http, rest, restful, router, app, api

dist
.tarball: https://registry.npmjs.org/express/-/express-4.19.2.tgz
.shasum: e25437827a3aa7f2a827bc8171bbbb664a356465
.integrity: sha512-5T6nhjsT+EOMzuck8JjBHARTHfMht0POzlA60WV2pMD3gyXw2LZnZ+ueGdNxG+0calOJcWKbpFcuzLZ91YWq9Q==
.unpackedSize: 214.8 kB
...
```

Для установки пакета напрямую из репозитория надо клонировать этот репозиторий к себе, а затем прописать команду ```npm install```.


### Задание 3

**Граф для matplotlib**:
```
digraph G {
  node [shape=rect];

  "matplotlib" -> "numpy";
  "matplotlib" -> "pillow";
  "matplotlib" -> "cycler";
  "matplotlib" -> "kiwisolver";
  "matplotlib" -> "pyparsing";
  "matplotlib" -> "python-dateutil";
}
```
![image](https://github.com/user-attachments/assets/2737978c-7ce7-46a5-8b1f-8581905ff432)

**Граф для express**:

```dot
digraph G {
  node [shape=rect];

  "express" -> "accepts";
  "express" -> "array-flatten";
  "express" -> "body-parser";
  "express" -> "content-disposition";
  "express" -> "cookie";
  "express" -> "cookie-signature";
  "express" -> "debug";
  "express" -> "depd";
  "express" -> "encodeurl";
  "express" -> "escape-html";
  "express" -> "etag";
  "express" -> "finalhandler";
  "express" -> "fresh";
  "express" -> "merge-descriptors";
  "express" -> "methods";
  "express" -> "on-finished";
  "express" -> "parseurl";
  "express" -> "path-to-regexp";
  "express" -> "proxy-addr";
  "express" -> "qs";
  "express" -> "range-parser";
  "express" -> "safe-buffer";
  "express" -> "send";
  "express" -> "serve-static";
  "express" -> "setprototypeof";
  "express" -> "statuses";
  "express" -> "type-is";
  "express" -> "utils-merge";
  "express" -> "vary";
}
```

![image](https://github.com/user-attachments/assets/216e5bc2-0bf2-4588-b4db-6773b7169db3)

### Задание 4

```
include "globals.mzn";

array[1..6] of var 0..9: numbers;
constraint all_different(numbers);

var int: FirstSum = sum(numbers[1..3]);
constraint FirstSum == sum(numbers[4..6]);

solve minimize FirstSum;

output ["Билет - ", show(numbers), " Сумма 3х цифр - ", show(FirstSum)];
```

### Задание 5

```
int: menu_count = 6;
int: dropdown_count = 5;
int: icons_count = 2;

array[1..menu_count] of tuple(int, int, int): menu_versions = 
  [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];

array[1..dropdown_count] of tuple(int, int, int): dropdown_versions = 
  [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];

array[1..icons_count] of tuple(int, int, int): icons_versions = 
  [(1,0,0), (2,0,0)];

tuple(int, int, int): root_version = (1,0,0);
  
var 1..menu_count: menu;
var 1..dropdown_count: dropdown;
var 1..icons_count: icons;

constraint (menu_versions[menu] == (1,0,0) \/ menu_versions[menu] == (1, 5, 0) /\ icons_versions[icons] == (1, 0, 0));

constraint (menu_versions[menu].2 >= 1 /\ menu_versions[menu].2 <= 5) -> (dropdown_versions[dropdown] == (2, 3, 0) \/ dropdown_versions[dropdown] == (2, 0, 0));

constraint menu_versions[menu] == (1, 0, 0) -> dropdown_versions[dropdown] == (1, 8, 0);

constraint (dropdown_versions[dropdown].2 >= 0 /\ dropdown_versions[dropdown].2 <= 3) -> icons_versions[icons] == (2, 0, 0);

solve satisfy;

output [
  "Menu version: ", show(menu_versions[menu]), "\n",
  "Dropdown version: ", show(dropdown_versions[dropdown]), "\n",
  "Icons version: ", show(icons_versions[icons]), "\n"
];
```

***Вывод:***

![image](https://github.com/user-attachments/assets/07c18fee-6774-44b8-9dc2-3cf9740b4299)


### Задание 6

```
int: foo_count = 2;
int: left_count = 1;
int: right_count = 1;
int: shared_count = 2;
int: target_count = 2;

array[1..foo_count] of tuple(int, int, int): foo_versions = 
[(1,0,0), (1,1,0)];

array[1..left_count] of tuple(int, int, int): left_versions = 
[(1,0,0)];

array[1..right_count] of tuple(int, int, int): right_versions = 
[(1,0,0)];

array[1..shared_count] of tuple(int, int, int): shared_versions = 
[(1,0,0), (2,0,0)];

array[1..target_count] of tuple(int, int, int): target_versions = 
[(1,0,0), (2,0,0)];

tuple(int, int, int): root_version = (1,0,0);


var 1..foo_count: foo;
var 1..left_count: left;
var 1..right_count: right;
var 1..shared_count: shared;
var 1..target_count: target;


constraint (foo_versions[foo].1 == 1 /\ foo_versions[foo].2 >= 0) 
/\ (target_versions[target].1 == 2 /\ target_versions[target].2 >= 0); 

constraint foo_versions[foo] == (1, 1, 0) -> 
(left_versions[left].1 == 1 /\ left_versions[left].2 >= 0) 
/\ (right_versions[right].1 == 1 /\ right_versions[right].2 >= 0); 


constraint left_versions[left] == (1, 0, 0) ->
(shared_versions[shared].1 >= 1);

constraint right_versions[right] == (1, 0, 0) ->
(shared_versions[shared].1 < 2);

constraint shared_versions[shared] == (1, 0, 0) ->
(target_versions[target].1 == 1 /\ target_versions[target].2 >= 0);

solve satisfy;

output [
"Root version: ", show(root_version), "\n",
"Foo version: ", show(foo_versions[foo]), "\n",
"Left version: ", show(left_versions[left]), "\n",
"Right version: ", show(right_versions[right]), "\n",
"Shared version: ", show(shared_versions[shared]), "\n",
"Target version: ", show(target_versions[target]), "\n"
];
```

***Вывод:***

![image](https://github.com/user-attachments/assets/644c5681-29a7-42ea-aaeb-632674b958ad)




### Задание 7

```
int: num_packages;

set of int: Packages = 1..num_packages;

array[Packages] of set of int: Versions;

array[Packages] of var int: selected_version;

array[Packages] of set of int: dependencies;

array[Packages, Packages] of int: min_version;

array[Packages, Packages] of int: max_version;

constraint
  forall(i in Packages) (
    forall(dep in dependencies[i]) (
      selected_version[dep] >= min_version[i, dep] /\
      selected_version[dep] <= max_version[i, dep]
    )
  );

solve satisfy;
```
