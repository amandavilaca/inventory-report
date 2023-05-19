from unittest import TestCase
from inventory_report.inventory.product import Product


def test_cria_produto():

    excepted_attributes_and_types = {
        "id": int,
        "nome_da_empresa": str,
        "nome_do_produto": str,
        "data_de_fabricacao": str,
        "data_de_validade": str,
        "numero_de_serie": str,
        "instrucoes_de_armazenamento": str,
        }

    product_mock = dict(
            id=1,
            nome_do_produto="Nicotine Polacrilex",
            nome_da_empresa="Target Corporation",
            data_de_fabricacao="2021-02-18",
            data_de_validade="2023-09-17",
            numero_de_serie="CR25 1551 4467 2549 4402 1",
            instrucoes_de_armazenamento="instrucao 1",
        )

    product = Product(
        id=product_mock['id'],
        nome_do_produto=product_mock['nome_do_produto'],
        nome_da_empresa=product_mock['nome_da_empresa'],
        data_de_fabricacao=product_mock['data_de_fabricacao'],
        data_de_validade=product_mock['data_de_validade'],
        numero_de_serie=product_mock['numero_de_serie'],
        instrucoes_de_armazenamento=product_mock
        ['instrucoes_de_armazenamento'],
        )

    for attribute, type in excepted_attributes_and_types.items():
        actual_value = getattr(product, attribute)
        expected_value = (product_mock[attribute])

        TestCase().assertEqual(actual_value, expected_value)
        TestCase().assertIsInstance(actual_value, type)
