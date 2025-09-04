import pandas as pd

# Lê o arquivo Excel (ou CSV)
arquivo = input("Digite o caminho completo do arquivo Excel (.xlsx ou .csv): ").strip()
if arquivo.lower().endswith('.xlsx'):
    df = pd.read_excel(arquivo, engine="openpyxl")
else:
    df = pd.read_csv(arquivo)

# Verifica se as colunas necessárias estão presentes
colunas_esperadas = ["nome", "idade", "altura", "telefone"]
for col in colunas_esperadas:
    if col not in df.columns:
        raise ValueError(f"Coluna obrigatória '{col}' não encontrada no arquivo.")

# Função para formatar cada linha em comando SQL
def linha_para_sql(row):
    nome = row["nome"]
    idade = row["idade"]
    altura = row["altura"]
    telefone = row["telefone"]
    return f"INSERT INTO cadpessoas VALUES ('{nome}', {idade}, {altura}, '{telefone}');"

# Gerar todos os comandos
sql_statements = [linha_para_sql(row) for _, row in df.iterrows()]

# Salvar em um arquivo .sql
with open("../inserts.sql", "w", encoding="utf-8") as f:
    for stmt in sql_statements:
        f.write(stmt + "\n")

print("✅ Arquivo 'inserts.sql' gerado com sucesso!")
