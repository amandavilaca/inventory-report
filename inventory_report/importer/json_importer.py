import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str) -> list[dict]:
        if not file_path.lower().endswith('.json'):
            raise ValueError("Arquivo inválido")

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
