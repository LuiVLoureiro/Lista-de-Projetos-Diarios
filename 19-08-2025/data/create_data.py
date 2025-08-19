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
        # ts (1 Mês)
        inicio = np.datetime64("2025-01-01T00:00:00")
        fim    = np.datetime64("2025-01-31T23:59:59")
        rng = np.random.default_rng(42)
        span = int((fim - inicio) / np.timedelta64(1, "s"))
        offs = rng.integers(0, span, size=10)
        ts = inicio + offs.astype("timedelta64[s]")

        print(ts)

        # player
        nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]

        # game
        jogos = ["Dado", "Reflexo", "Memória"]

        # score 
        scores = np.random.randint(64)


bot = Criar()

bot.dados_no_csv()