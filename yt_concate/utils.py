import os
import shutil

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUT_DIR


class Utils:

    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # 建立資料夾 已存在ok
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_output_filepath(self, channel_id, search_word):
        filename = channel_id + '_' + search_word + '.mp4'
        return os.path.join(OUTPUT_DIR, filename)

    def remove_download(self,channel_id):
        shutil.rmtree(CAPTIONS_DIR)
        print(f'remove:{CAPTIONS_DIR}')
        shutil.rmtree(VIDEOS_DIR)
        print(f'remove:{VIDEOS_DIR}')
        os.remove(self.get_video_list_filepath(channel_id))
        print(f'remove:{self.get_video_list_filepath(channel_id)}')
