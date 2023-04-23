import pandas

df=pandas.read_csv('accdf.csv')
#print(df)

print('sorting on balance')
df1=df.sort_values("balance")
print(df1)

print('sorting on accnm descending')
df2=df.sort_values("accnm",ascending=False)
print(df2)

