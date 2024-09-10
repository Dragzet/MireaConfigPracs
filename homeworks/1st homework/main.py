from zipfile import ZipFile
import SenyashaSystem
import ConfigLoader


def main():

    config = ConfigLoader.ConfigLoader("config.xml") # Парсим конфиг
    zipfile = ZipFile(config.get_zip_path())
    system = SenyashaSystem.System("", zipfile, config.get_zip_path()) # Иницилизируем систему
    system.start() # Старт системы


if __name__ == "__main__":
    main()