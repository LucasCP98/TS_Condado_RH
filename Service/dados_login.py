import pandas as pd


def dados_loguin_senha(self):
    # Lendo os dados do arquivo.csv.
    dados = pd.read_csv("../Data/senha_password.csv")

    # Dados da Tabela.
    login = dados["login"]
    senha = dados["senha"]

    return login, senha

