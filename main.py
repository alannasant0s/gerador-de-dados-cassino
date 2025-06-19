from datetime import datetime, timedelta
import streamlit as st
from faker import Faker
import pandas as pd
import random

# Configuração inicial
fake = Faker('pt_BR')

def configurar_pagina():
    """Configurações visuais da aplicação"""
    st.set_page_config(
        page_title="Gerador de Dados para Apostas",
        page_icon="🎲",
        layout="centered",
    )

def criar_dados_apostas(categoria, num_linhas, num_colunas):
    """Gera dados realistas para operações de plataforma de apostas"""
    dados = []
    
    # Dicionários de dados
    esportes = ['Futebol', 'Basquete', 'Tênis', 'Vôlei', 'Futebol Americano']
    jogos_cassino = ['Roleta', 'Blackjack', 'Poker', 'Baccarat', 'Caça-Níqueis']
    jogos_crash = ['Aviator', 'Crash', 'Mines', 'Dice', 'Plinko']
    
    for _ in range(num_linhas):
        registro = criar_registro_base()
        
        if categoria == 'Apostas Esportivas':
            registro.update(criar_dados_esportivos(esportes))
        elif categoria == 'Jogos de Cassino':
            registro.update(criar_dados_cassino(jogos_cassino))
        elif categoria == 'Jogos de Crash':
            registro.update(criar_dados_crash(jogos_crash))
        elif categoria == 'Depósitos':
            registro.update(criar_dados_deposito())
        elif categoria == 'Saques':
            registro.update(criar_dados_saque())
        elif categoria == 'Transações':
            registro.update(criar_dados_transacao())
        
        # Limita as colunas conforme solicitado
        dados.append(dict(list(registro.items())[:num_colunas]))
    
    return pd.DataFrame(dados)

def criar_registro_base():
    """Cria os dados básicos comuns a todos os registros"""
    return {
        'ID do Usuário': fake.uuid4()[:8],
        'Nome do Usuário': fake.user_name(),
        'Email': fake.email(),
        'CPF': fake.cpf(),
        'País': 'Brasil',
        'Estado': fake.estado_sigla(),
        'Cidade': fake.city(),
        'Data de Cadastro': fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y'),
        'Status da Conta': random.choice(['Ativa', 'Inativa', 'Verificação Pendente']),
        'VIP': random.choice(['Bronze', 'Prata', 'Ouro', 'Não VIP'])
    }

def criar_dados_esportivos(esportes):
    """Gera dados específicos para apostas esportivas"""
    valor_aposta = round(random.uniform(10.0, 1000.0), 2)
    odds = round(random.uniform(1.2, 10.0), 2)
    status = random.choice(['Ganha', 'Perdida', 'A Decorrer'])
    
    return {
        'Esporte': random.choice(esportes),
        'Evento': f"{fake.city()} vs {fake.city()}",
        'Mercado': random.choice(['Vencedor', 'Total de Gols', 'Ambos Marcam']),
        'Seleção': random.choice(['Casa', 'Fora', 'Empate']),
        'Odds': odds,
        'Valor da Aposta (R$)': valor_aposta,
        'Possível Retorno (R$)': round(valor_aposta * odds, 2),
        'Data/Hora da Aposta': fake.date_time_between(start_date='-30d', end_date='now').strftime('%d/%m/%Y %H:%M'),
        'Status': status,
        'Valor Ganho (R$)': round(valor_aposta * odds, 2) if status == 'Ganha' else 0.00
    }

def criar_dados_cassino(jogos):
    """Gera dados para jogos de cassino tradicionais"""
    valor_aposta = round(random.uniform(5.0, 500.0), 2)
    multiplicador = round(random.uniform(1.0, 100.0), 2)
    
    return {
        'Jogo': random.choice(jogos),
        'Valor da Aposta (R$)': valor_aposta,
        'Multiplicador': multiplicador,
        'Valor Ganho (R$)': round(valor_aposta * multiplicador, 2) if random.random() > 0.6 else 0.00,
        'Data/Hora da Jogada': fake.date_time_between(start_date='-30d', end_date='now').strftime('%d/%m/%Y %H:%M'),
        'Status': 'Concluído',
        'Provedor': random.choice(['Evolution', 'Playtech', 'Pragmatic Play'])
    }

def criar_dados_crash(jogos):
    """Gera dados para jogos de crash"""
    valor_aposta = round(random.uniform(5.0, 1000.0), 2)
    multiplicador = round(random.uniform(1.0, 50.0), 2)
    
    return {
        'Jogo': random.choice(jogos),
        'Valor da Aposta (R$)': valor_aposta,
        'Multiplicador': multiplicador,
        'Valor Ganho (R$)': round(valor_aposta * multiplicador, 2) if random.random() > 0.5 else 0.00,
        'Data/Hora da Jogada': fake.date_time_between(start_date='-30d', end_date='now').strftime('%d/%m/%Y %H:%M'),
        'Status': 'Concluído',
        'Cashout Automático': random.choice(['Sim', 'Não'])
    }

def criar_dados_deposito():
    """Gera dados de depósito via PIX"""
    valor = round(random.uniform(50.0, 5000.0), 2)
    
    return {
        'Método de Pagamento': 'PIX',
        'Valor (R$)': valor,
        'Taxa (R$)': 0.00,
        'Valor Líquido (R$)': valor,
        'Data/Hora': fake.date_time_between(start_date='-30d', end_date='now').strftime('%d/%m/%Y %H:%M'),
        'Status': 'Concluído',
        'ID da Transação': fake.uuid4()[:8],
        'Chave PIX': gerar_chave_pix(),
        'Bônus Recebido (R$)': round(valor * 0.1, 2) if random.random() > 0.7 else 0.00
    }

def criar_dados_saque():
    """Gera dados de saque via PIX"""
    valor = round(random.uniform(100.0, 10000.0), 2)
    data_solicitacao = fake.date_time_between(start_date='-30d', end_date='now')
    status = random.choices(
        ['Concluído', 'Cancelado', 'Pendente'],
        weights=[0.9, 0.05, 0.05],
        k=1
    )[0]
    
    registro = {
        'Método de Pagamento': 'PIX',
        'Valor Solicitado (R$)': valor,
        'Taxa (R$)': 0.00,
        'Valor Líquido (R$)': valor,
        'Data/Hora da Solicitação': data_solicitacao.strftime('%d/%m/%Y %H:%M'),
        'Status': status,
        'ID da Transação': fake.uuid4()[:8],
        'Chave PIX': gerar_chave_pix()
    }
    
    if status == 'Concluído':
        registro['Data/Hora da Conclusão'] = (data_solicitacao + timedelta(minutes=random.randint(1, 30))).strftime('%d/%m/%Y %H:%M')
    else:
        registro['Data/Hora da Conclusão'] = '-'
        registro['Motivo'] = fake.sentence() if status == 'Cancelado' else '-'
    
    return registro

def criar_dados_transacao():
    """Gera dados consolidados de transações"""
    tipo = random.choices(['Depósito', 'Saque'], weights=[0.6, 0.4], k=1)[0]
    valor = round(random.uniform(50.0, 5000.0), 2) if tipo == 'Depósito' else round(random.uniform(100.0, 10000.0), 2)
    
    registro = {
        'Tipo': tipo,
        'Método de Pagamento': 'PIX',
        'Chave PIX': gerar_chave_pix(),
        'Valor (R$)': valor,
        'Taxa (R$)': 0.00,
        'Data/Hora': fake.date_time_between(start_date='-30d', end_date='now').strftime('%d/%m/%Y %H:%M'),
        'ID da Transação': fake.uuid4()[:8],
        'Saldo Anterior (R$)': round(random.uniform(0.0, 50000.0), 2)
    }
    
    if tipo == 'Depósito':
        registro['Status'] = 'Concluído'
        registro['Novo Saldo (R$)'] = registro['Saldo Anterior (R$)'] + valor
    else:
        registro['Status'] = random.choices(
            ['Concluído', 'Cancelado'],
            weights=[0.9, 0.1],
            k=1
        )[0]
        registro['Novo Saldo (R$)'] = registro['Saldo Anterior (R$)'] - valor if registro['Status'] == 'Concluído' else registro['Saldo Anterior (R$)']
    
    return registro

def gerar_chave_pix():
    """Gera uma chave PIX aleatória"""
    return random.choice([
        fake.cpf(),
        fake.email(),
        f"+55{fake.msisdn()[3:]}",
        str(random.randint(10000000000000, 99999999999999))
    ])

def mostrar_interface():
    """Exibe a interface do usuário"""
    st.title('🎲 Gerador de Dados para Plataforma de Apostas')
    
    st.write("""
    ### Oie galera me chamo Alanna. Trabalho no mercado igaming e estou em transição de carreira para tecnologia.
    Desenvolvi esta ferramenta para construir projetos e estudar utilizando informações do contexto que já estou inserida. O objetivo do programa é gerar dados ficticios de plataformas de apostas esportivas e cassinos.
    Use os controles abaixo para criar os dados que precisar.
    """)
    
    st.markdown("---")
    
    categoria = st.selectbox(
        '**Selecione o tipo de operação**',
        ['Apostas Esportivas', 'Jogos de Cassino', 'Jogos de Crash', 
         'Depósitos', 'Saques', 'Transações']
    )
    
    col1, col2 = st.columns(2)
    with col1:
        num_linhas = st.slider('**Quantidade de registros**', 1, 1000, 50)
    with col2:
        num_colunas = st.slider('**Número de colunas**', 1, 20, 10)
    
    if st.button('**Gerar Dados**', type="primary"):
        st.markdown("---")
        st.subheader("Resultados Gerados")
        
        with st.spinner('Criando dados...'):
            dados = criar_dados_apostas(categoria, num_linhas, num_colunas)
            st.dataframe(dados, use_container_width=True)
            
            st.download_button(
                label="📥 Baixar como CSV",
                data=dados.to_csv(index=False, sep=';').encode('utf-8'),
                file_name=f'dados_apostas_{categoria.lower().replace(" ", "_")}.csv',
                mime='text/csv',
            )
    
    st.markdown("---")
    st.write("""
    ### Sobre este projeto
    Desenvolvido com ❤️ por **Alanna Santos**  
    [![GitHub](https://img.shields.io/badge/Meu_GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/alannasant0s)
    
    *Dados fictícios para fins educacionais e de desenvolvimento*
    """)

# Configuração e execução
configurar_pagina()
mostrar_interface()