import random

def text_to_dict(file):
  with open(file, 'r', encoding='utf-8') as file:
    dict = {}
    for line in file:
      parts = line.strip().split('. ', 1)
      if len(parts) == 2:
        key = int(parts[0])
        value = str(parts[1])
        dict[key] = value
  return dict

def get_frogfact(file):
  # with open('resources/responses.txt', 'r', encoding='utf-8') as file:
  #   responses = file.readlines()
  # random_response = random.choice(responses).strip()
  facts_dict = text_to_dict(file)
  random_entry = random.choice(list(facts_dict.items()))
  random_response = random_entry[1]
  return random_response

# print(text_to_dict('resources/responses.txt'))
# print(get_frogfact('resources/responses.txt'))