import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

ORIGINAL_DATA_PATH = "data/data.json"
EXTENDED_DATA_PATH = "data/extended_data.json"
