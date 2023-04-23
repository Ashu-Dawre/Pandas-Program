import pandas
import ssl

ssl._create_default_https_context=ssl._create_unverified_context
url='https://restapi.sohamglobal.in/api/accounts'
df=pandas.read_json(url)
print(df)
