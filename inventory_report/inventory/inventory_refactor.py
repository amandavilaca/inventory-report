from typing import Type
from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Type):
        self.importer = importer
        self.data = list()

    def import_data(self, file_path: str, report_type: str):

        report_mapping = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        products = self.importer.import_data(file_path)
        self.data.extend(products)

        report_method = report_mapping[report_type]
        return report_method(products)

    def __iter__(self):
        return InventoryIterator(self.data)
