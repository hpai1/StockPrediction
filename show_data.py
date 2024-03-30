import matplotlib.pyplot as plt
import pandas as pd


from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

def show_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['close'], color='blue', linewidth=2)
    plt.title('Close Price Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.show()