Projeto de Classificação e Clusterização com IA Generativa
   

Bem-vindo ao Projeto de Classificação e Clusterização com IA Generativa! Este é um aplicativo web interativo que usa inteligência artificial (IA) para analisar dados e fazer previsões úteis sobre clientes, saúde e preços de casas. Desenvolvido com Python e Streamlit, ele é fácil de usar e exibe resultados com gráficos claros, mesmo para quem não entende de programação.

📖 Descrição do Projeto
Imagine que você quer entender melhor seus clientes, prever riscos de saúde ou estimar o valor de uma casa. Este projeto é como um assistente inteligente que analisa informações e te ajuda a tomar decisões mais acertadas! Ele faz três coisas principais:

Análise de Clientes:
Usa dados como idade, renda e gênero para prever se alguém é um "comprador" (gasta bastante) ou não.
Agrupa clientes parecidos (ex.: jovens com renda alta) para direcionar estratégias de marketing.
Previsão de Saúde:
Analisa informações médicas, como colesterol e pressão arterial, para prever se uma pessoa tem risco de problemas cardíacos.
Ajuda a identificar quem precisa de mais cuidados.
Estimativa de Preços de Casas:
Com base em detalhes como número de quartos e tamanho, estima o valor de casas.
Útil para compradores, vendedores ou investidores.
O projeto usa inteligência artificial (modelos como Random Forest, K-Means e Regressão Linear) para estudar os dados e encontrar padrões. Tudo é mostrado em uma página web interativa, onde você pode inserir informações e ver previsões na hora, com gráficos que explicam os resultados de forma simples.

Por que é legal?
Fácil de usar: Não precisa ser expert em tecnologia! Basta clicar em botões e ajustar sliders.
Visual e interativo: Gráficos mostram como os dados são agrupados ou quão boas são as previsões.
Prático: Ajuda em decisões reais, como vender mais, cuidar da saúde ou investir em imóveis.
🚀 Como Começar
Pré-requisitos
Python 3.8+ instalado (baixe aqui).
Navegador web (ex.: Chrome, Firefox).
Os arquivos de dados (dados_ger.csv, heart.csv, kc_house_data.csv) na estrutura correta.
Estrutura do Repositório
text

Recolher

Encapsular

Copiar
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
Instalação
Clone o repositório:
bash

Recolher

Encapsular

Copiar
git clone https://github.com/SEU_USUARIO/projeto-classificacao-clusterizacao-ia.git
cd projeto-classificacao-clusterizacao-ia
Crie um ambiente virtual (opcional, mas recomendado):
bash

Recolher

Encapsular

Copiar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:
bash

Recolher

Encapsular

Copiar
pip install -r requirements.txt
Isso instala bibliotecas como streamlit, pandas, scikit-learn, seaborn e outras.
Gere o arquivo dados_ger.csv:
Execute o script de geração:
bash

Recolher

Encapsular

Copiar
python scripts/gerar_dados_ger.py
Isso cria parte_ii/dados_ger.csv com dados simulados de clientes.
Obtenha os outros datasets:
Baixe heart.csv e kc_house_data.csv (ex.: de fontes como Kaggle).
Coloque-os em parte_ii/datasets/:
text

Recolher

Encapsular

Copiar
parte_ii/datasets/heart.csv
parte_ii/datasets/kc_house_data.csv
Executando o Projeto
Inicie o aplicativo Streamlit:
bash

Recolher

Encapsular

Copiar
streamlit run scripts/app.py
Acesse no navegador:
Abra o link mostrado no terminal (geralmente http://localhost:8501).
Navegue pelas seções para ver análises, gráficos e fazer suas próprias previsões!
Como Usar
Análise de Clientes: Veja se uma pessoa é um comprador com base em idade, renda e gênero.
Saúde do Coração: Insira dados médicos para prever riscos cardíacos.
Preço de Casas: Informe características de uma casa para estimar seu valor.
Use os sliders e menus na seção "Faça sua Própria Previsão" para testar cenários e ver resultados instantâneos.
📊 Exemplos de Resultados
Gráficos: Veja como os clientes são agrupados por idade e renda ou como as previsões de saúde são precisas.
Métricas: Descubra a acurácia (quantas vezes a IA acerta) e outros números que mostram o desempenho.
Interatividade: Ajuste valores (ex.: renda de R$5000) e veja se a pessoa é classificada como comprador.
