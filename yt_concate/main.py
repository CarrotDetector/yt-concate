# API KEY
import urllib.request
import json
import sys,os # 為了將路徑加入syspath 防止import絕對路徑時的錯誤
sys.path.append(os.getcwd()) # 將此檔案上層的資料夾加入sys path
from yt_concate.settings import API_KEY


CHANNEL_ID = 'UCqECaJ8Gagnn7YCbPEzWH6g'  # 頻道id

def get_all_video_in_channel(channel_id):
    api_key = ''  # 輸入自己的api key
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
        api_key, channel_id)

    video_links = []
    url = first_url
    while True:

        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


#video_list = get_all_video_in_channel(CHANNEL_ID)
#print(video_list)  # 顯示影片清單
#print(len(video_list))  # 顯示影片清單筆數
