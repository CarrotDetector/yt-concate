import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")  # 使用環境變數取得 api key

DOWNLOADS_DIR = "downloads"
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR,"videos")
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR,"captions")

