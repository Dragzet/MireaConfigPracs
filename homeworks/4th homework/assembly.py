import struct
import logging
from logging import *

class Assembler:
    """
    Assembler for simple virtual machine.
    """

    def __init__(self):
        """
        Initializes the assembler.
        """
        self.commands = {
            'LOAD_CONST': 0,  # Код операции для загрузки константы
            'READ_MEM': 6,   # Код операции для чтения значения из памяти
            'WRITE_MEM': 7,   # Код операции для записи значения в память
            'EQUAL': 1       # Код операции для бинарной операции "=="
        }


    def assemble(self, source_path, binary_path, log_path):
        """
        Assembles the code from a source file and writes it to a binary file.

        :param source_path: Path to the source file.
        :param binary_path: Path to the binary file.
        :param log_path: Path to the log file.
        """
        with open(source_path, 'r', encoding="utf-8") as source_file, open(binary_path, 'wb') as binary_file:
            log_data = []
            for line in source_file:
                command, args = self.parse_instruction(line.strip())
                if command is None:
                    continue
                binary_instruction = self.encode_instruction(command, args)
                binary_file.write(binary_instruction)

                log_data.append(logging.create_log_entry(command, args, binary_instruction))
            logging.save_log_to_file(log_data, log_path)

    def parse_instruction(self, line):
        """
        Parses an instruction from a line of source code.

        :param line: The line of source code.
        :return: The command and its arguments.
        """
        if not line.strip():
            return None, None

        # Удаляем комментарии
        line = line.split('#', 1)[0].strip()
        if not line:
            return None, None

        parts = line.replace(',', '').split()
        command = parts[0]

        if command in ['WRITE_MEM', 'READ_MEM']:
            offset = parts[1]
            flag = parts[2]
            args = [int(offset), int(flag)]
        elif command == 'EQUAL':
            firstMemory = parts[1]
            secondMemory = parts[2]
            args = [int(firstMemory), int(secondMemory)]
        else:
            args = [int(arg) for arg in parts[1:]]
        return command, args

    def encode_instruction(self, command, args):
        """
        Encodes an instruction into a binary format.

        :param command: The command.
        :param args: The arguments.
        :return: The binary instruction.
        """
        if command == 'LOAD_CONST':
            opcode = self.commands[command]
            B = args[0]
            return struct.pack('<BB', opcode, B)
        elif command == 'READ_MEM':
            opcode = self.commands[command]
            B = args[0]  # offset
            C = args[1]  # flag
            return struct.pack('<BBB', opcode, B, C)
        elif command == 'WRITE_MEM':
            opcode = self.commands[command]
            B = args[0]  # offset
            C = args[1]  #3rd byte
            return struct.pack('<BBB', opcode, B, C)
        elif command == 'EQUAL':
            opcode = self.commands[command]
            A = args[0]  # Первый адрес
            B = args[1]  # Второй Адрес
            return struct.pack('<BBB', opcode, A, B)
        else:
            raise ValueError(f"Неизвестная команда {command}")