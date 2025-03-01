import os
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_API_KEY = os.getenv("HEADLINER_NEWSAPI_API_KEY")
