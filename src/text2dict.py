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


# print(text_to_dict('resources/responses.txt'))
