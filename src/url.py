import os

import cowsay
from dotenv import load_dotenv


def print_url():
  load_dotenv()
  URL = os.getenv("URL")
  cowsay.cow("Visit the URL below to add bot")
  print(f"\n{URL}\n")
