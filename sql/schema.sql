CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    empresa TEXT,
    mensagem TEXT,
    estagio TEXT DEFAULT 'Novo Lead',
    nota_qualificacao INTEGER,
    proxima_acao TEXT,
    criado_em TIMESTAMP DEFAULT NOW(),
    atualizado_em TIMESTAMP DEFAULT NOW()
);

CREATE TABLE interacoes (
    id SERIAL PRIMARY KEY,
    lead_id INTEGER REFERENCES leads(id),
    tipo TEXT,
    descricao TEXT,
    criado_em TIMESTAMP DEFAULT NOW()
);
