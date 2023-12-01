import re
import random
import sys
import time
import select
from database import universities_courses

def respond_to_question(question):
    response = 'Hello'
    return response

def print_with_delay(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

while True:
    question = input('You: ')
    if question.lower() == 'exit':
        print('Chatbot closed.')
        break

    answer = respond_to_question(question)
    print_with_delay('Chatbot: ' + answer)