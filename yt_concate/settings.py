import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")  # 使用環境變數取得 api key