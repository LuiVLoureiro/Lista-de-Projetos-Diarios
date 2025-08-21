import numpy as np
import pandas as pd
import os

class Criar():
    def __init__(self):
        pass

    def gerar_dados_no_csv(self):
        try:
            dir_atual = os.path.dirname(os.path.abspath(__file__))
            df = pd.DataFrame({
                'ts': [],
                'player': [],
                'game': [],
                'score': [],
            })
            df.to_csv(f"{dir_atual}/arcade.csv", index=False)
            print(f"sucess: Criação do arcade.csv foi feita com sucesso")
        except:
            print(f"error: Erro na Criação do Arquivo arcade.csv")

        nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
        jogos = ["Reflexo", "Memória"]

        arquivo = os.path.dirname(os.path.abspath(__file__))
        arquivo = os.path.join(arquivo, "arcade.csv")

        base = np.datetime64("2025-01-01T00:00:00")
        
        dias = 7
        for nome in nomes:
            for dia in range(dias):
                # Timestamp
                inicio = base + np.timedelta64(dia, "D")
                fim    = inicio + np.timedelta64(23, "h") + np.timedelta64(59, "m") + np.timedelta64(59, "s")
                rng = np.random.default_rng()
                span = int((fim - inicio) / np.timedelta64(1, "s"))
                offs = rng.integers(0, span, size=1)
                ts = inicio + offs.astype("timedelta64[s]")
                iso = np.datetime_as_string(ts, unit="s")
                for i in range(np.random.randint(3, 6)): # De 3 a 6 partidas por jogador alternando entre os jogos
                    # Escolher Jogo
                    jogo = np.random.choice(jogos)
                    if jogo == "Reflexo":
                        score = self.jogo_reflexo()
                    elif jogo == "Memória":
                        score = self.jogo_memoria()

                    # Salvar Dataframe
                    df = pd.DataFrame({
                        'ts': [iso],
                        'player': [nome],
                        'game': [jogo],
                        'score': [score]
                        })

                    df.to_csv(arquivo, mode="a", index=False, header=not arquivo)


    def jogo_reflexo(self):
        pares_acertados = np.random.randint(0, 10)
        score = pares_acertados * 10
        return float(score)

    def jogo_memoria(self):
        tempo_total_ms = np.random.randint(0, 500)
        score = 500 - (tempo_total_ms/10)
        return float(score)


bot = Criar()

bot.gerar_dados_no_csv()