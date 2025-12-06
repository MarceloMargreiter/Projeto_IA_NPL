# Bibliotecas
import pandas as pd
import streamlit as st
from transformers import pipeline


# =========================
# Configuração do Streamlit
# =========================
st.set_page_config(page_title="Análise de Sentimentos", layout="wide")



# =========================
# Cache do modelo Hugging Face (carregar uma vez)
# =========================
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )

sentiment_model = load_model()


# =========================
# Funções utilitárias
# =========================
def map_sentiment(stars: int) -> str:
    if stars == 1:
        return "MUITO NEGATIVO"
    elif stars == 2:
        return "NEGATIVO"
    elif stars == 3:
        return "NEUTRO"
    elif stars == 4:
        return "POSITIVO"
    else:
        return "MUITO POSITIVO"

def classify_phrase(phrase: str, model):
    """Classifica uma frase manualmente."""
    result = model(phrase)[0]
    stars = int(result['label'].split()[0])
    sentimento = map_sentiment(stars)
    score = result['score']
    return stars, sentimento, score

def classify_reviews(df: pd.DataFrame, model, text_col: str = "review_text") -> pd.DataFrame:
    """Classifica cada review individualmente."""
    df['sentiment_raw'] = df[text_col].apply(lambda x: int(model(str(x))[0]['label'].split()[0]))
    df['sentiment'] = df['sentiment_raw'].apply(map_sentiment)
    return df

def product_mean_sentiment(df: pd.DataFrame, product_col: str = "product_id"):
    """Calcula média de estrelas por produto (sentiment_raw e rating) e aplica o descritivo."""
    means = df.groupby(product_col).agg(
        mean_sentiment=('sentiment_raw', 'mean'),
        mean_rating=('rating', 'mean')
    ).reset_index()

    # Mapeia sentimento médio arredondado
    means['sentiment_mean'] = means['mean_sentiment'].round(4).astype(int).apply(map_sentiment)
    return means

def top_bottom_products(means: pd.DataFrame, n: int = 5):
    """Retorna dois DataFrames: top n melhores e top n piores produtos pela média de sentiment_raw(análise de sentimento)."""
    top_n = means.sort_values(by="mean_sentiment", ascending=False).head(n)
    bottom_n = means.sort_values(by="mean_sentiment", ascending=True).head(n)
    return top_n, bottom_n

# =========================
# Interface
# =========================
##st.title("Análise de Sentimentos de Produtos")
col_logo, col_title = st.columns([1, 11])
with col_logo:
    st.image("logo_2.png", width=180)  # ajuste o tamanho conforme necessário
with col_title:
    st.title("Análise de Sentimentos de Produtos")

tab_csv, tab_media, tab_teste = st.tabs(["Classificar Dataset", "Média por Produto", "Teste Manual"])

# -------------------------
# Aba 1: Classificação do Dataset
# -------------------------
with tab_csv:
    st.header("Classificação do Dataset")
    st.write("Clique no botão abaixo para processar o arquivo `Dados/reviews.csv` e gerar o novo CSV com sentimentos reclassificados usando NLP (Natural Language Processing).")

    if st.button("Classificar Dataset"):
        df = pd.read_csv("Dados/reviews.csv")

        if "review_text" not in df.columns:
            st.error("O arquivo não contém a coluna 'review_text'.")
        else:
            with st.spinner("Classificando reviews..."):
                df = classify_reviews(df, sentiment_model, text_col="review_text")

            st.success("Classificação concluída!")
            st.dataframe(df[['review_text', 'sentiment_raw', 'sentiment']].head(20))

            # Salvar arquivo processado
            df.to_csv("Dados/reviews_with_sentiment.csv", index=False)
            st.info("Arquivo `reviews_with_sentiment.csv` atualizado com os resultados.")

# -------------------------
# Aba 2: Média por Produto
# -------------------------
with tab_media:
    st.header("Média de Classificação por Produto")
    try:
        df_processed = pd.read_csv("Dados/reviews_with_sentiment.csv")

        if "product_id" in df_processed.columns and "rating" in df_processed.columns:
            means = product_mean_sentiment(df_processed, product_col="product_id")

            #st.subheader("Tabela completa de médias")
            #st.dataframe(means, use_container_width=True)

            # Usar função para pegar top/bottom
            top5, bottom5 = top_bottom_products(means, n=5)

            # Mostrar lado a lado
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🏆 Top 5 melhores produtos")
                st.dataframe(top5, use_container_width=True)
            with col2:
                st.subheader("⚠️ Top 5 piores produtos")
                st.dataframe(bottom5, use_container_width=True)

            
            st.subheader("Tabela completa de médias")
            st.dataframe(means, use_container_width=True)

        else:
            st.warning("O arquivo processado precisa conter as colunas 'product_id' e 'rating'.")
    except FileNotFoundError:
        st.error("Arquivo `reviews_with_sentiment.csv` não encontrado. Primeiro execute a classificação.")



# -------------------------
# Aba 3: Teste Manual
# -------------------------
with tab_teste:
    st.header("Teste Manual de Review")
    frase = st.text_area("Digite uma frase para análise", height=120)

    if st.button("Classificar Review"):
        if not frase.strip():
            st.warning("Digite uma frase para classificar.")
        else:
            stars, sentimento, score = classify_phrase(frase, sentiment_model)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Estrelas", stars)
            with col2:
                st.metric("Classificação", sentimento)
            with col3:
                st.metric("Confiança", f"{score:.2%}")