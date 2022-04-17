import sys,os # 為了將路徑加入syspath 防止import絕對路徑時的錯誤
sys.path.append(os.getcwd()) # 將此檔案上層的資料夾加入sys path

from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException

CHANNEL_ID = 'UCqECaJ8Gagnn7YCbPEzWH6g'  # 頻道id


def main():
    inputs = {
        "channel_id": CHANNEL_ID,
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
