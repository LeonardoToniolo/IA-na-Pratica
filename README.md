![IA na Prática - Capa](images/IA%20NA%20PR%C3%81TICA%20-%20CAPA.png)

# 📈 Stock Market Newsletter Generator

Este projeto cria uma **newsletter automatizada** que monitora e analisa oscilações no preço de ações e as principais notícias relacionadas a uma empresa específica no mercado de ações. Utilizando tecnologias de ponta como **GPT**, **Python** e **crewAI**, o projeto foi desenvolvido como parte do evento **IA na Prática**.

## 🚀 Objetivo

Desenvolver uma aplicação completa que analisa dados financeiros e notícias, e automaticamente gera uma newsletter informativa e bem estruturada. Este projeto é ideal para aprimorar suas habilidades técnicas em programação, análise de dados e inteligência artificial.

## 🛠️ Ferramentas Utilizadas

- **GPT-3.5**: Para a geração de conteúdo automatizado da newsletter.
- **Python**: Para desenvolvimento do backend, manipulação de dados, e integração com APIs financeiras.
- **crewAI**: Para automatizar e gerenciar agentes de IA que realizam tarefas específicas dentro do projeto.

### 📦 Bibliotecas Necessárias

- `yfinance==0.2.41`
- `crewai==0.28.8`
- `crewai[Tools]`
- `langchain==0.1.20`
- `langchain-openai==0.1.7`
- `langchain-community==0.0.38`
- `duckduckgo-search==5.3.0`

### 📋 Funcionalidades

1. **Análise de Preço das Ações**: Utiliza dados históricos de ações da Yahoo Finance para identificar tendências.
2. **Análise de Notícias**: Monitora e resume as notícias relacionadas à empresa, avaliando o impacto potencial dessas informações.
3. **Geração de Newsletter**: Com base nos dados analisados, gera automaticamente uma newsletter que resume as informações mais relevantes e oferece previsões sobre o futuro.

### 📂 Estrutura do Projeto

```bash
|-- images/
|   |-- IA NA PRÁTICA - CAPA.png
|-- notebook/
|   |-- stock_newsletter_generator.ipynb
|-- README.md
|-- requirements.txt
```

- **images/IA NA PRÁTICA - CAPA.png**: Imagem da capa utilizada no README.
- **notebook/stock_newsletter_generator.ipynb**: Contém o código Jupyter Notebook para execução do projeto.
- **README.md**: Este arquivo, que contém informações sobre o projeto.
- **requirements.txt**: Lista de dependências do Python.

### 🚀 Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/yourusername/stock-newsletter-generator.git
   cd stock-newsletter-generator
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Abra o Jupyter Notebook:**

   ```bash
   jupyter notebook notebook/stock_newsletter_generator.ipynb
   ```

4. **Execute as células do notebook para gerar a newsletter:**

   O resultado final da análise será apresentado diretamente no notebook.

### 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou novas funcionalidades.