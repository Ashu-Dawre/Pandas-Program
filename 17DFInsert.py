import pandas

dic={
"name":['praffull','soham','sharayu','janhavi'],
"city":['london','liverpool','dubai','new york']    
}
df=pandas.DataFrame(dic)
print(df)

df.insert(1,'fancode',9)
df.insert(3,'club','chelsea')
print(df)