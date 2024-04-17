import pandas as pd
import glob
import os

os.chdir(r'.\Tarea') #Verificar directorio actual de trabajo

pattern = 'demanda_electrica*.csv'

csv_files = glob.glob(pattern)

for file in csv_files:
    df = pd.read_csv(file)

    df['Fecha'] = df['Fecha'].str.replace('T00:00:00.000+01:00', '', regex=False)
    df['Fecha'] = df['Fecha'].str.replace('T00:00:00.000+02:00', '', regex=False)
    
    df.to_csv(file, index=False)


    #### fusionamos los csvs: ######


dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

df_concatenado = pd.concat(dfs, ignore_index=True)
df_concatenado['Fecha'] = df_concatenado['Fecha'].str.replace('T00:00:00.000+01:00', '', regex=False)
df_concatenado['Fecha'] = df_concatenado['Fecha'].str.replace('T00:00:00.000+02:00', '', regex=False)

df_concatenado.to_csv('demanda_electrica_2011_2023.csv', index=False)