import time
import concurrent.futures
from pytube import YouTube
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            for yt in data:
                if inputs['fast']:
                    if utils.caption_file_exists(yt):
                        print(f'found existing caption file{yt.id}')
                        continue
                # print('downloading caption for', yt.id)
                executor.submit(self.download_caption,yt)    
        end = time.time()
        print('took', end - start, 'seconds')
        return data

    def download_caption(self,yt):
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code(
                    'a.en')  # 取得英文字幕
                en_caption_convert_to_srt = (
                    en_caption.generate_srt_captions())
                text_file = open(yt.caption_filepath,
                                    "w",
                                    encoding='utf-8')
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
                print(f'OK url    :{yt.url}')
            except (AttributeError):#KeyError,
                print(f'ERROR URL :{yt.url}')
