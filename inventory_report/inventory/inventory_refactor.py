from dataclasses import dataclass, field
from typing import Union
from collections.abc import Iterable

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


@dataclass
class InventoryRefactor(Iterable):
    importer: Union[CsvImporter, JsonImporter, XmlImporter]
    data: list = field(default_factory=list)

    report_mapping = {
        "simples": SimpleReport(),
        "completo": CompleteReport(),
    }

    def import_data(self, file_path: str, report_type: str) -> str:
        list_products = self.importer.import_data(file_path)
        self.data.extend(list_products)

        report_method = self.report_mapping[report_type]

        report = report_method.generate(list_products)

        return report

    def __iter__(self):
        return InventoryIterator(self.data)
