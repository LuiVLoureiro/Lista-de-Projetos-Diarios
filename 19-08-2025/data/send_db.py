from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

caminho = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(caminho, "arcade.db")

db = create_engine(f"sqlite:///{caminho_db}")
Sessao = sessionmaker(bind=db)
sessao = Sessao()

Base = declarative_base()

Base.metadata.create_all(bind=db)