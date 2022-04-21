import time
from pytube import YouTube
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code(
                    'a.en')  # 取得英文字幕
                en_caption_convert_to_srt = (
                    en_caption.generate_srt_captions())
                text_file = open(utils.get_caption_path(yt.url),
                                 "w",
                                 encoding='utf-8')
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
                print(f'OK url:{yt.url}')
            except (KeyError, AttributeError):
                print(f'ERROR URL:{yt.url}')
        end = time.time()
        print('took', end - start, 'seconds')
        return data