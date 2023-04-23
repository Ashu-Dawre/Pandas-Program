import pandas
import numpy

df=pandas.read_csv('accdf.csv')
#print(df)

print('Filter by condition')
#df1=df[df['acctype']=='saving']
df1=df[df['acctype']!='saving']
print(df1)

print('Filter by relational operator')
df2=df[df['balance']>75000]
print(df2)

print('multiple conditions')
df3=df[(df['acctype']=='current') & (df['balance']<45000)]
print(df3)

df3=df[(df['acctype']=='fixed') | (df['balance']>90000)]
print(df3)

ano=[1029,1030,1008]
df4=df[df['accno'].isin(ano)]
print(df4)