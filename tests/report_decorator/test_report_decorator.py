import re
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

products_mock = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-12-22",
        "data_de_validade": "2024-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    },
    {
        "id": "4",
        "nome_do_produto": "Norepinephrine Bitartrate",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2020-12-24",
        "data_de_validade": "2025-08-19",
        "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
        "instrucoes_de_armazenamento": "instrucao 4",
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2021-04-14",
        "data_de_validade": "2025-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5",
    }]


def test_decorar_relatorio():

    green_phrases = [
        "Data de fabricação mais antiga:",
        "Data de validade mais próxima:",
        "Empresa com mais produtos:",
    ]

    date_regex = r"\033\[36m\d{4}-\d{2}-\d{2}\033\[0m"
    company_regex = r"\033\[31m([^:]+)\033\[0m"

    simple_report = SimpleReport()
    complete_report = CompleteReport()

    colored_simple_report = ColoredReport(simple_report)
    colored_complete_report = ColoredReport(complete_report)

    decorated_simple_report = colored_simple_report.generate(products_mock)
    decorated_complete_report = colored_complete_report.generate(products_mock)

    for phrase in green_phrases:
        assert f"\033[32m{phrase}\033[0m" in decorated_simple_report
        assert f"\033[32m{phrase}\033[0m" in decorated_complete_report

    assert re.search(date_regex, decorated_simple_report) is not None
    assert re.search(date_regex, decorated_complete_report) is not None

    assert re.search(company_regex, decorated_simple_report) is not None
    assert re.search(company_regex, decorated_complete_report) is not None
