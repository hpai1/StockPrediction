
from fetch_data import fetch_data
from show_data import show_data
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot

def main():
    
    df = fetch_data()

    if df is not None:
        
        print(df.head())  
    else:
        print("Fetching data failed. Check your API key or network connection.")


    # show_data(df)

    # plt.figure()
    # lag_plot(df['open'], lag=3)
    # plt.title('TESLA Stock - Autocorrelation plot with lag = 3')
    # plt.show()


if __name__ == "__main__":
    main()