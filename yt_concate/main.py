import sys,os
sys.path.append(os.getcwd()) # 將此檔案上層的資料夾加入sys path

from yt_concate.pipeline.steps.download_captions import DownloadCaptions # 為了將路徑加入syspath 防止import絕對路徑時的錯誤
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils


CHANNEL_ID = 'UCqECaJ8Gagnn7YCbPEzWH6g'  # 頻道id


def main():
    inputs = {
        "channel_id": CHANNEL_ID,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils =Utils()
    p = Pipeline(steps)
    p.run(inputs,utils)


if __name__ == "__main__":
    main()
