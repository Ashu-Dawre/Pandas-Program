import pandas

url='https://api.exchangerate-api.com/v4/latest/USD'

df=pandas.read_json(url)
print(df)
df.to_csv('rates.csv')