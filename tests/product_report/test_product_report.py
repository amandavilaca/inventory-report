from inventory_report.inventory.product import Product


def test_relatorio_produto():
    actual_product = Product(
        id="2",
        nome_do_produto="fentanyl citrate",
        nome_da_empresa="Target Corporation",
        data_de_fabricacao="2020-12-06",
        data_de_validade="2023-12-25",
        numero_de_serie="FR29 5951 7573 74OY XKGX 6CSG D20",
        instrucoes_de_armazenamento="instrucao 2",
    )

    expected_product = (
        "O produto fentanyl citrate fabricado em 2020-12-06 "
        "por Target Corporation com validade até 2023-12-25 "
        "precisa ser armazenado instrucao 2."
    )

    assert repr(actual_product) == expected_product
