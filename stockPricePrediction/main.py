import pandas
import prophet 
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    stockHistory = pandas.read_csv('./docs/MXRF11-history-19-22.csv')
    stockHistory = stockHistory[['Date', 'Adj Close']] # Remove another columns
    stockHistory.columns = ['ds', 'y'] # Rename respective columns
    
    prophetModel = prophet.Prophet()  # Instance prophet
    prophetModel.fit(stockHistory)    # Fit the model

    future = prophetModel.make_future_dataframe(periods=365)  # Generate future dataframe
    forecast = prophetModel.predict(future)     # Make forecastro from fit model

    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(365) # Get last occurances(traine + forecast)

    # True data v

    currentStockHistory = pandas.read_csv('./docs/MXRF11-history-22-23.csv')
    currentStockHistory = currentStockHistory[['Date', 'Adj Close']] # Remove another columns
    currentStockHistory.columns = ['ds', 'y'] # Rename respective columns

    currentProphetModel = prophet.Prophet()   # Instance prophet
    currentProphetModel.fit(currentStockHistory)   # Fit the model

    currentFuture = currentProphetModel.make_future_dataframe(periods=0)  # Generate future dataframe
    currentForecast = currentProphetModel.predict(currentFuture)
    
    currentForecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(0)   # Get last occurances(traine + forecast)

    # Graph

    plt.figure(figsize=(10, 6))  # Tamanho do gráfico (opcional)
    plt.plot(forecast[['ds']], forecast[['yhat']], label='valor(previsto)', color='c')

    plt.plot(currentForecast[['ds']], currentForecast[['yhat_upper']], label='valor máximo(esperado)', color='m')
    plt.plot(currentForecast[['ds']], currentForecast[['yhat']], label='valor(esperado)', color='b')
    plt.plot(currentForecast[['ds']], currentForecast[['yhat_lower']], label='valor mínimo(esperado)', color='purple')

    plt.xlabel('Data')
    plt.ylabel('Preço da ação')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()

main()