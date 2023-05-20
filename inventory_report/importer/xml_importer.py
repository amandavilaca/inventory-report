import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str) -> list[dict]:
        if not file_path.lower().endswith('xml'):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_path)
        root = tree.getroot()

        data = list()

        for record in root.findall("record"):
            product = {}
            for field in record:
                product[field.tag] = field.text
            data.append(product)
        return data
