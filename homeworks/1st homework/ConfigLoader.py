import xml.etree.ElementTree as ET

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.tree = ET.parse(config_path)
        self.root = self.tree.getroot()

    def get_zip_path(self):
        return self.root.find('file_system').find("path").text

    def get_start_script(self):
        return self.root.find('startup_script').find("path").text