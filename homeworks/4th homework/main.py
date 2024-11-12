import argparse
from logging import *
from assembly import Assembler
from virtual_machine import VirtualMachine

def main():
    parser = argparse.ArgumentParser(description="Assembler")
    parser.add_argument("--source", required=True, help="Путь к исходному файлу программы.")
    parser.add_argument("--binary", required=True, help="Путь к бинарному файлу.")
    parser.add_argument("--log", required=True, help="Путь к файлу лога (XML).")
    parser.add_argument("--result", required=True, help="Путь к файлу результата (XML).")
    parser.add_argument("--memory_range", type=int, nargs=2, required=True, help="Диапазон памяти (начало конец).")

    args = parser.parse_args()

    # Инициализация ассемблера и создание бинарного файла
    assembler = Assembler()
    assembler.assemble(args.source, args.binary, args.log)
    # Сохранение лога
    #save_log_to_file(log_entries, args.log)
    # Инициализация виртуальной машины и выполнение бинарного файла
    vm = VirtualMachine(memory_size=1024)
    vm.execute(args.binary, args.result, args.memory_range)

if __name__ == "__main__":
    main()
