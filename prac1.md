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
```
$ cat passwd.txt | sort
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
```
$ cat /etc/protocols  | grep -v Copyright | sort -nk2 -r | head -n 5 | awk '{print $1, $2}'
rvd 66
ipv6-opts 60
ipv6-nonxt 59
ipv6-icmp 58
ah 51
```
### Задача 3

**Решение**:
```  GNU nano 7.2                                   task3
#!/bin/bash
string=$1
size=${#string}
echo -n "+"
for ((i=-2;i<size;i++))
do
echo -n "-"
done
echo "+"
echo "| $string |"
echo -n "+"
for ((i=-2;i<size;i++))
do
echo -n "-"
done
echo "+"
```

```
$ ./task3 "hello mirea"
+-------------+
| hello mirea |
+-------------+
```

### Задача 4

***grep -o*** - поиск строк по заданному шаблону

```
$ cat main.cpp | grep -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' | sort | uniq
Close
Create
Files
MyFile
Write
a
and
be
but
can
close
enough
file
filename
fstream
fun
include
int
iostream
is
it
main
namespace
ofstream
open
std
text
the
to
tricky
txt
using
```

### Задача 5
***chmod -x*** - выдача прав доступа

***cp*** - копирование файла

```
#!/bin/bash
chmod +x $1
cp $1 /usr/local/bin

```

### Задача 6

***grep -o '#'*** - ищем строку по шаблону

***"$value" != "#"*** - проверка на наличие комментария

**Решение**:
```
#!/bin/bash
value=`cat $1 | head -n 1 | grep -o '#'`
if [ "$value" != "#" ]; then
   echo "No comments"
else
   echo "Comment in first line"
fi

```

**Проверка**:
1) Файл без комментариев
```
arhar@Senyasha MINGW64 /
$ cat nocomment.py
a = input()
print(a)

arhar@Senyasha MINGW64 /
$ ./task6 nocomment.py
No comments
```
2) Комментарий не в первой строке
```
arhar@Senyasha MINGW64 /
$ cat 2comment.py
a = input()
#conmment
print(a)

arhar@Senyasha MINGW64 /
$ ./task6 2comment.py
No comments
```
3) Комментарий в первой строке
```
arhar@Senyasha MINGW64 /
$ cat comment.py
#Print a
a = input()
print(a)

arhar@Senyasha MINGW64 /
$ ./task6 comment.py
Comment in first line
```

### Задача 7:

***find $1 -type f -exec md5sum {} +*** - поиск **только файлов** в заданном каталоге и подкаталогах, высчитывая хэш md5 для сравнения файлов

***uniq -w32 -D*** - оставляем неуникальные значения, сравниваем по 0-32 символам

***cut -c 33-*** - обрезание строки с 33 символа

**Решение**:
```
#!/bin/bash

find $1 -type f -exec md5sum {} + | sort | uniq -w32 -D | cut -c 33-
```

**Проверка**:

4 файла, где file2.txt и file4.txt - уникальны

```
total 4
-rw-r--r-- 1 arhar arhar 12 Sep  3 11:09 file1.txt
-rw-r--r-- 1 arhar arhar 13 Sep  3 11:09 file2.txt
-rw-r--r-- 1 arhar arhar 12 Sep  3 11:09 file3.txt
-rw-r--r-- 1 arhar arhar 14 Sep  3 11:09 file4.txt
```

```
arhar@Senyasha MINGW64 /prac1
$ ./task7 data7
 *data7/file1.txt
 *data7/file3.txt
```

### Задача 8:

***xargs tar -rvf "*.tar"*** - архивирование файлов

**Решение**:
```  GNU nano 7.2                    task8
#!/bin/bash

find . -type f -name "*.$1" | xargs tar -rvf archive.tar
```

**Проверка**:

```
arhar@Senyasha MINGW64 /prac1
$ ./task8 txt
./data7/file1.txt
./data7/file2.txt
./data7/file3.txt
./data7/file4.txt
./need.txt
./need2.txt

arhar@Senyasha MINGW64 /prac1
$ ls
archive.tar  data7  need.txt  need2.txt  task7  task8
```

### Задача 9

***sed 's/    /\t/g'*** - замена подстроки на заданную

***file1 > file2*** - запись в файл

**Решение**:
```
#!/bin/bash

sed 's/    /\t/g' $1 > $2
```

### Задача 10

***find path -type f -empty -name "*.txt"*** - поиск всех пустых текстовых файлов

**Решение:**
```
#!/bin/bash

find $1 -type f -empty -name "*.txt"

```

**Проверка:**
```
arhar@Senyasha MINGW64 /prac1/task10
$ touch need.txt

arhar@Senyasha MINGW64 /prac1/task10
$ touch need.py

arhar@Senyasha MINGW64 /prac1/task10
$ touch need2.txt

arhar@Senyasha MINGW64 /prac1/task10
$ ./task10 .
./need.txt
./need2.txt
```
