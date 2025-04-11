import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix, silhouette_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar o layout da página
st.set_page_config(page_title="Projeto de Classificação e Clusterização com IA Generativa", layout="wide")

# Título do aplicativo
st.title("Projeto de Classificação e Clusterização com IA Generativa")

# --- Carregar os datasets ---
st.header("📂 Carregamento dos Datasets")

# Carregar dados_ger.csv
file_path_dados_ger = r"C:\Users\taua_\OneDrive\Área de Trabalho\Projetos\visao_computacional_ia\dados_ger.csv"
try:
    df_dados_ger = pd.read_csv(file_path_dados_ger, encoding="utf-8", sep=",")
    st.write("Dataset dados_ger.csv carregado com sucesso!")
except FileNotFoundError:
    st.error(f"Erro: O arquivo 'dados_ger.csv' não foi encontrado em: {file_path_dados_ger}")
    st.stop()
except pd.errors.ParserError:
    st.error("Erro: Falha ao parsear 'dados_ger.csv'. Tentando com delimitador alternativo e codificação latin1.")
    try:
        df_dados_ger = pd.read_csv(file_path_dados_ger, encoding="latin1", sep=";", on_bad_lines="skip")
        st.write("Sucesso: Arquivo lido com delimitador ';' e codificação latin1.")
    except Exception as e:
        st.error(f"Tentativa alternativa falhou: {str(e)}")
        st.stop()
except Exception as e:
    st.error(f"Erro ao ler o arquivo 'dados_ger.csv': {str(e)}")
    st.stop()

# Verificar integridade de dados_ger.csv
expected_columns = ['Idade', 'Renda', 'Gênero', 'Comprador']
if not all(col in df_dados_ger.columns for col in expected_columns):
    st.error(f"Erro: O arquivo 'dados_ger.csv' não contém todas as colunas esperadas: {expected_columns}")
    st.stop()

if not (df_dados_ger['Idade'].dtype in [np.int64, np.float64] and 
        df_dados_ger['Renda'].dtype in [np.int64, np.float64]):
    st.error("Erro: As colunas 'Idade' e/ou 'Renda' não são numéricas.")
    st.stop()

if not df_dados_ger['Gênero'].isin(['Masculino', 'Feminino']).all():
    st.error("Erro: A coluna 'Gênero' contém valores inesperados (esperado: 'Masculino' ou 'Feminino').")
    st.stop()

if not df_dados_ger['Comprador'].isin([0, 1]).all():
    st.error("Erro: A coluna 'Comprador' contém valores não binários (esperado: 0 ou 1).")
    st.stop()

# Carregar heart.csv
file_path_heart = r"C:\Users\taua_\OneDrive\Área de Trabalho\Projetos\visao_computacional_ia\parte_ii\datasets\heart.csv"
try:
    df_heart = pd.read_csv(file_path_heart)
    st.write("Dataset heart.csv carregado com sucesso!")
except FileNotFoundError:
    st.error(f"Erro: O arquivo 'heart.csv' não foi encontrado em: {file_path_heart}")
    st.stop()

# Carregar kc_house_data.csv
file_path_kc_house = r"C:\Users\taua_\OneDrive\Área de Trabalho\Projetos\visao_computacional_ia\parte_ii\datasets\kc_house_data.csv"
try:
    df_kc_house = pd.read_csv(file_path_kc_house)
    st.write("Dataset kc_house_data.csv carregado com sucesso!")
except FileNotFoundError:
    st.error(f"Erro: O arquivo 'kc_house_data.csv' não foi encontrado em: {file_path_kc_house}")
    st.stop()

# --- Seção 1: Dados Gerados (dados_ger.csv) ---
st.header("🔍 Dados Gerados (dados_ger.csv)")
st.dataframe(df_dados_ger.head())

# Pré-processamento para dados_ger.csv
df_dados_ger['Gênero'] = LabelEncoder().fit_transform(df_dados_ger['Gênero'])
X_ger = df_dados_ger[['Idade', 'Renda', 'Gênero']]
y_ger = df_dados_ger['Comprador']

# Dividir em treino e teste
X_train_ger, X_test_ger, y_train_ger, y_test_ger = train_test_split(X_ger, y_ger, test_size=0.3, random_state=42)

# --- Seção 2: Classificação (dados_ger.csv) ---
st.header("📊 Classificação - Comprador ou Não (dados_ger.csv)")

# Treinar o modelo de classificação
model_ger = RandomForestClassifier(random_state=42)
model_ger.fit(X_train_ger, y_train_ger)

# Fazer previsões
y_pred_ger = model_ger.predict(X_test_ger)

# Calcular métricas
accuracy_ger = accuracy_score(y_test_ger, y_pred_ger)
precision_ger = precision_score(y_test_ger, y_pred_ger)
f1_ger = f1_score(y_test_ger, y_pred_ger)

# Exibir métricas
st.write(f"Acurácia do Modelo: **{accuracy_ger:.2f}**")
st.write(f"Precisão: **{precision_ger:.2f}**")
st.write(f"F1-Score: **{f1_ger:.2f}**")

# Matriz de Confusão
cm_ger = confusion_matrix(y_test_ger, y_pred_ger)
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(cm_ger, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel('Previsão')
ax.set_ylabel('Verdadeiro')
ax.set_title('Matriz de Confusão - Classificação Comprador')
st.pyplot(fig)

# --- Seção 3: Clusterização (dados_ger.csv) ---
st.header("🧠 Clusterização - Agrupamento por Similaridade (dados_ger.csv)")

# Aplicar K-Means
X_cluster = df_dados_ger[['Idade', 'Renda']]
kmeans = KMeans(n_clusters=2, random_state=42)
df_dados_ger['Cluster'] = kmeans.fit_predict(X_cluster)

# Calcular Silhouette Score
silhouette = silhouette_score(X_cluster, df_dados_ger['Cluster'])
st.write(f"Silhouette Score da Clusterização: **{silhouette:.2f}**")

# Exibir os dados com clusters
st.dataframe(df_dados_ger[['Idade', 'Renda', 'Cluster']].head())

# Visualizar os clusters
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(df_dados_ger['Idade'], df_dados_ger['Renda'], c=df_dados_ger['Cluster'], cmap='viridis')
ax.set_xlabel('Idade')
ax.set_ylabel('Renda')
ax.set_title('Clusters de Idade e Renda')
plt.colorbar(scatter, ax=ax, label='Cluster')
st.pyplot(fig)

# --- Seção 4: Classificação Binária - Heart Disease (heart.csv) ---
st.header("📈 Classificação Binária - Heart Disease (heart.csv)")
st.dataframe(df_heart.head())

# Pré-processamento para heart.csv
X_heart = df_heart.drop(columns=['target'])
y_heart = df_heart['target']

# Dividir em treino e teste
X_train_heart, X_test_heart, y_train_heart, y_test_heart = train_test_split(X_heart, y_heart, test_size=0.3, random_state=42)

# Treinar o modelo
model_heart = RandomForestClassifier(random_state=42)
model_heart.fit(X_train_heart, y_train_heart)

# Fazer previsões
y_pred_heart = model_heart.predict(X_test_heart)

# Calcular métricas
accuracy_heart = accuracy_score(y_test_heart, y_pred_heart)
precision_heart = precision_score(y_test_heart, y_pred_heart)
f1_heart = f1_score(y_test_heart, y_pred_heart)

# Exibir métricas
st.write(f"Acurácia do Modelo: **{accuracy_heart:.2f}**")
st.write(f"Precisão: **{precision_heart:.2f}**")
st.write(f"F1-Score: **{f1_heart:.2f}**")

# Matriz de Confusão
cm_heart = confusion_matrix(y_test_heart, y_pred_heart)
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(cm_heart, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel('Previsão')
ax.set_ylabel('Verdadeiro')
ax.set_title('Matriz de Confusão - Classificação Heart Disease')
st.pyplot(fig)

# --- Seção 5: Regressão - Preço de Casas (kc_house_data.csv) ---
st.header("📉 Regressão - Preço de Casas (kc_house_data.csv)")
st.dataframe(df_kc_house.head())

# Pré-processamento para kc_house_data.csv
features_kc = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors']
X_kc = df_kc_house[features_kc]
y_kc = df_kc_house['price']

# Dividir em treino e teste
X_train_kc, X_test_kc, y_train_kc, y_test_kc = train_test_split(X_kc, y_kc, test_size=0.3, random_state=42)

# Treinar o modelo de regressão
model_kc = LinearRegression()
model_kc.fit(X_train_kc, y_train_kc)

# Fazer previsões
y_pred_kc = model_kc.predict(X_test_kc)

# Calcular métricas
mse_kc = mean_squared_error(y_test_kc, y_pred_kc)
r2_kc = r2_score(y_test_kc, y_pred_kc)

# Exibir métricas
st.write(f"Erro Quadrático Médio (MSE): **{mse_kc:.2f}**")
st.write(f"R² Score: **{r2_kc:.2f}**")

# Visualizar previsões vs. valores reais
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_test_kc, y_pred_kc, alpha=0.5)
ax.plot([y_test_kc.min(), y_test_kc.max()], [y_test_kc.min(), y_test_kc.max()], 'r--', lw=2)
ax.set_xlabel('Preço Real')
ax.set_ylabel('Preço Previsto')
ax.set_title('Preço Real vs. Preço Previsto')
st.pyplot(fig)

# --- Seção 6: Interatividade ---
st.header("🛠️ Faça sua Própria Previsão")

# Previsão para dados_ger.csv
st.subheader("Previsão de Comprador (dados_ger.csv)")
idade_input = st.slider("Idade", 18, 65, 30)
renda_input = st.slider("Renda (R$)", 1000, 15000, 5000)
genero_input = st.selectbox("Gênero", ["Masculino", "Feminino"])
genero_encoded = 1 if genero_input == "Masculino" else 0

# Fazer previsão
input_data = pd.DataFrame([[idade_input, renda_input, genero_encoded]], columns=['Idade', 'Renda', 'Gênero'])
pred_comprador = model_ger.predict(input_data)[0]
st.write(f"Previsão: **{'Comprador' if pred_comprador == 1 else 'Não Comprador'}**")

# Previsão para heart.csv
st.subheader("Previsão de Doença Cardíaca (heart.csv)")
age_input = st.slider("Idade", 29, 77, 50)
sex_input = st.selectbox("Sexo", ["Feminino", "Masculino"])
sex_encoded = 1 if sex_input == "Masculino" else 0
cp_input = st.slider("Tipo de Dor Torácica (0-3)", 0, 3, 0)
trestbps_input = st.slider("Pressão Arterial em Repouso (mm Hg)", 94, 200, 120)
chol_input = st.slider("Colesterol (mg/dl)", 126, 564, 200)
fbs_input = st.selectbox("Açúcar no Sangue > 120 mg/dl", ["Não", "Sim"])
fbs_encoded = 1 if fbs_input == "Sim" else 0
restecg_input = st.slider("Eletrocardiograma em Repouso (0-2)", 0, 2, 0)
thalach_input = st.slider("Frequência Cardíaca Máxima (bpm)", 71, 202, 150)
exang_input = st.selectbox("Angina Induzida por Exercício", ["Não", "Sim"])
exang_encoded = 1 if exang_input == "Sim" else 0
oldpeak_input = st.slider("Depressão ST", 0.0, 6.2, 1.0)
slope_input = st.slider("Inclinação do Segmento ST (0-2)", 0, 2, 1)
ca_input = st.slider("Número de Vasos Principais (0-3)", 0, 3, 0)
thal_input = st.slider("Defeito de Tálio (1-3)", 1, 3, 2)

# Fazer previsão
input_data_heart = pd.DataFrame([[age_input, sex_encoded, cp_input, trestbps_input, chol_input, fbs_encoded,
                                  restecg_input, thalach_input, exang_encoded, oldpeak_input, slope_input, ca_input, thal_input]],
                                columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
pred_heart = model_heart.predict(input_data_heart)[0]
st.write(f"Previsão: **{'Possui Doença Cardíaca' if pred_heart == 1 else 'Não Possui Doença Cardíaca'}**")