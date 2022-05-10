from yt_concate.pipeline.steps.step import Step


class Postflight(Step):
    def process(self,data,inputs,utils):
        print ("in Postflight")
        if inputs['cleanup']:
            utils.remove_download(inputs["channel_id"])