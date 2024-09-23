from zipfile import ZipFile
import SenyashaSystem
import ConfigLoader
import TestSystem
import tkinter as tk


def main():

    root = tk.Tk()
    root.title("System Console")
    root.geometry("500x400")
    config = ConfigLoader.ConfigLoader("config.xml") # Парсим конфиг
    zipfile = ZipFile(config.get_zip_path())
    system = SenyashaSystem.System("", zipfile, config.get_zip_path(), root)  # Иницилизируем систему
    # testsystem = TestSystem.System("", zipfile, config.get_zip_path()) # Иницилизируем систему
    # testsystem.start()
    root.mainloop()


if __name__ == "__main__":
    main()