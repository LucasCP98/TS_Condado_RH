import pandas as pd


def dados_loguin_senha(self):
    # Lendo os dados do arquivo.csv.
    dados = pd.read_csv("../Data/senha_password_produtos.csv")

    # Dados da Tabela.
    login = dados["login"].values
    senha = dados["senha"].values
    adicionar_ao_carrinho_os_itens = dados["adicionar_ao_carrinho_os_itens"].values

    return login, senha, adicionar_ao_carrinho_os_itens
