from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey, Float, Text, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import pandas as pd
from datetime import datetime
import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(caminho, "arcade.db")

db = create_engine(f"sqlite:///{caminho_db}")
Sessao = sessionmaker(bind=db)
sessao = Sessao()

Base = declarative_base()

# Classes
class Partida(Base):
    __tablename__ = "partida"
    id_partida = Column("id_partida", Integer, primary_key=True, autoincrement=True)
    datetime = Column("ts", DateTime)
    id_jogador = Column("id_jogador", Integer, ForeignKey("jogadores.id_jogador"), nullable=False)
    id_jogo = Column("id_jogo", Integer, ForeignKey("jogos.id_jogo"), nullable=False)
    score = Column("score", Float)

    jogador = relationship("Jogadores", back_populates="partida")
    jogo = relationship("Jogos", back_populates="partida")

class Jogadores(Base):
    __tablename__ = "jogadores"
    id_jogador = Column("id_jogador", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", Text)

    partida = relationship("Partida", back_populates="jogadores")

class Jogos(Base):
    __tablename__ = "jogos"
    id_jogo = Column("id_jogo", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", Text)

    partida = relationship("Partida", back_populates="jogos")

Base.metadata.create_all(bind=db)

# Registrar do Arquivo arcade.csv

df = pd.read_csv(os.path.join(caminho, "arcade.csv"), parse_dates=["ts"])
df = df.dropna(subset=["ts", "player", "game", "score"]).drop_duplicates()
with db.begin() as conn:
    id_por_jogador = {}
    for nome in df["player"].unique():
        row = conn.execute(
            text("SELECT id_jogador FROM jogadores WHERE nome = :n LIMIT 1"),
            {"n": nome}
        ).fetchone()
        if row is None:
            conn.execute(text("INSERT INTO jogadores (nome) VALUES (:n)"), {"n": nome})
            row = conn.execute(
                text("SELECT id_jogador FROM jogadores WHERE nome = :n LIMIT 1"),
                {"n": nome}
            ).fetchone()
        id_por_jogador[nome] = row[0]

    id_por_jogo = {}
    for nome in df["game"].unique():
        row = conn.execute(
            text("SELECT id_jogo FROM jogos WHERE nome = :n LIMIT 1"),
            {"n": nome}
        ).fetchone()
        if row is None:
            conn.execute(text("INSERT INTO jogos (nome) VALUES (:n)"), {"n": nome})
            row = conn.execute(
                text("SELECT id_jogo FROM jogos WHERE nome = :n LIMIT 1"),
                {"n": nome}
            ).fetchone()
        id_por_jogo[nome] = row[0]

    ins_sql = text(
        "INSERT INTO partida (ts, id_jogador, id_jogo, score) "
        "VALUES (:ts, :id_jogador, :id_jogo, :score)"
    )

    for _, r in df.iterrows():
        ts_py = r["ts"].to_pydatetime() if isinstance(r["ts"], pd.Timestamp) else datetime.fromisoformat(r["ts"])
        conn.execute(
            ins_sql,
            {
                "ts": ts_py,
                "id_jogador": id_por_jogador[r["player"]],
                "id_jogo": id_por_jogo[r["game"]],
                "score": float(r["score"]),
            }
        )

sessao.close()