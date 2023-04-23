import numpy
import pandas

arr=numpy.array([
    ['praffull','sharayu','shailaja','soham'],
    ['sql','spark','csharp','javaee'],
    ['microsoft','oracle','google','accenture'],
    ['london','berlin','dubai','new york'],
    [20,9,15,2]
])

print(arr)
print(arr.shape)

#df=pandas.DataFrame(arr)
df=pandas.DataFrame(arr,['Name','Tool','Company','Location','Experience'],['Self','Daughter','Wife','Son'])
'''
rows=numpy.array(['Name','Technology','Company'])
cols=numpy.array(['Emp1','Emp2','Emp3','Emp4'])
df=pandas.DataFrame(arr,rows,cols)
'''
print(df)
