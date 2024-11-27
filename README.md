# Preço Sanic App

Este é um aplicativo simples construído com **Sanic** para previsão de preços de ações usando **AutoML** com os modelos **LightGBM** e **XGBoost**. A aplicação consome dados financeiros de ações via **yfinance** e realiza a previsão de preço de fechamento utilizando o pacote **FLAML** para AutoML.

## Tecnologias Usadas

- **Sanic**: Framework assíncrono para construção de APIs.
- **yfinance**: Biblioteca para obtenção de dados financeiros.
- **FLAML**: AutoML para otimização e seleção automática de modelos.
- **LightGBM** e **XGBoost**: Algoritmos populares para tarefas de regressão.

## Instalação

### Pré-requisitos

Antes de começar, você precisa ter o **Python 3.7** ou superior instalado em sua máquina. Além disso, é necessário ter o **pip** instalado.

### Passos para instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/PrecoSanicApp.git
    cd PrecoSanicApp
    ```

2. **Crie e ative um ambiente virtual**  
   Recomendamos o uso de um ambiente virtual para garantir que as dependências não conflitem com outras aplicações.

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. **Instale as dependências**  
   Instale as bibliotecas necessárias listadas no `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Build a aplicação**  
   Agora, você pode buildar a aplicação localmente usando o comando:

    ```bash
    sudo docker build -t preco-sanic-app .
    ```
5. **Execute a aplicação**  
   Agora, você pode rodar a aplicação localmente usando o comando:

    ```bash
    sudo docker run -p 8000:8000 preco-sanic-app
    ```

### Como usar a API

A aplicação oferece um endpoint `/previsao` para fazer previsões do preço de fechamento de uma ação com base no histórico dos últimos 365 dias, com um intervalo de 1 dia, por padrão.

**Endpoint**

- **URL**: `http://localhost:8000/previsao`
- **Método**: `POST`

Envie uma requisição POST com um corpo JSON contendo o código da ação que deseja prever o preço. Por padrão, se você não fornecer o parâmetro `ticker`, o código da ação será **AAPL** (Apple Inc.).

- **Periodo**: ‘1d’, ‘5d’, ‘1mo’, ‘3mo’, ‘6mo’, ‘1y’, ‘2y’, ‘5y’, ‘10y’, ‘ytd’, ‘max’.
- **Intervalo**: ‘1m’, ‘2m’, ‘5m’, ‘15m’, ‘30m’, ‘60m’, ‘90m’, ‘1h’, ‘1d’, ‘5d’, ‘1wk’, ‘1mo’, ‘3mo’.

Obs: Não são obrigatorios os campos period e interval, caso não tenha period e interval, por padrão será 1y e 1d.

**Corpo da Requisição₁:**

    {
        "ticker": "AAPL",
        "period": "1y",
        "interval": "1d"
    }

**Corpo da Requisição₂:**

    {
        "ticker": "AAPL"
    }

**Resposta:**

    {
      "ticker": "AAPL",
      "predicted_price": [234.98]
    }

