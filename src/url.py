from dotenv import load_dotenv
import cowsay
import os

def print_url():
    load_dotenv()
    URL = os.getenv("URL")
    cowsay.cow(f"Visit the URL below to add bot")
    print(f"\n{URL}\n")