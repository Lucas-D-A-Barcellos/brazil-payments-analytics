# Análise de Pix e outros Meios de Pagamentos no Brasil

Projeto de Engenharia de Dados utilizando Databricks, PySpark, Delta Lake e Power BI para ingestão, tratamento e análise de dados públicos do Banco Central do Brasil relacionados às transações PIX e meios de pagamento.

## Objetivo

Construir uma solução completa de dados seguindo a arquitetura Medallion (Bronze, Silver e Gold), desde a ingestão dos dados via API até a disponibilização de dashboards analíticos no Power BI.

O projeto demonstra conceitos de:

- Engenharia de Dados
- ETL/ELT
- Arquitetura Lakehouse
- Delta Lake
- Modelagem Analítica
- Business Intelligence

---

## Tecnologias Utilizadas

- Python
- PySpark
- Databricks
- Delta Lake
- SQL
- Power BI
- Git/GitHub
- API Open Data Banco Central

---

## Arquitetura

```text
Banco Central APIs
        │
        ▼
    Bronze Layer
(Dados Brutos - Delta)
        │
        ▼
    Silver Layer
(Limpeza e Tratamento)
        │
        ▼
     Gold Layer
(Dados Analíticos)
        │
        ▼
      Power BI
```

---

## Fonte dos Dados

Os dados são consumidos através das APIs públicas do Banco Central do Brasil.

### Estatísticas de Meios de Pagamento

Contém informações sobre:

- PIX
- TED
- DOC
- TEC
- Boletos
- Cheques

### Transações PIX por Localização

Contém informações agregadas por:

- Região
- Estado
- Município

---

# 🥉 Camada Bronze

Responsável pela ingestão dos dados e armazenamento em formato bruto.

### Tabelas

| Tabela | Descrição |
|----------|----------|
| bronze.payment_statistics | Estatísticas de meios de pagamento |
| bronze.pix_transactions | Estatísticas específicas de transações PIX |

### Processamentos

- Consumo das APIs do Banco Central;
- Conversão para DataFrames Spark;
- Armazenamento em Delta Lake;
- Preservação dos dados originais.

---

# 🥈 Camada Silver

Responsável pela limpeza, padronização e preparação dos dados.

### Transformações

- Tratamento de valores nulos;
- Remoção de registros duplicados;
- Extração de Ano e Mês;
- Padronização dos datasets.

### Tabelas

| Tabela | Descrição |
|----------|----------|
| silver.payment_statistics | Dados tratados de meios de pagamento |
| silver.pix_transactions | Dados tratados de transações PIX |

---

# 🥇 Camada Gold

Responsável pela criação das tabelas analíticas consumidas pelo Power BI.

### Tabela PIX

Tabela:

```text
gold.pix_transactions
```

Granularidade:

```text
Região
 └── Estado
      └── Município
```

Métricas:

- Pagamentos Pessoa Física
- Pagamentos Pessoa Jurídica
- Recebimentos Pessoa Física
- Recebimentos Pessoa Jurídica

### Tabela de Meios de Pagamento

Tabela:

```text
gold.payment_transactions
```

Métricas de Quantidade:

- Quantidade de PIX
- Quantidade de TED
- Quantidade de DOC
- Quantidade de TEC
- Quantidade de Boletos
- Quantidade de Cheques

Métricas Financeiras:

- Valor PIX
- Valor TED
- Valor DOC
- Valor TEC
- Valor Boletos
- Valor Cheques

---

## Dashboard Power BI

O dashboard foi desenvolvido utilizando as tabelas da camada Gold.

### Principais Indicadores

- Evolução das transações PIX ao longo do tempo;
- Comparação entre PIX e meios tradicionais de pagamento;
- Volume financeiro movimentado;
- Distribuição geográfica por Região, Estado e Município;
- Ranking de Estados;
- Comparativo entre Pessoa Física e Pessoa Jurídica.

### Possíveis Insights

- Crescimento da adoção do PIX;
- Redução da utilização de meios tradicionais;
- Estados com maior movimentação financeira;
- Participação regional nas transações.

---

## Estrutura do Projeto

```text
├── notebooks
│   ├── bronze
│   ├── silver
│   └── gold
│
├── src
│   └── ingestion.py
│
├── dashboard
│   └── powerbi
│
└── README.md
```

## Autor

Lucas Daniel Alves Barcellos

Analista de Dados com foco em Engenharia de Dados, Data Science e soluções analíticas utilizando Python, SQL, Power BI e Databricks.
