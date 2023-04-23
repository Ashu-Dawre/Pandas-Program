import pandas
import ssl
import numpy

ssl._create_default_https_context=ssl._create_unverified_context
url='https://restapi.sohamglobal.in/api/accounts'
df=pandas.read_json(url)
print(df.head(3))

df1=df.describe()
#print(df1)
print(numpy.round(df1,2))
