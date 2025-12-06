
# Carregando os dados
import pandas as pd
from transformers import pipeline

df = pd.read_csv(r"Dados\reviews.csv")

# Carregar pipeline de análise de sentimentos (modelo multilíngue)
sentiment_model = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Função para mapear estrelas para categorias em português
def map_sentiment(stars):
    if stars == 1:
        return "MUITO NEGATIVO"
    elif stars == 2:
        return "NEGATIVO"
    elif stars == 3:
        return "NEUTRO"
    elif stars == 4:
        return "POSITIVO"
    else:  # 5 estrelas
        return "MUITO POSITIVO"

# -------------------------------
# Testar em uma frase específica
frase_teste = "I really loved this product, it works perfectly!"
resultado_teste = sentiment_model(frase_teste)[0]   # {'label': 'X stars', 'score': valor}

# Extrair apenas o número de estrelas
stars_teste = int(resultado_teste['label'].split()[0])
sentimento_teste = map_sentiment(stars_teste)

print("Frase teste:", frase_teste)
print("Estrelas:", stars_teste)
print("Classificação mapeada:", sentimento_teste)
print("Confiança:", f"{resultado_teste['score']:.4%}")
# -------------------------------

# Rodar o modelo em cada review do CSV
df['sentiment_raw'] = df['review_text'].apply(lambda x: int(sentiment_model(str(x))[0]['label'].split()[0]))
df['sentiment'] = df['sentiment_raw'].apply(map_sentiment)

print(df[['review_text', 'sentiment_raw', 'sentiment']].head())

# Salvar novo arquivo com os resultados
df.to_csv("Dados/reviews_with_sentiment.csv", index=False, mode='w')