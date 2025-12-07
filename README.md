

# **Projeto_IA_PLN (Processamento de Linguagem Natural)**
**Componente curricular Projeto de Inteligencia Artificial - UNOESC - 2025**


## Tecnologias utilizadas
- Python 3
- VS Code
- Pandas
- Seaborn
- Matplotlib
- Jupyterlab
- Transformers
- Torch
- Streamlit
- Scikit-learn


## Como executar o projeto:

* ### Apontar para onde o repositório será clonado localmente:
Digite no Terminal:
```bash
cd "caminho onde o repositório será clonado. (Ex.: "C:/Nova Pasta")
```

* ### Clonar Projeto
Copiar o endereço do projeto e clonar usando o Terminal do VS Code.
```bash 
Git clone "https://github.com/MarceloMargreiter/Projeto_IA_NPL.git"
```

* ## Acessar o repositório clonado:
```bash
cd .\Projeto_IA_NPL\
```
 

* ### Criar Variável de Ambiente (.venv): 
Digite no Terminal:
```bash
python -m venv .venv
```    

* ### Ativar a Variável criada:

#### **Windows:**  
```bash
.venv\Scripts\activate
```
   
#### **Linux ou MacOS:**   
```bash
source .venv/bin/activate
```

* ### Instale os pacotes necessários no ambiente virtual:

```bash
pip install -r requirements.txt
``` 

* ### Execute o comando abaixo no terminal para gerar o Dashboard Streamlit:

```bash
streamlit run app.py
```
O app será executado no seu navegador localmente em:
```bash
http://localhost:8501/
```


## Problemas
- As pessoas perdem muito tempo e fica difícil fazer uma avaliação sobre os produtos de interesse para compra de um E-commerce, o que está gerando perda de vendas por conta da morosidade de avaliar o produto lendo todos os reviews.

- Criar um avaliador de sentimentos para resumir se o produto é bem ou mal avaliado com base nos comentários ajudará o cliente a ter uma avaliação rápida e prática com a experiência obtida por outros clientes.


## Requisitos do negócio
- Vamos criar um modelo que lê comentários e diz se são positivos ou negativos, para avaliar os reviews, fazendo também uma avaliação geral com base nos comentários e comparando com os valores de rating.

- Método: Processamento de Linguagem Natural (PLN)

- Disponibilizar o dasboard online para interação do cliente (*usuário*).



##  Dataset utilizado: 
### *https://www.kaggle.com/datasets/abhayayare/e-commerce-dataset*
* /products.csv
* /reviews.csv
* /users.csv

        *Extraídos em 24/11/2025.