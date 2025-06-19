[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://betdata-generator.streamlit.app/)

Projeto full stack para geração de dados fictícios de transações financeiras no contexto de casas de apostas. Desenvolvido para auxiliar nos meus estudos em análises de dados e desenvolvimento full stack. Simulando operações reais como depósitos, saques e apostas.

## Principais funcionalidades

- **Geração de transações financeiras realistas** exclusivamente via PIX
- **Controle preciso** sobre quantidade de registros (1 a 10.000 linhas)
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
git clone https://github.com/alannasant0s/gerador-de-dados-cassino.git

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
streamlit run main.py
