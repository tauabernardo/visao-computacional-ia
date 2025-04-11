# Projeto de Classificação e Clusterização com IA Generativa

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red) ![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-orange)

Bem-vindo ao **Projeto de Classificação e Clusterização com IA Generativa**! Este é um aplicativo web interativo que usa inteligência artificial (IA) para analisar dados e fazer previsões úteis sobre clientes, saúde e preços de casas. Desenvolvido com Python e Streamlit, ele é fácil de usar e exibe resultados com gráficos claros, mesmo para quem não entende de programação.

## 📖 Descrição do Projeto

Imagine que você quer entender melhor seus clientes, prever riscos de saúde ou estimar o valor de uma casa. Este projeto é como um assistente inteligente que analisa informações e te ajuda a tomar decisões mais acertadas! Ele faz três coisas principais:

1. **Análise de Clientes**:
   - Usa dados como idade, renda e gênero para prever se alguém é um "comprador" (gasta bastante) ou não.
   - Agrupa clientes parecidos (ex.: jovens com renda alta) para direcionar estratégias de marketing.

2. **Previsão de Saúde**:
   - Analisa informações médicas, como colesterol e pressão arterial, para prever se uma pessoa tem risco de problemas cardíacos.
   - Ajuda a identificar quem precisa de mais cuidados.

3. **Estimativa de Preços de Casas**:
   - Com base em detalhes como número de quartos e tamanho, estima o valor de casas.
   - Útil para compradores, vendedores ou investidores.

O projeto usa **inteligência artificial** (modelos como Random Forest, K-Means e Regressão Linear) para estudar os dados e encontrar padrões. Tudo é mostrado em uma página web interativa, onde você pode inserir informações e ver previsões na hora, com gráficos que explicam os resultados de forma simples.

### Por que é legal?
- **Fácil de usar**: Não precisa ser expert em tecnologia! Basta clicar em botões e ajustar sliders.
- **Visual e interativo**: Gráficos mostram como os dados são agrupados ou quão boas são as previsões.
- **Prático**: Ajuda em decisões reais, como vender mais, cuidar da saúde ou investir em imóveis.

## 🚀 Como Começar

### Pré-requisitos
- **Python 3.8+** instalado ([baixe aqui](https://www.python.org/downloads/)).
- Navegador web (ex.: Chrome, Firefox).
- Os arquivos de dados (`dados_ger.csv`, `heart.csv`, `kc_house_data.csv`) na estrutura correta.

### Estrutura do Repositório
projeto-classificacao-clusterizacao-ia/
├── parte_ii/
│   ├── datasets/
│   │   ├── heart.csv
│   │   └── kc_house_data.csv
│   └── dados_ger.csv
├── scripts/
│   ├── gerar_dados_ger.py
│   └── app.py
├── requirements.txt
├── README.md
└── .gitignore


4. **Outros Arquivos**:
- Crie um `requirements.txt` com:
streamlit>=1.0.0
pandas>=2.0.0
numpy>=1.21.0
scikit-learn>=1.0.0
seaborn>=0.11.0
matplotlib>=3.4.0
faker>=8.0.0

- Crie um `.gitignore` com:
pycache/
*.pyc
venv/
*.csv

  
Se precisar de ajuda para criar outros arquivos (ex.: `requirements.txt`) ou ajustar algo no README, é só avisar!




