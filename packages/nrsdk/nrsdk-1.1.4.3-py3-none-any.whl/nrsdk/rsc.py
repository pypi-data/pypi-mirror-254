from nrsdk import NeuroRecorder
from nrsdk.mcf_reader import McfReader
import os
import glob
from time import sleep
        
def get_file_list(fpath, ext='mcf'):    
    file_filter = "*.{}".format(ext)
    return glob.glob(os.path.join(fpath, file_filter))

class Rsc(NeuroRecorder):
    def __init__(self):   
        NeuroRecorder.__init__(self)

    def stim(self, fpath, delay_before = 5, deley_after = 5):
        mcf = McfReader(fpath, marker_type=True)
        print(f"start stim from file[{fpath}] with marker id {mcf.marker_id}")
        if delay_before > 0:
            self.trigger(mcf.marker_id)
            print(f"add marker {mcf.marker_id}[before]")
            sleep(delay_before)
        print(f"start stim from file[{fpath}] with param {mcf.paradigm.get()}")
        self.stim_start(mcf.paradigm.get())
        sleep(mcf.paradigm.duration())
        if deley_after > 0:
            sleep(deley_after)
            self.trigger(mcf.marker_id)
            print(f"add marker {mcf.marker_id}[after]")

    
    def stim_all(self, ffolder, delay_before = 5, deley_after = 5):
        # 读取fpath目录下的mcf文件列表
        fpath_list = get_file_list(ffolder)
        fpath_list.sort()
        fpath_list.sort(key=lambda x: int(x.replace(ffolder + "\\", "")[:-4]))
        for idx, fpath in enumerate(fpath_list):
            self.stim(fpath, delay_before, deley_after)

