import pandas as pd
import matplotlib.pyplot as plt

# lê o ".csv"
df = pd.read_csv("filme_netflix.csv")

# mostra informaçoes
print("Quantidade de linhas:", len(df))
print(df.head())

# separa as colunas
df["type"] = df["type"].fillna("Nao Informado")
df["country"] = df["country"].fillna("Nao Informado")
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

# ============= Grafico de Pizza ( Grafico de Setores ) =============

tipos = df["type"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    tipos.values,
    labels=tipos.index,
    autopct="%1.1f%%"
)

plt.title("Porcentagem de Filmes e Series")
plt.legend(tipos.index)

plt.show()

# ============= Grafico em Barra =============

paises = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))

plt.bar(
    paises.index,
    paises.values,
    color="blue"
)

plt.title("Top 10 Paises")
plt.xlabel("Paises")
plt.ylabel("Quantidade")

plt.xticks(rotation=45)

plt.show()

# ============= Histograma =============

plt.figure(figsize=(8,5))

plt.hist(
    df["release_year"].dropna(),
    bins=20,
    color="green"
)

plt.title("Distribuicao dos Anos")
plt.xlabel("Ano")
plt.ylabel("Quantidade")

plt.show()

# ============= BOXPLOT =============

# pega só o Filme
filmes = df[df["type"] == "Movie"].copy()

# pegando os numeros da duracao
filmes["duracao"] = filmes["duration"].str.extract(r"(\d+)")

# transformando para numero
filmes["duracao"] = pd.to_numeric(
    filmes["duracao"],
    errors="coerce"
)

plt.figure(figsize=(6,5))

plt.boxplot(
    filmes["duracao"].dropna()
)

plt.title("Boxplot da Duracao dos Filmes")
plt.ylabel("Minutos")

plt.show()

# ============= Analise UNIVARIADA-1 + Ano de lançamentos dos filmes =============

print("\n===== ANALISE ANO DE LANCAMENTO =====")

print("Media:", df["release_year"].mean())
print("Mediana:", df["release_year"].median())
print("Moda:", df["release_year"].mode()[0])

print("Minimo:", df["release_year"].min())
print("Maximo:", df["release_year"].max())

print("Desvio Padrao:", df["release_year"].std())

print("Q1:", df["release_year"].quantile(0.25))
print("Q2:", df["release_year"].quantile(0.50))
print("Q3:", df["release_year"].quantile(0.75))

# ============= Analise UNIVARIADA-2 + Duração dos filmes =============

print("\n===== ANALISE DURACAO DOS FILMES =====")

print("Media:", filmes["duracao"].mean())
print("Mediana:", filmes["duracao"].median())
print("Moda:", filmes["duracao"].mode()[0])

print("Minimo:", filmes["duracao"].min())
print("Maximo:", filmes["duracao"].max())

print("Desvio Padrao:", filmes["duracao"].std())

print("Q1:", filmes["duracao"].quantile(0.25))
print("Q2:", filmes["duracao"].quantile(0.50))
print("Q3:", filmes["duracao"].quantile(0.75))

# ============= Relatorio =============

print("\n===== RELATORIO =====")

print("A maioria dos titulos da base sao filmes.")
print("Os anos mais recentes aparecem com maior frequencia.")
print("Existem filmes com duracoes acima da media.")
print("Os graficos ajudam a entender melhor os dados analisados.")
