## Projetos Diários — 19/08 a 31/08

Série de 13 micro-projetos em Python (um por dia) para treinar **ETL (CSV → SQLite via SQLAlchemy), análise com Pandas/NumPy, gráficos com Matplotlib** e **estatística descritiva**.
O primeiro projeto (19/08) é o **Pulse**. De 20/08 a 31/08, os temas são mais simples e independentes.

### Stack

* Python 3.13+
* NumPy, Pandas, Matplotlib
* SQLAlchemy + SQLite
* (Opcional) Jupyter Notebook

### Estrutura

```
PROJETOS_DIARIOS_PYTHON/
├─ 19-08-2025/              # Pulse
├─ 20-08-2025/              # Hydra
├─ 21-08-2025/              # SpendLite
├─ 22-08-2025/              # MoveCount
├─ 23-08-2025/              # SleepSketch
├─ 24-08-2025/              # TaskTally
├─ 25-08-2025/              # FoodMood (lite)
├─ 26-08-2025/              # Ambient
├─ 27-08-2025/              # ReadRate
├─ 28-08-2025/              # FitBits (caseiro)
├─ 29-08-2025/              # SoundFocus
├─ 30-08-2025/              # CaffTrack
├─ 31-08-2025/              # HabitScore
└─ README.md                # este arquivo
```

Cada pasta do dia segue este **template**:

```
YYYY-MM-DD_TEMA/
├─ data.csv                 # dados brutos (entrada)
├─ models.py                # modelos SQLAlchemy (1 tabela simples)
├─ etl.py                   # CSV -> validação/transform -> SQLite
├─ analysis.ipynb (ou .py)  # análises e gráficos
└─ figs/                    # .png exportados
```

### Fluxo de trabalho (branches)

* Criar branch: `git checkout -b feat/2025-08-20-hydra`
* Entregar: push + PR para `main`
* Padrão de commit: `ftr: ...`, `fix: ...`, `docs: ...`, `chore: ...`

### Critérios gerais (para recrutadores)

* **ETL limpo** (tipagem, datas, missing, ranges).
* **Métricas claras** (média, desvio, frequências) + 1 correlação/regressão simples (NumPy).
* **Visualizações objetivas** (2 gráficos por projeto).
* **Reprodutibilidade**: scripts rodam com `python etl.py` e `python analysis.py` (ou notebook).
* **Documentação enxuta**: problema, dados, análises, gráficos, conclusão rápida.

---

# 20/08 — Hydra: Hidratação Diária

**Ideia.** Registrar copos de água e horários para entender padrão de hidratação.

**Esquema (tabela única).**

| coluna   | tipo     | descrição                          |
| -------- | -------- | ---------------------------------- |
| id       | INTEGER  | PK                                 |
| ts       | DATETIME | data/hora do consumo               |
| ml       | INTEGER  | volume em mililitros (>0)          |
| contexto | TEXT     | manhã/tarde/noite/pós-treino, etc. |

**ETL.** `data.csv` → Pandas (valida `ml>0`, parse `ts`) → SQLite via SQLAlchemy.

**Análises & Métricas.**

* Total diário e média por **faixa horária**.
* Distribuição de volumes (hist).
* Correlação simples: **nº de eventos** × **total diário** (NumPy).

**Visualizações.**

* Barras: consumo por hora do dia.
* Linha: acumulado diário (curva de hidratação).

**Entregáveis.**

* `hydra.db`, 2 gráficos `.png`, breve conclusão (melhor janela do dia).

---

# 21/08 — SpendLite: Micro-Despesas do Dia

**Ideia.** Mapear pequenos gastos e “vazamentos” de orçamento.

**Esquema.**

| coluna    | tipo     | descrição                   |
| --------- | -------- | --------------------------- |
| id        | INTEGER  | PK                          |
| ts        | DATETIME | data/hora da despesa        |
| valor     | REAL     | valor positivo              |
| categoria | TEXT     | alimentação/transporte/etc. |

**ETL.** Normaliza decimais, valida `valor>0`, grava em SQLite.

**Análises & Métricas.**

* Soma diária, **ticket médio**, top categorias.
* **Média móvel** (3 dias) com NumPy.

**Visualizações.**

* Pizza: % por categoria.
* Linha: gastos/dia + média móvel.

**Entregáveis.**

* `spendlite.db`, 2 gráficos `.png`, insights rápidos por categoria.

---

# 22/08 — MoveCount: Passos & Pausas (lite)

**Ideia.** Log de caminhadas/alongamentos para ver horários mais ativos.

**Esquema.**

| coluna      | tipo     | descrição                        |
| ----------- | -------- | -------------------------------- |
| id          | INTEGER  | PK                               |
| inicio      | DATETIME | início do bloco                  |
| fim         | DATETIME | fim do bloco                     |
| passos\_est | INTEGER  | passos estimados (>=0)           |
| tipo        | TEXT     | caminhada curta/alongamento/etc. |

**ETL.** Calcula `duracao_min`, valida tempos.

**Análises & Métricas.**

* Duração média por tipo; passos/hora.
* Probabilidade de pausa por faixa horária.

**Visualizações.**

* Barras: duração média por tipo.
* Linha: passos por hora do dia.

**Entregáveis.**

* `movecount.db`, 2 gráficos `.png`, recomendação de horário.

---

# 23/08 — SleepSketch: Sono Simplificado

**Ideia.** Deitar/levantar + qualidade (1–5) para ver padrões.

**Esquema.**

| coluna    | tipo     | descrição        |
| --------- | -------- | ---------------- |
| id        | INTEGER  | PK               |
| deitar    | DATETIME | hora de deitar   |
| levantar  | DATETIME | hora de levantar |
| qualidade | INTEGER  | 1–5              |

**ETL.** Calcula `horas_sono` (diferenca em horas), valida faixa 0–16h.

**Análises & Métricas.**

* Média/variância de `horas_sono`.
* Correlação (NumPy): `horas_sono` × `qualidade`.
* Outliers via **z-score** (NumPy).

**Visualizações.**

* Hist: horas de sono.
* Linha: qualidade (média móvel).

**Entregáveis.**

* `sleepsketch.db`, 2 gráficos `.png`, insight sobre duração ótima.

---

# 24/08 — TaskTally: Pomodoros Simples

**Ideia.** Quantos blocos de foco por tarefa/dia e taxa de conclusão.

**Esquema.**

| coluna     | tipo     | descrição       |
| ---------- | -------- | --------------- |
| id         | INTEGER  | PK              |
| ts\_inicio | DATETIME | início do bloco |
| ts\_fim    | DATETIME | fim do bloco    |
| tarefa     | TEXT     | nome/tema       |
| concluido  | BOOLEAN  | 0/1             |

**ETL.** Calcula `dur_min`, valida 15–60 min.

**Análises & Métricas.**

* Pomodoros/dia; **taxa de conclusão**.
* *Control chart* simples: média ± 1 desvio (NumPy).

**Visualizações.**

* Barras: pomodoros/dia (empilhado concluído vs não).
* Linha: throughput diário.

**Entregáveis.**

* `tasktally.db`, 2 gráficos `.png`, conclusão de produtividade.

---

# 25/08 — FoodMood (lite): Refeição & Energia

**Ideia.** Tipo de refeição e energia 30–60 min depois (1–5).

**Esquema.**

| coluna       | tipo     | descrição           |
| ------------ | -------- | ------------------- |
| id           | INTEGER  | PK                  |
| ts           | DATETIME | horário da refeição |
| tipo         | TEXT     | leve/média/pesada   |
| energia\_pos | INTEGER  | 1–5                 |

**ETL.** Normaliza categorias e valida escala 1–5.

**Análises & Métricas.**

* Energia média por tipo; distribuição por horário.
* Tabela de contingência e **qui-quadrado** (implementado com Pandas/NumPy) para “tipo” vs “alta energia (≥4)”.

**Visualizações.**

* Barras: energia média por tipo.
* Boxplot: energia por tipo (opcional).

**Entregáveis.**

* `foodmood.db`, 2 gráficos `.png`, recomendação de tipos/horários.

---

# 26/08 — Ambient: Clima & Conforto (manual)

**Ideia.** Relacionar temperatura/umidade com conforto (1–5).

**Esquema.**

| coluna   | tipo     | descrição        |
| -------- | -------- | ---------------- |
| id       | INTEGER  | PK               |
| ts       | DATETIME | medição          |
| temp\_c  | REAL     | temperatura (°C) |
| umid     | REAL     | umidade (%)      |
| conforto | INTEGER  | 1–5              |

**ETL.** Valida ranges (ex.: 10–40°C; 10–100%); trata missing.

**Análises & Métricas.**

* Correlações NumPy: `temp↔conforto`, `umid↔conforto`.
* Regressão linear simples `conforto ~ temp` (coef e R² manual).

**Visualizações.**

* Dispersão com linha de regressão.
* Heatmap 2D (binning NumPy) `temp × umid`.

**Entregáveis.**

* `ambient.db`, 2 gráficos `.png`, faixa ótima de conforto.

---

# 27/08 — ReadRate: Páginas & Ritmo de Leitura

**Ideia.** Páginas por sessão e **ritmo** (páginas/hora).

**Esquema.**

| coluna  | tipo     | descrição          |
| ------- | -------- | ------------------ |
| id      | INTEGER  | PK                 |
| inicio  | DATETIME | início da sessão   |
| fim     | DATETIME | fim da sessão      |
| paginas | INTEGER  | páginas lidas (≥0) |
| obra    | TEXT     | livro/artigo       |

**ETL.** Calcula `ritmo_ph = paginas / horas`.

**Análises & Métricas.**

* Ritmo médio; melhores horários.
* Regressão polinomial (NumPy `polyfit grau 2`): `ritmo ~ hora`.

**Visualizações.**

* Linha: ritmo ao longo do dia.
* Hist: páginas por sessão.

**Entregáveis.**

* `readrate.db`, 2 gráficos `.png`, dica de janela ótima.

---

# 28/08 — FitBits (caseiro): Reps & Tempo

**Ideia.** Micro-exercícios (flexões, prancha, alongamento).

**Esquema.**

| coluna   | tipo     | descrição                  |
| -------- | -------- | -------------------------- |
| id       | INTEGER  | PK                         |
| ts       | DATETIME | horário                    |
| tipo     | TEXT     | flexão/prancha/alongamento |
| reps     | INTEGER  | repetições (≥0)            |
| dur\_seg | INTEGER  | duração em segundos (≥0)   |

**ETL.** Normaliza reps/duração e infere “carga”.

**Análises & Métricas.**

* Média de reps por tipo; total/dia.
* Z-score para comparar esforço entre tipos.

**Visualizações.**

* Barras: reps por tipo/dia.
* Linha: total diário (média móvel).

**Entregáveis.**

* `fitbits.db`, 2 gráficos `.png`, evolução de consistência.

---

# 29/08 — SoundFocus: Música vs Concentração

**Ideia.** Ambiente sonoro (silêncio/lo-fi/pop/…) vs foco (1–5).

**Esquema.**

| coluna   | tipo     | descrição               |
| -------- | -------- | ----------------------- |
| id       | INTEGER  | PK                      |
| ts       | DATETIME | registro                |
| ambiente | TEXT     | silêncio/lo-fi/pop/etc. |
| foco     | INTEGER  | 1–5                     |

**ETL.** Padroniza categorias e valida escala.

**Análises & Métricas.**

* Foco médio e variância por ambiente.
* **Bootstrap** (NumPy, 1000 amostras) da diferença de médias (top2 ambientes).

**Visualizações.**

* Barras: foco médio (com erro padrão).
* Distribuição: hist ou box por ambiente.

**Entregáveis.**

* `soundfocus.db`, 2 gráficos `.png`, recomendação de trilha.

---

# 30/08 — CaffTrack: Cafeína Simples

**Ideia.** Bebidas cafeinadas e “alerta” após 30 min (1–5).

**Esquema.**

| coluna   | tipo     | descrição                |
| -------- | -------- | ------------------------ |
| id       | INTEGER  | PK                       |
| ts       | DATETIME | ingestão                 |
| bebida   | TEXT     | café/chá/energético/etc. |
| dose\_mg | INTEGER  | cafeína estimada (mg)    |
| alerta   | INTEGER  | 1–5                      |

**ETL.** Mapa de bebidas → dose padrão (pode sobrescrever manualmente).

**Análises & Métricas.**

* Correlação: `dose_mg × alerta`.
* Ajuste linear `alerta ~ dose_mg` e R² manual.

**Visualizações.**

* Dispersão: dose vs alerta (+ linha de tendência).
* Barras: alerta médio por bebida.

**Entregáveis.**

* `cafftrack.db`, 2 gráficos `.png`, *dose sweet spot*.

---

# 31/08 — HabitScore: Mini-Hábitos & Score Único

**Ideia.** 3–5 hábitos binários/dia (ex.: 2L água, caminhar, 1h estudo, sono ≥7h).
Criar **score** 0–100 ponderado.

**Esquema.**

| coluna        | tipo | descrição |
| ------------- | ---- | --------- |
| id            | INT  | PK        |
| data          | DATE | dia       |
| agua\_ok      | BOOL | 0/1       |
| caminhada\_ok | BOOL | 0/1       |
| estudo\_ok    | BOOL | 0/1       |
| sono\_ok      | BOOL | 0/1       |

**ETL.** Mapear BOOL→{0,1}; **weights** NumPy (ex.: `[0.3,0.2,0.3,0.2]`).

**Análises & Métricas.**

* Score diário; dias “verdes” (≥80).
* Matriz de correlação entre hábitos (Pandas/NumPy).

**Visualizações.**

* Linha: score diário (média móvel).
* Barras empilhadas: hábitos cumpridos por dia.

**Entregáveis.**

* `habitscore.db`, 2 gráficos `.png`, *dashboard* resumo.

---

## Observações finais (para recrutadores)

* Cada projeto isola um **problema simples**, aplica **ETL** robusto, **análises estatísticas básicas** e **visualizações** claras.
* O conjunto demonstra **consistência**, **boas práticas de dados** e **capacidade de experimentar rapidamente** hipóteses com Python.
* O último dia consolida o padrão em um score interpretável, favorecendo **decisão orientada a dados**.

