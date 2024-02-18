# qlapi-nrsdk



## Getting started

> export eeg to edf file
```python
from qlapi_nrsdk import Rsa, McfReader

de=Rsa()
def stim_with_mcf(fname, device=None):
    #读取mcf文件
    mcf = McfReader(fname, marker_type="name")
    paradigm = mcf.paradigm

    print(f"File {fname} start. marker id is {paradigm.marker_id}. stim total：{paradigm.duration()} s, sleep {start_delay} s")
    #对指定设备施加刺激指令
    de.stim_start(paradigm.get(), device)
    sleep(paradigm.duration() + start_delay)

mcf_fname = "E:/Temp/test/ISM_HC011.mcf"

#读取设备列表
list = de.device_list()
if len(list) < 1:
    print("no device available!")
else:  
    for idx, device in enumerate(list):
        stim_with_mcf(fname=mcf_fname, device=device["conncode"])
```


## version 
> v0.1.1

+ 开始刺激
+ 结束刺激
+ 查询设备列表