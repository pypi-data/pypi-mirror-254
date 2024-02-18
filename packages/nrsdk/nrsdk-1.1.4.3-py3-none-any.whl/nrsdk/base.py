import os
import glob
from datetime import datetime, timezone

TRIGGER_MAPPING = {
    1000: 'start of stimulation',
    1001: 'end of stimulation',
    1201: 'event 1',
    1202: 'event 2',
    1203: 'event 3',
    1204: 'event 4',
    1205: 'event 5',
    1206: 'event 6',
    1207: 'event 7',
    1208: 'event 8',
    1209: 'event 9',
    1210: 'event 10'
}

DEVICE_MAPPING = {
    101: 'A32',
    102: 'A64R',
    103: 'C64',
    104: 'H32S',
    105: 'A32'
}

def bytes_to_number(bs, isBig=False, signed=True):
    if (len(bs) == 3) and not isBig:
        isNeg = bs[0] & 0x80 == 1 and signed
        return (0xFFFFFFFF if isNeg else 0x0) | bs[0]<< 16 | bs[1] << 8  | bs[2]
    return int.from_bytes(bs, byteorder='big' if isBig else 'little', signed=signed)

def bytes_to_datetime(bs, isBig=True):
    year = bytes_to_number(bs[1:3], isBig=True)
    month = bytes_to_number(bs[3:4])
    day = bytes_to_number(bs[4:5])
    hour = bytes_to_number(bs[5:6])
    minute = bytes_to_number(bs[6:7])
    sec = bytes_to_number(bs[7:8])
    ms = bytes_to_number(bs[8:], isBig=True)
    return datetime(year, month, day, hour, minute, sec, ms,
                                 tzinfo=timezone.utc)

        
def get_file_list(fpath, ext='edf'):    
    file_filter = "*.{}".format(ext)
    return glob.glob(os.path.join(fpath, file_filter))