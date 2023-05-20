import csv
from typing import List
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:

        products = Inventory.read_csv(file_path)

        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError("O tipo de relatório fornecido não é válido")

    def read_csv(file_path: str) -> List[dict]:

        products = list()
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products
