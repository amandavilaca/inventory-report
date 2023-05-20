from typing import Dict, List
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products: List[Dict]) -> str:
        simple_report = SimpleReport.generate(products)

        companies = [product['nome_da_empresa']
                     for product in products
                     if product.get('nome_da_empresa')]

        companies_stock_counts = Counter(companies)

        complete_report = "\nProdutos estocados por empresa:\n"
        for company, count in companies_stock_counts.items():
            complete_report += f"- {company}: {count}\n"
        output = simple_report + complete_report
        return output
