from pathlib import Path

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:

        extension = Path(file_path).suffix.lower()

        importer_mapping = {
            ".csv": CsvImporter,
            ".json": JsonImporter,
            ".xml": XmlImporter,
        }

        report_mapping = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        if extension not in importer_mapping:
            raise ValueError("Formato de arquivo inválido")

        if report_type not in report_mapping:
            raise ValueError("Tipo de relatório inválido")

        importer_strategy = importer_mapping[extension]()

        products = importer_strategy.import_data(file_path)

        report_method = report_mapping[report_type]
        return report_method(products)
