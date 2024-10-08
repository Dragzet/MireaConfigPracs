import os
import zipfile


class System:

    USER = "SENYASHA"

    def __init__(self, path, zipfile, zipfilePath):
        self.path = path # Текущее положение
        self.zipfile = zipfile # ОС
        self.zipfilePath = zipfilePath # Путь к ОС

    def ls(self):
        result = []
        for file in self.zipfile.namelist():
            if file[-1] == "/":
                if len(self.path.split('/')) + 1 == len(file.split("/")) and self.path in file: # Обработчик для директорий
                    result.append(file.replace(self.path, ""))
            else:

                if len(self.path.split('/')) == len(file.split("/")) and self.path in file: # Обработчик для файлов
                    result.append(file.replace(self.path, ""))

        return sorted(result, key=lambda s: ("/" in s, s), reverse=True) # Директории вперед, файлы назад

    def isExist(self, target):
        return target in self.ls()

    def isDirExist(self, target):
        if target[-1] != "/":
            target += "/"
        for file in self.zipfile.namelist():
            if file[-1] == "/" and file == target:
                return True
        return False

    def cd(self, target_directory):
        targets = target_directory.split()[-1].split("/")
        for target in targets:
            if len(target) == 0: continue
            if target == ".." and self.path.count("/") <= 1: # Идем к корню
                self.path = ""
                continue
            if target == "..":
                self.path = self.path[:self.path[:-2].rfind("/")] + "/"
                continue
            if target[-1] != "/": # Обрабатываем случаи, когда приходит Sys вместо Sys/
                target += "/"
            if not self.isExist(target): # Есть ли в локальном пути такая папка??
                return "Error: Unknown dir"
            self.path = self.path + target
        return

    def rm(self, target):
        if target[-1] == "/": # Точно ли это не директория?
            return "Error: Can't remove directory"
        if not self.isExist(target): # Есть ли такой файл в локальном пути?
            return "Error: No such file"

        tempZip = self.zipfilePath + ".tmp" # Создаем временный файл для записи

        with zipfile.ZipFile(tempZip, "w") as zip:
            for file in self.zipfile.infolist():
                if file.filename.split("/")[-1] != target and file.filename not in self.ls(): # Если наша цель - не записываем в наш новый файлик
                    data = self.zipfile.read(file.filename)
                    zip.writestr(file, data)

        self.zipfile.close()
        os.remove(self.zipfilePath) # Удаляем старый файл, ставим наш новый
        os.rename(tempZip, self.zipfilePath)
        self.zipfile = zipfile.ZipFile(self.zipfilePath)

    def cp(self, target, targetPath):
        if target[-1] == "/":
            return "Error: Cannot copy dir"
        if not self.isExist(target): # Есть ли такой файл в локальном пути?
            return "Error: File doesn't exist"
        if not self.isDirExist(targetPath): # Есть ли такая директория во всей ОС?
            return "Error: Dir doesn't exist"

        if targetPath[-1] != "/":
            targetPath += '/'

        tempZip = self.zipfilePath + ".tmp" # Создаем временный файлиу

        with zipfile.ZipFile(tempZip, "w") as zip:
            for file in self.zipfile.infolist():
                if file.filename.split("/")[-1] != target: # Не наша цель - просто записываем
                    data = self.zipfile.read(file.filename)
                    zip.writestr(file, data)
                else:
                    data = self.zipfile.read(file.filename) # Если наша цель, записываем дважды
                    zip.writestr(file, data)
                    zip.writestr(targetPath + "Copy" +file.filename.split("/")[-1], data)


        self.zipfile.close()
        os.remove(self.zipfilePath) # Удаляем старый файл, добавляем новый
        os.rename(tempZip, self.zipfilePath)
        self.zipfile = zipfile.ZipFile(self.zipfilePath)

    def start(self):
        inputLine = input("\n" + self.USER + (" ~\n$ " if self.path == "" else f" {self.path}\n$ "))

        while inputLine != "exit":
            inputLine = inputLine.split()

            match inputLine[0]:
                case "ls":
                    [print(i) for i in self.ls()]
                case "cd":
                    if len(inputLine) != 2:
                        print("Error: Unknown command")
                    else:
                        error = self.cd(inputLine[1])
                        if error:
                            print(error)
                case "rm":
                    if len(inputLine) != 2:
                        print("Error: Unknown command")
                    else:
                        error = self.rm(inputLine[1])
                        if error:
                            print(error)
                case "cp":
                    if len(inputLine) != 3:
                        print("Error: Unknown command")
                    else:
                        error = self.cp(inputLine[1], inputLine[2])
                        if error:
                            print(error)
                case _:
                    print("Error: Unknown command")

            inputLine = input("\n" + self.USER + (" ~\n$ " if self.path == "" else f" {self.path}\n$ "))