### Задача 1

Создадим файл need.jsonnet, запишем в него:
```
local groups = [
  "ИКБО-1-24",
  "ИКБО-2-24",
  "ИКБО-3-24",
  "ИКБО-4-24",
  "ИКБО-5-24",
  "ИКБО-6-24",
  "ИКБО-7-24",
  "ИКБО-8-24",
  "ИКБО-9-24",
  "ИКБО-10-24",
  "ИКБО-11-24",
  "ИКБО-12-24",
  "ИКБО-13-24",
  "ИКБО-14-24",
  "ИКБО-15-24",
  "ИКБО-16-24",
  "ИКБО-17-24",
  "ИКБО-18-24",
  "ИКБО-19-24",
  "ИКБО-20-24",
  "ИКБО-21-24",
  "ИКБО-22-24",
  "ИКБО-23-24",
  "ИКБО-24-24"
];

local student(name, age, group, subject) = {
  name: name,
  age: age,
  group: group,
  subject: subject,
};

local students = [
  student("Иванов И.И.", 19, "ИКБО-4-24", "Конфигурационное управление"),
  student("Петров П.П.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Сидоров С.С.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Харитонов А.Н", 18, "ИКБО-10-24", "Конфигурационное управление")
];

{
  groups: groups,
  students: students,
}
```

В результате увидим:

![image](https://github.com/user-attachments/assets/586da9e9-317b-4bef-af6e-abca719e485c)

### Задача 2

```
 let List/length =
        https://prelude.dhall-lang.org/v21.1.0/List/length

  let groups =
        List/map Natural Text (\(i : Natural) -> "ИКБО-${Natural/show i}-23")
        (List/replicate 24 Natural/successor 0)
  
  let students =
      [ { name = "Иванов И.И.", group = "ИКБО-4-20", age = 19 }
      , { name = "Петров П.П.", group = "ИКБО-5-20", age = 18 }
      , { name = "Сидоров С.С.", group = "ИКБО-5-20", age = 18 }
      , { name = "Харитонов А.Н.", group = "ИКБО-10-23", age = 18 }
      ]
  
  in  { groups = groups
      , students = students
      , subject = "Конфигурационное управление"
      }
```


### Задача 3

```python
BNF = '''
E = 0 | 1 | 0 E | 1 E
'''
```

### Задача 4

```python
BNF = '''
E =  | ( E ) | { E } | E E
'''
```

### Задача 5

```python
BNF = """
E = L | E & L | E | E | E
L = x | y | "(" E ")" | "~" L | "(" E ")" | "~" L
"""
```
