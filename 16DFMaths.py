import pandas

dic={
    'mumbai':[35,32,36],
    'london':[18,20,14],
    'dubai':[44,46,43]
}

df=pandas.DataFrame(dic)
print(df)

#df=df.add(1)
#df=df.sub(0.5)
#df=df.mul(2)
df=df.div(2)
print(df)