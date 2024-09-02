### Задача 1
***cat*** - считывание файла
***sort*** - сортировка данных

**passwd.txt**:
```$ cat passwd.txt
Anton
DragZet
Zetsize
Mirea
```

**Решение**:
```$ cat passwd.txt | sort
Anton
DragZet
Mirea
Zetsize
```

### Задача 2

***grep - i*** - поиск строк по подстроке (не учитывая регистр)
***sort -nk2 -r*** - числовая сортировка в обратном порядке по 2 столбцу
***head -n 5*** - вывод первых 5 строк
***awk '{print $1, $2}'*** - вывод заданных столбцов

**Решение**:
```$ cat /etc/protocols  | grep -v Copyright | sort -nk2 -r | head -n 5 | awk '{print $1, $2}'
rvd 66
ipv6-opts 60
ipv6-nonxt 59
ipv6-icmp 58
ah 51
```

