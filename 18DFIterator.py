import pandas

dic={
"name":['praffull','soham','sharayu','janhavi'],
"city":['london','liverpool','dubai','new york'],
"club":['chelsea','liverpool','tottenham','dortmund']
}
df=pandas.DataFrame(dic)
print(df)
print('--------iterations------------')
for i,j in df.iterrows():
    print(j)
    print()