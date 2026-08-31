import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import matplotlib.pyplot as plt
from datetime import datetime
# Conexão com o Supabase (Session Pooler) - preencha com seus dados reais
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
)
engine = create_engine(db_url, connect_args={"sslmode": "require"})

# Carrega os leads num DataFrame do pandas
df = pd.read_sql("SELECT * FROM leads", engine)

# Métricas
total_leads = len(df)
por_estagio = df["estagio"].value_counts()
nota_media = df["nota_qualificacao"].mean()
leads_quentes = df[df["nota_qualificacao"] >= 8]

# Gráfico simples de funil
por_estagio.plot(kind="bar", title="Leads por estágio")
plt.tight_layout()
plt.savefig("funil_leads.png")

# Relatório em texto
relatorio = f"""
Relatório Semanal - CRM BStech
Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}

Total de leads: {total_leads}
Nota média de qualificação: {nota_media:.1f}
Leads quentes (nota >= 8): {len(leads_quentes)}

Distribuição por estágio:
{por_estagio.to_string()}
"""

print(relatorio)

with open("relatorio_semanal.txt", "w", encoding="utf-8") as f:
    f.write(relatorio)