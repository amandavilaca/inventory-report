from datetime import datetime
from collections import Counter
from typing import Dict, List


class SimpleReport:
    @staticmethod
    def generate(products: List[Dict]) -> str:

        today_date = datetime.today().date()
        manufacturing_dates = list()
        expiration_dates = list()
        companies = list()

        for product in products:
            if product.get('data_de_fabricacao'):
                manufacturing_dates.append(product['data_de_fabricacao'])
            if product.get('data_de_validade') and (
                product['data_de_validade'] >= str(today_date)
            ):
                expiration_dates.append(product['data_de_validade'])
            if product.get('nome_da_empresa'):
                companies.append(product['nome_da_empresa'])

        oldest_date = min(manufacturing_dates, default=None)
        closest_date = min(expiration_dates, default=None)
        company_bigger_stock = Counter(companies).most_common(1)[0][0]

        output = f"Data de fabricação mais antiga: {oldest_date}\n"
        output += f"Data de validade mais próxima: {closest_date}\n"
        output += f"Empresa com mais produtos: {company_bigger_stock}"

        return output
