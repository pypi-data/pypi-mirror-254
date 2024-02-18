from bs4 import BeautifulSoup
from .paradigm import Paradigm
import os

class McfReader():
    def __init__(self, fname, marker_type=False):
        self._fname = fname
        self._blocks = None
        self._marker_type = marker_type
        self._marker_id = None
        self._paradigm = None
        #read
        self._parser()

    @property
    def paradigm(self):
        return self._paradigm

    @property
    def marker_id(self):
        return self._marker_id

    def _parser(self):
        soup = BeautifulSoup(open(self._fname), 'xml')
        self._blocks = soup.blocks
        # read file name as marker id
        if self._marker_type:
            self._read_marker()
        self._read_paradigm()

    def _read_marker(self):
        try:
            (fpath, fname) = os.path.split(self._fname)
            self._marker_id = int(fname[:-4])
        except:
            print (f"{self._fname} _read_marker error.")

    def _read_channels(self, blocks):
        rst = dict()
        try:
            electrodes = blocks.find_all("electrode")
            for idx, electrode in enumerate(electrodes):
                ch = electrode["channelID"]
                current = electrode["amplitude"] 
                # current uA to mA
                rst[ch]= float(current) / 1000.0
        except:
            print("_read_channels error.")

        return rst
            
    def _read_paradigm(self):
        try:
            up = self._blocks.find_all(id="0")[0]
            dc = self._blocks.find_all(id="1")[0]
            down = self._blocks.find_all(id="2")[0]
            up_duration = up.duration_ms.text
            duration = dc.duration_ms.text
            down_duration = down.duration_ms.text
            channels = self._read_channels(dc.spatialPattern)

            self._paradigm = Paradigm(channels, up_duration, duration, down_duration, marker_id=self._marker_id)
        except:
            print (f"{self._fname} _read_paradigm error.")

