from faker import Faker
import pandas as pd
import random

# Inicializar o Faker
fake = Faker()

# Lista para armazenar os dados
data = []

# Gerar 200 registros
for _ in range(200):
    idade = random.randint(18, 65)
    renda = random.randint(1000, 15000)
    genero = random.choice(['Masculino', 'Feminino'])
    comprador = 1 if renda > 7000 else 0
    # Adicionar os dados à lista
    data.append([idade, renda, genero, comprador])

# Criar o DataFrame
df = pd.DataFrame(data, columns=['Idade', 'Renda', 'Gênero', 'Comprador'])

# Salvar o DataFrame em um arquivo CSV na pasta raiz
df.to_csv(r"C:\Users\taua_\OneDrive\Área de Trabalho\Projetos\visao_computacional_ia\dados_ger.csv", index=False)

print("Arquivo 'dados_ger.csv' gerado com sucesso em 'C:\\Users\\taua_\\OneDrive\\Área de Trabalho\\Projetos\\visao_computacional_ia\\dados_ger.csv'!")
print("Primeiras linhas do dataset:")
print(df.head())