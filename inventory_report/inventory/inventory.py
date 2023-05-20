import csv
import json
from typing import List
from pathlib import Path
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".csv":
            products = Inventory.read_csv(file_path)
        elif extension == ".json":
            products = Inventory.read_json(file_path)
        else:
            raise ValueError("Formato de arquivo inválido")

        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError("O tipo de relatório fornecido não é válido")

    def read_csv(file_path: str) -> List[dict]:

        data = list()
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def read_json(file_path: str) -> List[dict]:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
