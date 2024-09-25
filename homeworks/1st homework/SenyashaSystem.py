import os
import zipfile
from tkinter import scrolledtext
import tkinter as tk

class System:

    USER = "SENYASHA"

    def __init__(self, path, zipfile, zipfilePath, root):
        self.path = path # Текущее положение
        self.zipfile = zipfile # ОС
        self.zipfilePath = zipfilePath # Путь к ОС
        self.root = root

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
        self.output_area.grid(row=0, column=0, padx=10, pady=10)
        self.output_area.config(state=tk.DISABLED)
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, "\n" + self.USER + (" ~\n$ " if self.path == "" else f" {self.path}\n$ "))
        self.output_area.yview(tk.END)
        self.output_area.config(state=tk.DISABLED)

        self.input_field = tk.Entry(root, width=40)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)
        self.input_field.bind("<Return>", self.handle_input)


    def handle_input(self, event=None):
        user_input = self.input_field.get()
        self.input_field.delete(0, tk.END)

        if user_input == "exit":
            self.root.quit()
        else:
            self.process(user_input)

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
            if len(target) == 0: return "Error: Unknown dir"
            if target == ".." and self.path.count("/") <= 1:  # Идем к корню
                self.path = ""
                continue
            if target == "..":
                self.path = self.path[:self.path[:-2].rfind("/")] + "/"
                continue
            if target[-1] != "/":  # Обрабатываем случаи, когда приходит Sys вместо Sys/
                target += "/"
            if not self.isExist(target):  # Есть ли в локальном пути такая папка??
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

    def process(self, command):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, command)
        inputLine = command.split()
        #result = "\n" + self.USER + (" ~\n$ " if self.path == "" else f" {self.path}\n$ ")
        result = "\n"
        if len(inputLine) == 0:
            inputLine = " "
        match inputLine[0]:

            case "ls":
                result += "".join([f"{i}\n" for i in self.ls()])
            case "cd":
                if len(inputLine) != 2:
                    result += "Error: Unknown command"
                else:
                    error = self.cd(inputLine[1])
                    if error:
                        result = error
                        print(error)
            case "rm":
                if len(inputLine) != 2:
                    result += "Error: Unknown command"
                else:
                    error = self.rm(inputLine[1])
                    if error:
                        result += error
            case "cp":
                if len(inputLine) != 3:
                    result += "Error: Unknown command"
                else:
                    error = self.cp(inputLine[1], inputLine[2])
                    if error:
                        result += error
            case _:
                result += "Error: Unknown command"

        # Выводим результат в текстовое поле
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, result)
        self.output_area.yview(tk.END)  # Прокручиваем к концу
        self.output_area.config(state=tk.DISABLED)
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, "\n" + self.USER + (" ~\n$ " if self.path == "" else f" {self.path}\n$ "))
        self.output_area.yview(tk.END)  # Прокручиваем к концу
        self.output_area.config(state=tk.DISABLED)