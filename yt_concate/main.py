import sys, os
import distutils.util

sys.path.append(os.getcwd())  # 將此檔案上層的資料夾加入sys path
# 為了將路徑加入syspath 防止import絕對路徑時的錯誤
import getopt

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

# CHANNEL_ID = 'UCqECaJ8Gagnn7YCbPEzWH6g'  # 頻道id

def print_usage():
    print('python main.py OPTIONS')
    print('OPTIONS:')
    print('{:>6}{:<15}{}'.format('-i', '--channel_id', '要搜尋的的頻道 id'))
    print('{:>6}{:<15}{}'.format('-s', '--search_word', '要搜尋的字/詞'))
    print('{:>6}{:<15}{}'.format('-l', '--limit', '合併影片的最高片段數量'))
    print('{:>6}{:<15}{}'.format('-c', '--cleanup',
                                 '結果檔產生後，刪除程式執行中產生的檔案(True),不刪除檔案(False)'))
    print('{:>6} {:<15}{}'.format('-f', '--fast',
                                 '程式執行中會先檢查檔案(True)，重新下載所需檔案(False)'))

def main():
    inputs = { # 儲存要傳入的參數 for pipeline
        'channel_id': '',
        'search_word':'',
        'limit':'',
        'cleanup':False,
        'fast':True,
    }

    argv = sys.argv[1:]
    print(argv)
    short_opts = 'hi:s:l:c:f:'
    long_opts = 'help channel_id= search_word= limit= cleanup= fast='.split()

    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ("-i", "--channel_id"):
            inputs['channel_id'] = arg
        elif opt in ("-s", "--search_word"):
            inputs['search_word'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = int(arg)
        elif opt in ("-c", "--cleanup"):
            inputs['cleanup'] = bool(distutils.util.strtobool(arg))
        elif opt in ("-f", "--fast"):
            inputs['fast'] = bool(distutils.util.strtobool(arg))
        # print(arg)

    if not inputs['channel_id'] or not inputs['search_word'] or not inputs['limit']:
        print('channel_id、search_word、limit三個為必填參數')
        print_usage()
        sys.exit(2)

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
