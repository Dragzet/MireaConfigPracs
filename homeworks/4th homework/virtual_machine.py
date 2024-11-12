import struct
import xml.etree.ElementTree as ET

class VirtualMachine:
    """
    Virtual machine for executing binary code.

    Attributes:
        stack (list): Stack of the virtual machine.
        memory (list): Memory of the virtual machine.
    """

    def __init__(self, memory_size):
        """
        Initializes the virtual machine.

        :param memory_size: Size of the memory.
        """
        self.memory = [0] * memory_size
        self.stack = [0]

    def execute(self, binary_path, result_path, memory_range):
        """
        Executes the binary code from a file and writes the result to a file.

        :param binary_path: Path to the binary file.
        :param result_path: Path to the result file.
        :param memory_range: Range of memory to write to the result file.
        """
        with open(binary_path, 'rb') as binary_file:
            while True:
                opcode_byte = binary_file.read(1)
                if not opcode_byte:
                    break
                opcode = opcode_byte[0]
                if opcode == 0:  # LOAD_CONST
                    self.load_const(binary_file)
                elif opcode == 6:  # READ_MEM
                    self.read_mem(binary_file)
                elif opcode == 7:  # WRITE_MEM
                    self.write_mem(binary_file)
                elif opcode == 1:  # EQUAL
                    self.equal(binary_file)
                else:
                    raise ValueError(f"Неизвестный код операции: {opcode}")

            self.save_memory_to_xml(memory_range, result_path)

    def load_const(self, binary_file):
        """
        Executes the LOAD_CONST command.

        :param binary_file: File object with the binary code.
        """
        data = binary_file.read(1)
        if len(data) < 1:
            raise ValueError("Недостаточно данных для команды LOAD_CONST")
        B = struct.unpack('<B', data)[0]
        self.stack.append(B)

    def read_mem(self, binary_file):
        """
        Executes the READ_MEM command.

        :param binary_file: File object with the binary code.
        """
        data = binary_file.read(2)
        if len(data) < 2:
            raise ValueError("Недостаточно данных для команды READ_MEM")
        B, C = struct.unpack('<BB', data)
        self.stack.append(self.memory[B])

    def write_mem(self, binary_file):
        """
        Executes the WRITE_MEM command.

        :param binary_file: File object with the binary code.
        """
        data = binary_file.read(2)
        if len(data) < 2:
            raise ValueError("Недостаточно данных для команды WRITE_MEM")
        B, C = struct.unpack('<BB', data)
        data = self.stack.pop()
        address = data + B
        #print(data, address)
        self.memory[address] = data

    def equal(self, binary_file):
        """
        Executes the EQUAL command.

        :param binary_file: File object with the binary code.
        """
        data = binary_file.read(2)
        if len(data) < 2:
            raise ValueError("Недостаточно данных для команды EQUAL")

        B, C = struct.unpack('<BB', data)
        first = self.stack.pop()
        second = self.memory[first + B]
        print(first, second, B)
        result = int(first == second)
        print(result)

        self.stack.append(result)

    def save_memory_to_xml(self, memory_range, result_file):
        root = ET.Element("Memory")
        need = []
        for address in range(memory_range[0], memory_range[1]):
            need.append(self.create_entry(address, self.memory[address]))

        root.extend(need)
        tree = ET.ElementTree(root)
        tree.write(result_file, encoding="utf-8", xml_declaration=True)

    def create_entry(self, memory_add, memory_val):
        entry = ET.Element("memory_card")
        entry.set("address", str(memory_add))
        entry.set("value", str(memory_val))
        return entry