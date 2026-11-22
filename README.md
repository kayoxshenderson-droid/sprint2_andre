# Análise de Dados do Catálogo da Netflix

Projeto da Sprint 2 do Challenge (FIAP), feito em Python com Pandas e Matplotlib.

O script lê uma base com os títulos da Netflix (`filme_netflix.csv`), trata valores ausentes e gera gráficos e estatísticas para entender o catálogo.

## O que o código faz

**Tratamento dos dados**
- Preenche `type` e `country` vazios com "Nao Informado".
- Converte `release_year` para número.
- Extrai a duração em minutos dos filmes a partir da coluna `duration`.

**Gráficos**
- Pizza: proporção de filmes e séries.
- Barras: os 10 países com mais títulos.
- Histograma: distribuição dos anos de lançamento.
- Boxplot: duração dos filmes.

**Estatística descritiva** (ano de lançamento e duração dos filmes)
- Média, mediana e moda
- Mínimo e máximo
- Desvio padrão
- Quartis (Q1, Q2, Q3)

## Tecnologias

- Python 3
- Pandas
- Matplotlib

## Como executar

```bash
pip install pandas matplotlib
python analise.py
```

Os gráficos abrem um por vez. Feche cada janela para ver o próximo.

## Autor

Kayo Henderson, Ciência da Computação, FIAP.
