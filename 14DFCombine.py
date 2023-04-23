import numpy
import pandas

vdoarr=numpy.array([
        ['hibernate','education','sohamglobal','english',1450,200],
        ['sweet bengal','tourism','spacetimecinema','bengali',540,120],
        ['git-github','education','sohamglobal','english',540,221],
        ['data science','education','sharayuglobal','english',380,47],
        ['sql-db','education','sohamglobal','english',1270,550],
        ['test cricket','sports','spacetimecinema','english',45809,5748],
        ['install visual studio','education','sohamglobal','english',4732,543],
        ['premier league','sports','soformidable','english',7438,763],
        ['spark','education','sharayuglobal','english',8743,795],
        ['rawangla sikkim','tourism','spacetimecinema','hindi',8694,764],
        ['configure tomcat','education','sohamglobal','english',5932,384],
        ['intro to javabeans','education','sharayuglobal','hindi',9484,667],
        ['ramoji hyderabad','tourism','spacetimecinema','telugu',7944,154]
])

cols=['Title','Category','Channel','Language','Views','Likes']
df=pandas.DataFrame(vdoarr,columns=cols)
print(df)

#print(df.head(4))
#print(df.tail(3))
print('combining using rows')
df1=df.head(4)
df2=df.tail(3)
res=df1.append(df2)
print(res)

print('combining using columns')
df3=df[['Title','Category']]
df4=df[['Views','Likes']]
res=pandas.concat([df3,df4],axis=1)
print(res)