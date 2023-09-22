import random

import src


def get_frogfact(file):
  # with open('resources/responses.txt', 'r', encoding='utf-8') as file:
  #   responses = file.readlines()
  # random_response = random.choice(responses).strip()
  facts_dict = src.text_to_dict(file)
  random_entry = random.sample(facts_dict.items(), 1)
  print(random_entry)
  random_response = random_entry[0][1]
  return random_response
