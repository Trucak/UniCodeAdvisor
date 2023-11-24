import random

# Dados sobre universidades e cursos
universidades_cursos = {
    'universidade1': ['curso1', 'curso2', 'curso3'],
    'universidade2': ['curso4', 'curso5', 'curso6'],

}

# Respostas sobre suporte técnico de informática
suporte_tecnico_respostas = [
    'Tente reiniciar o computador.',
    'Verifique se os drivers estão atualizados.',
    'Você já tentou desligar e ligar novamente?',
]

# Informações sobre linguagens de programação
linguagens_programacao = {
    'python': 'Python é uma linguagem de programação de alto nível e fácil de aprender.',
    'java': 'Java é uma linguagem de programação popular, usada em diversos contextos.',
    'javascript': 'JavaScript é uma linguagem de script amplamente usada para desenvolvimento web.',
 
}

def responder_pergunta(pergunta):
    if 'universidade' in pergunta.lower() and 'curso' in pergunta.lower():
        return obter_resposta_universidades_cursos()

    elif 'suporte técnico' in pergunta.lower() or 'informática' in pergunta.lower():
        return random.choice(suporte_tecnico_respostas)

    elif 'linguagem de programação' in pergunta.lower():
        return obter_resposta_linguagens_programacao()

    else:
        return 'Desculpe, não entendi a pergunta.'

def obter_resposta_universidades_cursos():
    universidade = random.choice(list(universidades_cursos.keys()))
    curso = random.choice(universidades_cursos[universidade])
    resposta = f'Na {universidade}, o curso oferecido é {curso}.'
    return resposta

def obter_resposta_linguagens_programacao():
    linguagem = random.choice(list(linguagens_programacao.keys()))
    informacao = linguagens_programacao[linguagem]
    resposta = f'Sobre {linguagem.capitalize()}: {informacao}'
    return resposta

# Loop principal
while True:
    pergunta = input('Você: ')
    if pergunta.lower() == 'sair':
        print('Chatbot encerrado.')
        break

    resposta = responder_pergunta(pergunta)
    print('Chatbot:', resposta)