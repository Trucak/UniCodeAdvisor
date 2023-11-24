import re
import random
import pandas as pd
import sys
import time
import select

# Caminho para o arquivo Excel
caminho_excel = r'/Users/tomasmartim/Desktop/Projetos Pessoais/UniCodeAdvisor/cna23_1f_resultados.xls'

# Carregar dados do Excel, pulando a primeira linha
dados_excel = pd.read_excel(caminho_excel, skiprows=1)

# Criar base de dados a partir do Excel
universidades_cursos = {}
for index, row in dados_excel.iterrows():
    # Use índices numéricos para acessar as colunas corretas
    universidade = row[3]  # Índice da coluna D (universidades)
    curso = row[4]  # Índice da coluna E (cursos)

    if pd.notna(universidade) and pd.notna(curso):
        if universidade not in universidades_cursos:
            universidades_cursos[universidade] = [curso]
        else:
            universidades_cursos[universidade].append(curso)

def responder_pergunta(pergunta):
    # Verificar se a pergunta contém o nome de algum curso e palavras-chave
    curso_presente = any(c.lower() in pergunta.lower() for cursos in universidades_cursos.values() for c in cursos)
    palavras_chave_presentes = any(palavra_chave in pergunta.lower() for palavra_chave in ['instituição','instituições','faculdade','faculdades','universidade','universidades'])

    if curso_presente and palavras_chave_presentes:
        palavra_chave_plural = next((p for p in ['instituicoes', 'faculdades', 'universidades'] if p in pergunta.lower()), 'instituicoes')
        resposta = obter_resposta_por_instituicoes(pergunta, palavra_chave_plural)
    else:
        resposta = 'Não foram encontradas instituições que ofereçam o curso mencionado na pergunta ou as palavras-chave necessárias.'

    return resposta

def obter_resposta_por_instituicoes(pergunta, palavra_chave_plural):
    instituicoes_com_curso = [u for u, cursos in universidades_cursos.items() if any(c.lower() in pergunta.lower() for c in cursos)]
    
    if instituicoes_com_curso:
        resposta = f'O curso está disponível nas seguintes {palavra_chave_plural}:\n'
        resposta += '\n'.join([f'{i + 1}. {instituicao}' for i, instituicao in enumerate(instituicoes_com_curso)])
    else:
        resposta = f'Não foram encontradas {palavra_chave_plural} que ofereçam o curso mencionado na pergunta.'

    return resposta

def imprimir_com_atraso(texto, atraso=0.01):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(atraso)
    print()

# Loop principal
while True:
    pergunta = input('Tu: ')
    if pergunta.lower() == 'sair':
        print('Chatbot encerrado.')
        break

    resposta = responder_pergunta(pergunta)
    imprimir_com_atraso('Chatbot: ' + resposta)