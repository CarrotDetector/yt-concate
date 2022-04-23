import sys, os

sys.path.append(os.getcwd())  # 將此檔案上層的資料夾加入sys path
# 為了將路徑加入syspath 防止import絕對路徑時的錯誤

from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils

CHANNEL_ID = 'UCqECaJ8Gagnn7YCbPEzWH6g'  # 頻道id


def main():
    inputs = { # 儲存要傳入的參數 for pipeline
        'channel_id': CHANNEL_ID,
        'search_word':'love',
        'limit':20,
    }
    steps = [  #儲存每一個步驟 for pipeline
        Preflight(),  #
        GetVideoList(),  # 取得影片清單
        InitializeYT(),  # 將YT物件產出
        DownloadCaptions(),  # 下載字幕
        ReadCaption(),  # 讀取字幕
        Search(),  # 搜尋
        DownloadVideos(),  #下載影片
        EditVideo(),  # 編輯影片
        Postflight(),  #
    ]

    utils = Utils()  # 建立utils 實例
    p = Pipeline(steps)  # 將steps 一個一個產生實例
    p.run(inputs, utils)  # 執行每個step(傳入inputs跟utils實例)

 
if __name__ == "__main__":
    main()
