import pandas

df=pandas.read_csv('orders.csv')
print(df)
print('-'*30)
print('show status of null values in DF')
print(pandas.isnull(df))
#print(df.describe())

print('-'*30)
print('romove rows with null values')
df1=df.dropna()
print(df1)

print('-'*30)
print('remove columns with null values')
df2=df.dropna(axis=1)
print(df2)

print('-'*30)
print('rename null values')
df['userid'].fillna('NoUserID',inplace=True)
print(df)

print('-'*30)
print('replace values')
df3=df.replace('confirmed','PLACED')
print(df3)