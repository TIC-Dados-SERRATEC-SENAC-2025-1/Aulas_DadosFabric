import pandas as pd
import os


caminho = os.scandir('C:\_mlUc1\Aulas_DadosFabric\The Spotify')


for file in caminho:
    if file.is_file() and file.name.endswith('.csv'):
        print(f'Processando: {file.name}')
        
      
        df = pd.read_csv(file.path, sep=',', encoding='utf8')
        df.columns = [col.replace('_', ' ').split()[3] for col in df.columns]
   
   
        if 'track' in df.columns:
            # Substitui vírgula por ponto sem usar replace()
            df['track'] = df['track'].astype(str).str.split(',').str.join('.')

           
            df.to_csv(f'tratado_{file.name}', index=False)
        
        else:
            print(f"Coluna 'dataset_of_10s_track' não encontrada em {file.name}")
