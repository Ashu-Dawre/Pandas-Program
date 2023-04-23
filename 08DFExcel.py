#pip install openpyxl
import pandas

file=pandas.ExcelFile('companies.xlsx')
df=file.parse('Sheet1')
print(df)
