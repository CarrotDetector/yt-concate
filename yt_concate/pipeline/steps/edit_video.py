from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from .step import Step


class EditVideo(Step):

    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

        
        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'],
                                                    inputs['search_word'])
        final_clip.write_videofile(output_filepath)


    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_string(start), self.parse_time_string(end)

    def parse_time_string(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000
        # return 多個用逗點分隔時會自動當成tuple



