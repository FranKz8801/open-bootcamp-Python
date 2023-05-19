import pandas as pd

# Lee el archivo Excel
df = pd.read_excel('archivo_excel.xlsx')

# Convierte el archivo a formato CSV
df.to_csv('archivo_csv.csv', index=False)