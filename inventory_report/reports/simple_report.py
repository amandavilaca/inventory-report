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

            manufacturing_date = product.get('data_de_fabricacao')
            expiration_date = product.get('data_de_validade')
            expiration_date_obj = datetime.strptime(expiration_date,
                                                    '%Y-%m-%d').date()
            company = product.get('nome_da_empresa')

            manufacturing_dates.append(manufacturing_date)
            if expiration_date_obj >= today_date:
                expiration_dates.append(expiration_date_obj)
            companies.append(company)

            oldest_date = min(manufacturing_dates, default=None)
            closest_date = min(expiration_dates, default=None)
            company_bigger_stock = Counter(companies).most_common(1)[0][0]

            output = f"Data de fabricação mais antiga: {oldest_date}\n"
            output += f"Data de validade mais próxima: {closest_date}\n"
            output += f"Empresa com mais produtos: {company_bigger_stock}"

        return output
