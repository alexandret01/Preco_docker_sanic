from sanic import Sanic
from sanic.response import json
import yfinance as yf
from flaml import AutoML
import pandas as pd
import numpy as np

app = Sanic("PrecoSanicApp")

@app.route("/previsao", methods=["POST"])
async def previsao(request):
    data = request.json
    ticker = data.get('ticker', 'AAPL')
    periodo = data.get('period', '1y')
    intervalo = data.get('interval', '1d')

    # Obtendo dados financeiros com yfinance
    stock_data = yf.download(ticker, period=periodo, interval=intervalo)
    df = pd.DataFrame(stock_data)

    # Seleção de features (X) e variável alvo (y)
    X = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # Features
    y = df['Close']  # Variável alvo (preço de fechamento)

    # Garantindo que y seja um pandas Series ou numpy array
    y = np.array(y)  # Convertendo y para numpy array, caso não seja
    X = X.values  # Convertendo X para numpy array, se necessário

    # Inicializando o AutoML com especificação de regressão
    automl = AutoML()

    # Ajustando o modelo com orçamento de tempo e deixando o AutoML escolher o modelo
    automl.fit(X, y, task="regression", time_budget=60)

    # Fazendo a previsão para o último ponto de dados
    predicted_price = automl.predict(X[-1:])

    # Retornando o preço previsto
    return json({"ticker": ticker, "predicted_price": predicted_price.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)