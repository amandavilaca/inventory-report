import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str) -> list[dict]:
        if not file_path.lower().endswith('.csv'):
            raise ValueError("Arquivo inválido")

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
