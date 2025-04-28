import os
from dotenv import load_dotenv

load_dotenv()

RETAILCRM_API_URL = os.getenv('RETAILCRM_API_URL')
RETAILCRM_API_KEY = os.getenv('RETAILCRM_API_KEY')