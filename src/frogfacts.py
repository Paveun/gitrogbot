import random


def get_frogfact():
  with open('resources/responses.txt', 'r', encoding='utf-8') as file:
    responses = file.readlines()
  random_response = random.choice(responses).strip()
  return random_response
