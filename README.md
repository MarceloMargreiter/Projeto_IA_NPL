
##  Dataset: 
### *https://www.kaggle.com/datasets/abhayayare/e-commerce-dataset*
* /products.csv
* /reviews.csv
* /users.csv


# Etapas:
* apontar o caminho (cd)
* criar ambiente variável (*caso não exista*)

    python -m venv .venv
* ativar a variável de ambiente:
    
    bash'''
        .venv\Scripts\activate
      '''

* instalar as bibliotecas necessárias:
    pip install -r requirements.txt
    
* executar:
     python sentiment_app.py


* executar app streamlit
    streamlit run app.py