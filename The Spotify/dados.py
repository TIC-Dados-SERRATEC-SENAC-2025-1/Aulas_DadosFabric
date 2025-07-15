# import pandas as pd
# import os

# dados = 00
# # Caminho onde estão os arquivos
# caminho = os.scandir('C:\_mlUc1\Aulas_DadosFabric\The Spotify')

# for file in caminho:
#     if file.is_file() and file.name.endswith('.csv'):
#         print(f'Processando: {file.name}')
        
#         # Lê o arquivo CSV
#         df = pd.read_csv(file.path, sep=',', encoding='utf8')

#         # Verifica se a coluna existe
#         if 'track' in df.columns:
#             # Substitui vírgula por ponto sem usar replace()
#             df['track'] = df['track'].astype(str).str.split(',').str.join('.')
#             dados += 10

#             # Salva com outro nome ou sobrescreve
#             df.to_csv(f'tratado_{file.name}', index=False)
#         else:
#             print(f"Coluna 'dataset_of_10s_track' não encontrada em {file.name}")



import pandas as pd
import os

dados = 00
# Caminho onde estão os arquivos
caminho = os.scandir('C:\_mlUc1\Aulas_DadosFabric\The Spotify')
i = 1

for file in caminho:
    if file.is_file() and file.name.endswith('.csv'):
        print(f'Processando: {file.name}')
        
        # Lê o arquivo CSV
        df = pd.read_csv(file.path, sep=',', encoding='utf8')
        df.columns = [col.replace('_', ' ').split()[3] for col in df.columns]
        df['id_ano'] = i
        i += 1  
        # Verifica se a coluna existe
        if 'track' in df.columns:
            # Substitui vírgula por ponto sem usar replace()
            df['track'] = df['track'].astype(str).str.split(',').str.join('.')

            # Salva com outro nome ou sobrescreve
            df.to_csv(f'tratado_{file.name}', index=False)
        
        else:
            print(f"Coluna 'dataset_of_10s_track' não encontrada em {file.name}")