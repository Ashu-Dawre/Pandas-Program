import pandas

df=pandas.read_csv('accdf.csv')

print('Group information')
df2=df.groupby('acctype')
print(df2)

for rec in df2:
    print(rec)

print(df.groupby('acctype').groups)
