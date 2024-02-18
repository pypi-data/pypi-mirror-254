import pandas as pd


class Planilhas:

    """Classe para criação de planilhas e manipulação de planilhas"""

    # Leitura da planilha
    def __init__(self, nome_planilha):
        self.nome_planilha = nome_planilha
        self.leitura_planilha = pd.read_excel(self.nome_planilha)

    # Listando valores de uma coluna
    def listando_valores(self, n_coluna):
        return self.leitura_planilha[n_coluna].tolist()

    @staticmethod
    # Criando dataframe para escrever na planilha
    def armazenando_dataframe(nome_coluna1='', lista_1=[], nome_coluna2='', lista_2=[], nome_planilha=''):
        dados = pd.DataFrame({nome_coluna1: lista_1, nome_coluna2: lista_2})
        return dados.to_excel(f'{nome_planilha}.xlsx', index=False)

