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

print('Selecting a single column')
print(df['Title'])

print('Selecting multiple columns')
print(df[['Title','Language','Views']])

print('Selecting data from row, column using index')
print(df.loc[3])

print(df.loc[5,'Title'])
print(df.loc[5,['Title','Language']])

n=int(input('enter row : '))
lst=['Title','Channel','Likes']
print(df.loc[n,lst])

print(df.loc[8:])
print(df.loc[2:7])
print('---------------------------')
print(df.loc[2:7,'Title'])

print(df.loc[:5])
