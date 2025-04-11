import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Inicializar o Faker
fake = Faker()

# Função para gerar dados para heart.csv
def gerar_heart_data(n_samples=1000):
    data = []
    for _ in range(n_samples):
        row = {
            "age": random.randint(29, 77),
            "sex": random.randint(0, 1),
            "cp": random.randint(0, 3),
            "trestbps": random.randint(94, 200),
            "chol": random.randint(126, 564),
            "fbs": random.randint(0, 1),
            "restecg": random.randint(0, 2),
            "thalach": random.randint(71, 202),
            "exang": random.randint(0, 1),
            "oldpeak": round(random.uniform(0.0, 6.2), 1),
            "slope": random.randint(0, 2),
            "ca": random.randint(0, 3),
            "thal": random.randint(1, 3),
            "target": random.randint(0, 1),
        }
        data.append(row)
    return pd.DataFrame(data)

# Função para gerar dados para kc_house_data.csv
def gerar_kc_house_data(n_samples=1000):
    data = []
    for _ in range(n_samples):
        # Gerar uma data entre 2014 e 2015
        start_date = datetime(2014, 1, 1)
        end_date = datetime(2015, 12, 31)
        date = fake.date_between(start_date=start_date, end_date=end_date)
        date_str = date.strftime("%Y%m%d")

        row = {
            "id": fake.unique.random_int(min=1000000000, max=9999999999),
            "date": date_str,
            "price": round(random.uniform(200000.0, 8000000.0), 2),
            "bedrooms": random.randint(0, 10),
            "bathrooms": round(random.uniform(0.0, 8.0), 2),
            "sqft_living": random.randint(290, 13540),
            "sqft_lot": random.randint(520, 1651359),
            "floors": round(random.uniform(1.0, 3.5), 1),
            "waterfront": random.randint(0, 1),
            "view": random.randint(0, 4),
            "condition": random.randint(1, 5),
            "grade": random.randint(1, 13),
            "sqft_above": random.randint(290, 9410),
            "sqft_basement": random.randint(0, 4820),
            "yr_built": random.randint(1900, 2015),
            "yr_renovated": random.choice([0] * 8 + [random.randint(1900, 2015)]),  # 80% chance de ser 0
            "zipcode": random.randint(98001, 98199),
            "lat": round(random.uniform(47.1559, 47.7776), 4),
            "long": round(random.uniform(-122.519, -121.315), 4),
            "sqft_living15": random.randint(399, 6210),
            "sqft_lot15": random.randint(651, 871200),
        }
        data.append(row)
    return pd.DataFrame(data)

# Criar a pasta parte_ii/datasets/ se ela não existir
output_dir = "parte_ii/datasets"
os.makedirs(output_dir, exist_ok=True)

# Gerar os dados
heart_df = gerar_heart_data(n_samples=1000)  # 1000 amostras
kc_house_df = gerar_kc_house_data(n_samples=1000)  # 1000 amostras

# Salvar os dados em arquivos CSV
heart_df.to_csv(os.path.join(output_dir, "heart.csv"), index=False)
kc_house_df.to_csv(os.path.join(output_dir, "kc_house_data.csv"), index=False)

print("Arquivos gerados com sucesso:")
print(f"- {os.path.join(output_dir, 'heart.csv')}")
print(f"- {os.path.join(output_dir, 'kc_house_data.csv')}")