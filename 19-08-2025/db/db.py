from sqlalchemy import create_engine, DateTime, Column, String, Integer, Float, Enum, Boolean, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Juntar Caminhos para a Pasta Atual
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_database = os.path.join(diretorio, "pulse.db")

# Criar Database
db = create_engine(f"sqlite:///{caminho_database}")
Sessao = sessionmaker(bind=db)
sessao = Sessao()
Base = declarative_base()

# Tabelas

class Sessoes(Base): 
    __tablename__ = "sessoes"
    id =  Column("id", Integer, primary_key=True, autoincrement=True)
    start_ts = Column("start_ts", DateTime)
    end_ts = Column("end_ts", DateTime)
    duration_min = Column("duration_min", Float)
    category = Column("category", String)
    focus_score = Column("focus_score", Integer)
    mood_score = Column("mood_score", Integer)
    interruption = Column("interruption", Integer)
    sleep_hours_prev = Column("sleep_hours_prev", Float)
    caffeine_mg = Column("caffeine_mg", Integer)
    temperature_c = Column("temperature_c", Float)
    room_temp_label = Column("room_temp_label", Enum)
    window_open = Column("window_open", Boolean)
    notes = Column("notes", Text)

    def __init__(self, id, start_ts, end_ts, duration_min, category, focus_score, mood_score, interruption
                , sleep_hours_prev, caffeine_mg, temperature_c, room_temp_label, window_open, notes):
        
        self.id = id
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.duration_min = duration_min
        self.category = category
        self.focus_score = focus_score
        self.mood_score = mood_score
        self.interruption = interruption
        self.sleep_hours_prev = sleep_hours_prev
        self.caffeine_mg = caffeine_mg
        self.temperature_c = temperature_c
        self.room_temp_label = room_temp_label
        self.window_open = window_open
        self.notes = notes
        


Base.metadata.create_all(bind=db)