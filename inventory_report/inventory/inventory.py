import csv
import json
from typing import List
from pathlib import Path
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:

        extension = Path(file_path).suffix.lower()

        extension_mapping = {
             ".csv": Inventory.read_csv,
             ".json": Inventory.read_json,
             ".xml": Inventory.read_xml,
        }

        report_type_mapping = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        if extension not in extension_mapping:
            raise ValueError("Formato de arquivo inválido")

        if report_type not in report_type_mapping:
            raise ValueError("Tipo de relatório inválido")

        reader_method = extension_mapping[extension]
        products = reader_method(file_path)

        report_method = report_type_mapping[report_type]
        return report_method(products)

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

    def read_xml(file_path: str) -> List[dict]:
        # Fonte: https://docs.python.org/3/library/xml.etree.elementtree.html
        fields = ["id", "nome_do_produto", "nome_da_empresa",
                  "data_de_fabricacao", "data_de_validade", "numero_de_serie",
                  "instrucoes_de_armazenamento"]

        tree = ET.parse(file_path)
        root = tree.getroot()

        data = list()

        for record in root.findall("record"):
            product = dict()
            for field in fields:
                product[field] = record.find(field).text
            data.append(product)
        return data
