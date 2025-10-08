import pandas as pd

file_path = 'data/PIMPF - Produção física industrial por seções e atividades industriais.xlsx'

print("--- RESULTADOS DA EXPLORAÇÃO ---")

try:
    df = pd.read_excel(file_path)

    print("\n[1. DIMENSÕES]")
    print(f"Amostras (Linhas): {df.shape[0]}")

    print("\n[2. VALORES FALTANTES]")
    print(df.isnull().sum())

except Exception as e:
    print(f"\nERRO: Não foi possível carregar os dados. Detalhes: {e}")