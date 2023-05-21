from pathlib import Path
import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    extension = Path(file_path).suffix.lower()

    importer_mapping = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }

    importer_strategy = importer_mapping[extension]
    inventory = InventoryRefactor(importer_strategy)
    report = inventory.import_data(file_path, report_type)

    print(report, end='')


if __name__ == "__main__":
    main()
