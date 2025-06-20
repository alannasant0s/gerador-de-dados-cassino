[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://betdata-generator.streamlit.app/)

Esse projeto foi criado a partir da minha necessidade de estudar utilizando dados do contexto o qual eu já estou inserida, que é o mercado Igaming.Essa aplicação gera dados fictícios de transações no contexto de casas de apostas. 

## Principais funcionalidades

- **Geração de transações financeiras realistas** exclusivamente via PIX
- **Controle preciso** sobre quantidade de registros (1 a 100.000 linhas)
- **Dados temporais estratégicos** com horários de pico de movimento
- **Múltiplas categorias** de operações:
  - Apostas esportivas
  - Jogos de cassino (roleta, blackjack, etc.)
  - Jogos de crash (Aviator, Mines, etc.)
  - Histórico completo de depósitos e saques
- **Status variados** de transação (completo, pendente, cancelado)

## Tecnologias que utilizei

### Backend:
- Python 3.10+
- Streamlit (para interface e lógica)
- Faker para geração de dados realistas
- Pandas para manipulação dos datasets

### Frontend:
- Streamlit Components (interface web)
- CSS personalizado para melhor experiência

### Ferramentas:
- Git para controle de versão
- GitHub para hospedagem do código
- Streamlit Cloud para deploy

## Como Você consegue utilizar?

### Opção 1: Acesse direto (recomendado)
Visite o app em produção:  
 [https://betdata-generator.streamlit.app/](https://betdata-generator.streamlit.app/)

### Opção 2: Execução local
```bash
# Clone o repositório
git clone https://github.com/alannasant0s/BetData-Generator.git

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
streamlit run main.py
