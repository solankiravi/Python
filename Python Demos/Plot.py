import  pandas as pd
import matplotlib.pyplot as mp
url = 'https://www.quandl.com/api/v3/datasets/EOD/V.csv?api_key=Fa1P1yZLGnGSsXktrvzL'
df = pd.read_csv(url, parse_dates=True,index_col=0)
df = df.rename(columns={'Close':'Stock Price'})
s = df['Stock Price']

s_to_plot = s.sort_index(ascending=True).tail(100)
ax = s_to_plot.plot(title='End of Day Visa Stock Prices for US Exchange')
ax.set_ylabel('Stock Price')
df.plot.bar() 
mp.show()