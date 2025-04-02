import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

WATSON_API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
