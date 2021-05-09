import pandas as pd
import openpyxl


dados = pd.read_excel(
  'gastosALEMANHA.xlsx','2021-SUPERMERCADO', engine='openpyxl')

print(dados.head(10))


a = pd.Series([2,4,55,-1,3.4,0])
print(a)