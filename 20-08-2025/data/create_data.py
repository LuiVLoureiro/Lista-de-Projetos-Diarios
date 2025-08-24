import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
inicio = np.datetime64("2025-01-01T00:00:00")
fim = np.datetime64("2025-01-07T00:00:00")
span_seg = int((fim - inicio) / np.timedelta64(1, 's'))
n = 50
off = rng.integers(0, span_seg, size=n)
timestamps = inicio + off.astype('timedelta64[s]')





# ts	DATETIME	data/hora do consumo
# ml	INTEGER	volume em mililitros (>0)
# contexto	TEXT	manhã/tarde/noite/pós-treino, etc.
# ETL. data.csv → Pandas (valida ml>0, parse ts) → SQLite via SQLAlchemy.


