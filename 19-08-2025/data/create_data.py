import numpy as np
import pandas as pd
import os


class Criar():
    def __init__(self):
        pass

    def arquivo_csv(self, nome=""):
        try:
            dir_atual = os.path.dirname(os.path.abspath(__file__))
            df = pd.DataFrame({
                'ts': [],
                'player': [],
                'game': [],
                'score': [],
            })
            df.to_csv(f"{dir_atual}/{nome}.csv", index=False)
            print(f"sucess: Criação do {nome}.csv foi feita com sucesso")
        except:
            print(f"error: Erro na Criação do Arquivo {nome}.csv")
    def dados_no_csv(self):
        pass


bot = Criar()

bot.arquivo_csv("arcade")