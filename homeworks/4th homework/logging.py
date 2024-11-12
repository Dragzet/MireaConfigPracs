import xml.etree.ElementTree as ET


def create_log_entry(command, args, binary_instruction):
    """
    Создает XML-запись лога для инструкции.

    :param command: Имя команды.
    :param args: Аргументы команды.
    :param binary_instruction: Бинарное представление инструкции.
    :return: Объект XML Element.
    """
    entry = ET.Element("instruction")
    entry.set("command", command)
    entry.set("binary", binary_instruction.hex())

    for i, arg in enumerate(args):
        arg_elem = ET.SubElement(entry, f"arg{i}")
        arg_elem.text = str(arg)

    return entry


def save_log_to_file(log_entries, log_path):
    """
    Сохраняет все записи лога в XML-файл.

    :param log_entries: Список объектов Element с записями инструкций.
    :param log_path: Путь к файлу лога.
    """
    root = ET.Element("log")
    root.extend(log_entries)
    tree = ET.ElementTree(root)
    tree.write(log_path, encoding="utf-8", xml_declaration=True)
