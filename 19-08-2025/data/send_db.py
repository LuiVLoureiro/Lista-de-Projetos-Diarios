from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
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