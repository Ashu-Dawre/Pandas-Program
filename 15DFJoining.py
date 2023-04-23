import pandas

cdf=pandas.read_csv('customers.csv')
odf=pandas.read_csv('orders.csv')

print('Inner join - only matching from both DF')
dfinner=cdf.merge(odf,on='userid',how='inner')
#print(dfinner)

print('Left Outer join - all customers DF and matching/NaN orders')
dfleft=cdf.merge(odf,on='userid',how='left')
#print(dfleft[['name','orderno']])

print('Right Outer join - all orders DF and matching/NaN customers')
dfright=cdf.merge(odf,on='userid',how='right')
print(dfright)