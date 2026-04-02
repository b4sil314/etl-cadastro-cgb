import os
import re
import pandas as pd

pasta_entrada = r"C:\Users\USER\OneDrive - GRUPO CGB\Banco de dados\Importar"
pasta_saida = os.path.join(pasta_entrada, "limpos")
os.makedirs(pasta_saida, exist_ok=True)


def limpar(texto):
    if pd.isna(texto):
        return ''

    texto = str(texto)

    texto = re.sub(r'<[^>]*>', '', texto)
    texto = re.sub(r'@[^@]*@', '', texto)
    texto = re.sub(r'[\[\]\(\)#%]', '', texto)
    texto = texto.replace('\n', ' ').replace('\r', ' ')
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()


print("📂 Lendo arquivos...")

for arquivo in os.listdir(pasta_entrada):

    if arquivo.lower().endswith(".xlsx"):

        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        nome_saida = arquivo.replace(".xlsx", "_limpo.csv")
        caminho_saida = os.path.join(pasta_saida, nome_saida)

        print(f"🔄 Processando: {arquivo}")

        try:
            df = pd.read_excel(caminho_entrada, engine="openpyxl")

            df = df.astype(str).apply(lambda col: col.map(limpar))

            df.to_csv(
                caminho_saida,
                sep=';',
                index=False,
                encoding='utf-8-sig'  # 👈 AQUI
            )

            print(f"✅ Gerado: {nome_saida}")

        except Exception as e:
            print(f"❌ Erro em {arquivo}: {e}")

print("\n🚀 Todos os arquivos foram processados!")