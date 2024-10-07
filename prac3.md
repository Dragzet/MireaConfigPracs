### Задача 1

Создадим файл need.jsonnet, запишем в него:
```
local groupPrefix = 'ИКБО-';
local year = '-23';
local groupNum = std.range(1, 10);

local studentData = [
  {name: "Коротков А. А.", age: 52, groupIndex: 3},
  {name: "Жагло И. Д.", age: 20, groupIndex: 2},
  {name: "Запрягаев М. А.", age: 19, groupIndex: 1},
  {name: "Харитонов А.Н.", age: 18, groupIndex: 4}
];

{
  groups: [groupPrefix + std.toString(i) + year for i in groupNum],

  students: [
    {
      age: student.age,
      group: groupPrefix + std.toString(student.groupIndex) + year,
      name: student.name
    } for student in studentData
  ],

  subject: "Конфигурационное управление"
}
```

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
<expression> = <term> | <open> <term> <operation> <term> <close> | <negative> <open> <term> <operation> <term> <close> | <open> <expression> <operation> <expression> <close>| <negative> <open <expression> <close>
<term> = <variable> | <negative> <variable> | <open> <variable> <operation> <variable> <close> | <negative> <open> <variable> <operation> <variable> <close>
<variable> = x | y | z | w
<operation> = & | V
<negative> = ~
<open> = (
<close> = )
"""
```
