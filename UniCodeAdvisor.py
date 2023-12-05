from imports import *

def find_courses_in_universities(course_name):
    matching_universities = []
    for university, courses in universities_courses.items():
        for course, _ in courses:
            if re.search(rf'\b{re.escape(course_name)}\b', course, re.IGNORECASE) and course.lower() == course_name.lower():
                matching_universities.append(university)

    return matching_universities

def extract_course_name(question):
    match = re.search(r'curso(?: de)? (.+?)\??$', question, re.IGNORECASE)
    return match.group(1) if match else None

def contains_institution_keywords(question):
    institution_keywords = ['faculdade', 'faculdades', 'instituição', 'instituições', 'universidade', 'universidades']
    return any(keyword in question.lower() for keyword in institution_keywords)

def respond_to_question(username, question):
    if question.lower() == 'delete':
        confirm_delete = input("Você tem certeza que deseja apagar o histórico? (sim/não): ")
        if confirm_delete.lower() == 'sim':
            try:
                os.remove(f"{username}_history.txt")
                answer = "Histórico apagado com sucesso."
            except FileNotFoundError:
                answer = "Histórico não encontrado. Como posso ajudar agora?"
        else:
            answer = "Entendi, vou manter o histórico. Como posso ajudar agora?"
    elif contains_institution_keywords(question.lower()) and "curso" in question.lower():
        course_name = extract_course_name(question)
        if course_name:
            universities = find_courses_in_universities(course_name)
            if universities:
                response = [f"- {university}\n" if university != universities[-1] else f"- {university}" for university in universities]
                answer = f"O curso '{course_name}' é oferecido por:\n{''.join(response)}"
            else:
                answer = f"Desculpe, não encontrei faculdades que ofereçam o curso '{course_name}'."
        else:
            answer = "Desculpe, não consegui identificar o curso na pergunta."
    else:
        answer = "Desculpe, não entendi a pergunta."

    with open(f"{username}_history.txt", 'a') as file:
        file.write(f'Tu: {question}\nChatbot: {answer}\n')

    return answer

def display_user_history(username):
    try:
        with open(f"{username}_history.txt", 'r') as file:
            content = file.read()
            print(f"Histórico para {username}:\n{content}")
    except FileNotFoundError:
        print(f"Histórico para {username} não encontrado.")


def print_with_delay(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

username = input('Digite seu username: ')
display_user_history(username)

while True:
    question = input('Tu: ')
    if question.lower() == 'sair':
        print('Chatbot fechado.')
        break

    answer = respond_to_question(username, question)
    print_with_delay('Chatbot: ' + answer)