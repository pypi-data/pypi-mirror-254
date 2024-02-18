
import json

WAVEFORM_MAPPING = {
    "dc":0,
    "ac":1,
    "pulse": 2,
    "pulse101": 101, #脉冲含正向-水平-负向三部分各40us，正向/负向上升、下降时长各15uS 脉冲发送频率130Hz 
    "pulse102": 102, #脉冲含正向-水平-负向三部分各40us，正向/负向上升、下降时长各15uS 脉冲发送频率130Hz 
    "pulse105": 105 #脉冲含正向-水平-负向三部分各40us，正向/负向上升、下降时长各15uS 脉冲发送频率130Hz 
}

class Paradigm(object):
    def __init__(self, channels, up, duration, down, marker_id = None, type='dc'):
        self._channels=channels
        self._up = float(up) / 1000
        self._duration = float(duration)  / 1000
        self._down = float(down) / 1000
        self._waveform = WAVEFORM_MAPPING.get(type.lower())
        self._marker_id = marker_id
        self._paradigm = self._gen_paradigm()

    def _gen_paradigm(self):
        pd = {}
        if self._channels is None or len(self._channels) == 0:
            return None
        pd["params"] = [{}]
        # 这个marker id指定在sequence同级，实际marker_id在sequence上级，需要改sdk接口解析逻辑
        if self._marker_id:
            pd["marker_id"] = self._marker_id
        pd["params"][0]["channels"] = []
        
        for idx, channel in enumerate(self._channels.keys()):
            ch_param = {}
            ch_param["channel_id"] = int(channel)
            ch_param["waveform"] = self._waveform
            ch_param["current"] = self._channels[channel]
            ch_param["ramp_up"] = self._up
            ch_param["ramp_down"] = self._down
            ch_param["duration"] = self._duration
            # 去掉只有63个通道的限制
            # if (ch_param["channel_id"] >= 63):
            #     ch_param["channel_id"] = 62
            pd["params"][0]["channels"].append(ch_param)

        return json.dumps(pd)


    def get(self):
        return self._paradigm

    @property
    def marker_id(self):
        return self._marker_id
    
    def duration(self):
        return self._duration + self._up + self._down