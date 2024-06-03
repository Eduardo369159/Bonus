import pandas as pd
import os

# Diretório onde os arquivos Excel estão localizados
diretorio = 'Z:\\CONTROLLER\\CAMPANHAS\\AGENTE\\2024\\202404'
# Lista para armazenar os DataFrames de todos os arquivos Excel
dfs = []

# Percorre todos os arquivos no diretório
for filename in os.listdir(diretorio):
    # Verifica se o arquivo começa com 'BONUS' e tem extensão .xlsx
    if filename.startswith('BONUS') and filename.endswith('.xlsx'):
        # Caminho completo do arquivo
        filepath = os.path.join(diretorio, filename)
        # Lê o arquivo Excel e adiciona o DataFrame à lista
        df = pd.read_excel(filepath)
        dfs.append(df)

# Concatena todos os DataFrames da lista em um único DataFrame
concatenated_df = pd.concat(dfs, ignore_index=True)

# Salva o DataFrame concatenado em um novo arquivo Excel
concatenated_file = './data/concatenated_bonus_files.xlsx'
concatenated_df.to_excel(concatenated_file, index=False)

print(f'Os arquivos foram concatenados e salvos em {concatenated_file}')
