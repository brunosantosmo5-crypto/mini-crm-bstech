📊 Mini-CRM BStech — Automação, PostgreSQL e IA

Sistema de gestão de leads (CRM) com banco de dados PostgreSQL, automação via n8n, qualificação automática por IA e relatórios em Python com pandas.

🎯 Problema

Gerenciar leads manualmente — sem histórico centralizado, sem priorização e sem follow-up automático — faz oportunidades esfriarem e se perderem. Este projeto automatiza a captura, qualificação e monitoramento de leads do início ao fim.

🧭 Como funciona
Captura — um cliente preenche um formulário (Google Forms), que alimenta uma planilha do Google Sheets.
n8n (Trigger + Postgres) — detecta a nova resposta e insere o lead no banco de dados PostgreSQL.
IA (Google Gemini) — analisa a mensagem do lead e retorna uma nota de qualificação (0-10), categoria (quente/morno/frio) e sugestão de próxima ação.
n8n (Postgres) — atualiza o registro do lead no banco com a qualificação da IA.
Alerta de follow-up — um segundo workflow roda diariamente, verificando no banco quais leads estão sem atualização há mais de 3 dias, e envia um alerta por e-mail.
Relatório semanal (Python) — um script separado, usando pandas, consulta o banco, calcula métricas (total de leads, nota média, funil por estágio) e gera um relatório em texto e um gráfico.
🛠️ Stack
Camada	Ferramenta
Orquestração	n8n
Banco de dados	PostgreSQL (Supabase)
Geração de qualificação	Google Gemini API
Análise de dados	Python (pandas, SQLAlchemy, matplotlib)
Notificação	Gmail
📂 Estrutura do repositório
mini-crm-bstech/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── workflow/
│   ├── mini-crm-captura-qualificacao.json
│   └── alerta-followup.json
├── scripts/
│   └── relatorio_crm.py
├── sql/
│   └── schema.sql
└── docs/
    └── funil_leads.png
▶️ Como rodar

Banco de dados:

Crie um projeto gratuito no Supabase.
Rode o conteúdo de sql/schema.sql no SQL Editor para criar as tabelas.
Use a connection string do Session Pooler (não a conexão direta — hosts diretos do Supabase costumam falhar em ambientes sem suporte a IPv6, incluindo o n8n cloud).

Workflows do n8n:

Importe os dois arquivos de workflow/ no seu n8n.
Configure suas credenciais (Google Sheets, Postgres, Google Gemini, Gmail).
Publique os dois workflows.

Script de relatório:

Instale as dependências:
bash
   pip install -r requirements.txt
Copie .env.example para .env e preencha com os dados reais do seu banco.
Rode:
bash
   python scripts/relatorio_crm.py
📋 Exemplo de saída do relatório
Relatório Semanal - CRM BStech
Total de leads: 5
Nota média de qualificação: 7.2
Leads quentes (nota >= 8): 2

Distribuição por estágio:
Novo Lead    5
🚧 Possíveis melhorias futuras
Fluxo de aprovação/interação humana antes de mudar o estágio do lead
Dashboard visual (ex: Streamlit) em vez de relatório em texto
Agendamento automático do script de relatório (cron)
Testes automatizados para o script Python
📄 Licença

Este projeto é livre para uso e estudo (MIT License).
