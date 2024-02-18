from __future__ import annotations # for Python 3.7-3.9
import enum
import json
from typing import TypedDict
from functools import wraps

def to_list(in_ch):
    ret = []
    for ch in in_ch:
        assert ch % 1 == 0, 'ch must be int'
        ret.append(int(ch))
    return ret

def to_int(in_int):
    assert in_int % 1 == 0, 'ch must be int'
    return int(in_int)

class WaveForm(enum.IntEnum):
    DC = 0,
    AC = 1,
    BidPulse = 3 

class NrParamChannel(TypedDict):
    waveform: Union[WaveForm,int]
    frequency:int = 0
    current: Union[int,float]
    ramp_up:Union[int,float] = 0
    ramp_down:Union[int,float] = 0
    duration:Union[int,float]
    phase_position:Union[int,float] = 0
    channel_id:int = 0

    @classmethod
    def dc(cls, current:float, 
            *, channel_id = 0, duration = 0xFFFFFFFF, ramp_up = 0, ramp_down = 0)->NrParamChannel:
        return {
                "waveform":WaveForm.DC,
                "current": current,
                "duration":duration,
                "ramp_up":ramp_up,
                "ramp_down":ramp_down,
                "channel_id":channel_id,
                }

    
    @classmethod
    def ac(cls, current:float, frequency:int,
            *, duration=0xFFFFFFFF, ramp_up = 0, ramp_down = 0, phase_position = 0
            ) ->NrParamChannel:
        return {
            "waveform":WaveForm.AC,
            "current": current,
            "duration":duration,
            "ramp_up":ramp_up,
            "ramp_down":ramp_down,
            "channel_id":0,
            "phase_position":phase_position,
            }


class NrParamParams(TypedDict):
    channels: list[NrParamChannel]
    @classmethod
    def default(cls)->dict:
        return {"channels": []}

class NrParamBase(TypedDict):
    params:List[NrParamParams]
    @classmethod
    def default(cls)->dict:
        return {"params": [NrParamParams.default()]}

class NrParam:
    @classmethod
    @wraps(NrParamChannel.ac)
    def ac(cls, *arg, **kwargs)->NrParamChannel:
        return NrParamChannel.ac(*arg, **kwargs)

    @classmethod
    @wraps(NrParamChannel.dc)
    def dc(cls, *arg, **kwargs)->NrParamChannel:
        return NrParamChannel.dc(*arg, **kwargs)

    def get_param(self) -> NrParamBase:
        return self.param

    # ch_id_start 决定channel_apply时通道id从0或1 开始
    def __init__(self, ch_id_start = 0):
        self.ch_id_start = ch_id_start
        self.param:NrParamBase = NrParamBase.default()
    
    def channel_apply(self, channel_id:Union[list, int], wave:NrParamChannel, *, 
                    channel_id_nega:Union[list, int] = [], duration = None, ramp_up = None, ramp_down = None)->None:

        channel_list:list[NrParamChannel] = self.param["params"][0]["channels"]
        def app_int(ch_id:int, scale:float):
            ch_id = to_int(ch_id) 
            assert ch_id >= self.ch_id_start
            ch_wave = wave.copy()
            ch_wave['channel_id'] = ch_id - self.ch_id_start # TODO
            if duration is not None:
                ch_wave['duration'] = duration
            if ramp_up is not None:
                ch_wave['ramp_up'] = ramp_up
            if ramp_down is not None:
                ch_wave['ramp_down'] = ramp_down
            ch_wave['current'] *= scale

            channel_list.append(ch_wave)

        try:
            int(channel_id)
        except:
            pass
        else:
            channel_id = [channel_id]
        
        try:
            int(channel_id_nega)
        except:
            pass
        else:
            channel_id_nega = [channel_id_nega]
        
        scals = {}
        if len(channel_id) == 0:
            for i in channel_id_nega:
                scals[i] = -1
        elif len(channel_id_nega) != 0:
            posi_s = 1/len(channel_id)
            posi_n = -1/len(channel_id_nega)
            for i in channel_id_nega:
                scals[i] = posi_n
            for i in channel_id:
                scals[i] = posi_s
        channel_id = list(set(channel_id)|set(channel_id_nega))
        for i in channel_id:
            app_int(i, scals.get(i, 1))

if __name__ == '__main__':      
    p = NrParam() # 
    dc = p.dc(1)
    ac = p.ac(1, 10)
    p.channel_apply([4,3,5], ac, channel_id_nega=[2], duration=100)
    pr = json.dumps(p.get_param(), indent=2)
    print(pr)
