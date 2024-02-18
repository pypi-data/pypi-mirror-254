from ctypes import *
from operator import contains
import os
import json

def nr_sdk():    
    cur_path = os.path.dirname(__file__)
    dll_path = cur_path + "/lib/QLNRSdk.dll"
    api = cdll.LoadLibrary(dll_path)
    
    # init
    api.QLNR_Init()
    return api

_api = nr_sdk()

class NRSDK(object):
    def __init__(self) :
        self.ip = r'127.0.0.1'
        self.login_handle = c_void_p(None)
        self.connected = False

    def connect(self, ip=None):
        if ip:
            self.ip = ip
        #login
        server_ip = c_char_p(self.ip.encode('utf-8'))
        res = _api.QLNR_Login(server_ip, pointer(self.login_handle))
        self.connected = (res == 0)

        #log
        print("connect to app server[{}] {}.".format(self.ip, "success" if self.connected else "fail"))

        return self
        
    def close(self):
        print("logout from app server[{}]".format(self.ip))
        _api.QLNR_Logout(self.login_handle)
        self.connected = False
    
    # 未连接时，自动连接一次
    def _assert_connected(self):
        if self.connected:
            return
        
        self.connect()

    # 开始刺激
    def _start_stimulation(self, param, device=None):
        self._assert_connected()

        # 字符串格式统一为dict
        if isinstance(param, str):
            param = json.loads(param)

        s = json.dumps(param, indent=4)
        # print(s)

        param_2 = c_char_p(s.encode('utf-8'))
        p_resp = (c_char * 512)(0)
        len = 512
        device_code = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        res = -1
        try:
            res = _api.QLNR_StartStimulationEx(self.login_handle, param_2, p_resp, len, device_code)
            # print("start stimulation {}".format(resp_result(res)))
            # if res != _RESP_SUCCESS:
            #     print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
    
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL
        
    #停止刺激
    def _stop_stimulation(self, device=None):
        self._assert_connected()

        p_resp = (c_char * 512)(0)
        len = 512
        device_code = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        try:
            res = _api.QLNR_StopStimulationEx(self.login_handle, p_resp, len, device_code)
            # print("stop stimulation {}".format(resp_result(res)))
            # if res != _RESP_SUCCESS:
            #     print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL
        
    #获取上位机已连接的设备列表
    def _get_device_list(self):
        self._assert_connected()

        p_resp = (c_char * 512)(0)
        len1 = 512
        p_list = (c_char * 4096)(0)
        len2 = 4096
        res = -1
        try:
            res = _api.QLNR_GetDeviceListEx(self.login_handle, p_resp, len1, p_list, len2)
            # print("get device list {}".format(resp_result(res)))
            if res == _RESP_SUCCESS:
                list = p_list.value.decode("utf-8")
                return json.loads(list)
            else:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return []

    #设置wifi参数
    def _set_wifi_config(self, ssid, skey, device=None):
        self._assert_connected()
        print(f"ssid:{ssid}, secret:{skey}: device:{device}")

        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_ssid = c_char_p(ssid.encode('utf-8')) if ssid else c_char_p(None)
        p_skey = c_char_p(skey.encode('utf-8')) if skey else c_char_p(None)
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        try:
            res = _api.QLNR_SetDeviceWifiConfigEx(self.login_handle, p_ssid, p_skey, p_resp, len, p_device)
            # print("set wifi config {} for device[{}]".format(resp_result(res), device))
            if res != _RESP_SUCCESS:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL

    #查询wifi参数
    def _get_wifi_config(self, device=None):
        self._assert_connected()

        p_wifi_config = (c_char * 512)(0)
        wifi_config_len = 512
        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)

        result = {}
        try:
            res = _api.QLNR_GetDeviceWifiConfigEx(self.login_handle, p_wifi_config, wifi_config_len, p_resp, len, p_device)
            print("get wifi config {} for device[{}]".format(resp_result(res), device))
            if res == _RESP_SUCCESS:
                wifi_config = p_wifi_config.value.decode("utf-8")
                # print(wifi_config)
                wifi_config = json.loads(wifi_config)
                result["ssid"] = wifi_config["configssid"]
                result["skey"] = wifi_config["configpassword"]
                result["ssid_default"] = wifi_config["defaultssid"]
                result["skey_default"] = wifi_config["defaultpassword"]
                result["ssid_connected"] = wifi_config["currentssid"]
                result["skey_connected"] = wifi_config["currentpassword"]

            else:
                print(p_resp.value.decode("utf-8"))
            
        except Exception as e:
            print(e)
        
        return result

    #重启设备
    def _restart_device(self, device=None):
        self._assert_connected()

        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)

        try:
            res = _api.QLNR_SetDeviceResetEx(self.login_handle, p_resp, len, p_device)
            # print("restart device {} for device[{}], resp: {}".format(resp_result(res), device, p_resp.value.decode("utf-8")))
            
        except Exception as e:
            print(e)
        
        return res

    #事件标记
    def _trigger(self, event_id, device=None):
        self._assert_connected()
        
        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)

        try:
            res = _api.QLNR_SetTrigger(self.login_handle, event_id, p_resp, len, p_device)
            # print("trigger {} for device[{}], resp: {}".format(resp_result(res), device, p_resp.value.decode("utf-8")))
            
        except Exception as e:
            print(e)
        
        return res

    #开启信号采集（并记录到文件）
    def _start_collection(self, param=None, path=None, file_type=None, device=None):
        self._assert_connected()

        p_param = c_char_p(None)
        if param:
            # 字符串格式统一为dict
            if isinstance(param, str):
                param = json.loads(param)

            s = json.dumps(param, indent=4)
            print(s)

            p_param = c_char_p(s.encode('utf-8'))
        p_path = c_char_p(path.encode('utf-8')) if path else c_char_p(None)
        
        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)

        try:
            res = _api.QLNR_StartCollectEx(self.login_handle, p_param, p_path, file_type, p_resp, len, p_device)
            # print("start collection {} for device[{}], resp: {}".format(resp_result(res), device, p_resp.value.decode("utf-8")))
            
        except Exception as e:
            print(e)
        
        return res

    #停止信号采集
    def _stop_collection(self, device=None):
        self._assert_connected()
        
        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)

        try:
            res = _api.QLNR_StopCollectEx(self.login_handle, p_resp, len, p_device)
            # print("start collection {} for device[{}], resp: {}".format(resp_result(res), device, p_resp.value.decode("utf-8")))
            
        except Exception as e:
            print(e)
        
        return res
        

    #获取上位机已连接的设备列表
    def _get_subject_list(self):
        self._assert_connected()

        p_resp = (c_char * 512)(0)
        len1 = 512
        p_list = (c_char * 4096)(0)
        len2 = 4096
        res = -1
        try:
            res = _api.QLNR_GetPatientListEx(self.login_handle, p_resp, len1, p_list, len2)
            # print("get subject list {}".format(resp_result(res)))
            if res == _RESP_SUCCESS:
                list = p_list.value.decode("utf-8")
                return json.loads(list)
            else:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return []

    #获取范式列表-和设备相关
    def _get_paradigm_list(self, device=None):
        self._assert_connected()

        p_resp = (c_char * 512)(0)
        len1 = 512
        p_list = (c_char * 40960)(0)
        len2 = 40960
        res = -1
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        try:
            res = _api.QLNR_GetParadigmListEx(self.login_handle, p_resp, len1, p_list, len2, p_device)
            # print("get paradigm list {}".format(resp_result(res)))
            if res == _RESP_SUCCESS:
                list = p_list.value.decode("utf-8")
                return json.loads(list)
            else:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return []

    #设置被试
    def _set_subject_select(self, subject_id, device=None):
        self._assert_connected()
        # print(f"_set_subject_select(subject_id:{subject_id}, : device:{device})")

        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_subject_id = c_char_p(subject_id.encode('utf-8')) if subject_id else c_char_p(None)
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        try:
            res = _api.QLNR_SetPatientEx(self.login_handle, p_subject_id, p_resp, len, p_device)
            # print("_set_subject_select {} for device[{}]".format(resp_result(res), device))
            if res != _RESP_SUCCESS:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL

    #设置范式
    def _set_paradigm_select(self, paradigm_id, device=None):
        self._assert_connected()
        # print(f"_set_paradigm_select(paradigm_id:{paradigm_id}, : device:{device})")

        p_resp = (c_char * 512)(0)
        len = 512
        res = -1
        p_paradigm_id = c_char_p(paradigm_id.encode('utf-8')) if paradigm_id else c_char_p(None)
        p_device = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        try:
            res = _api.QLNR_SetParadigmEx(self.login_handle, p_paradigm_id, p_resp, len, p_device)
            # print("_set_paradigm_select {} for device[{}]".format(resp_result(res), device))
            if res != _RESP_SUCCESS:
                print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
        
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL

    # 开始刺激
    def _start_stim_by(self, param, device=None):
        self._assert_connected()

        # 字符串格式统一为dict
        if isinstance(param, str):
            param = json.loads(param)

        s = json.dumps(param, indent=4)
        # print(s)

        param_2 = c_char_p(s.encode('utf-8'))
        p_resp = (c_char * 512)(0)
        len = 512
        device_code = c_char_p(device.encode('utf-8')) if device else c_char_p(None)
        res = -1
        try:
            res = _api.QLNR_StartStimulationByCustomEx(self.login_handle, param_2, p_resp, len, device_code)
            # print("start _stim_with_custom_param {}".format(resp_result(res)))
            # if res != _RESP_SUCCESS:
            #     print(p_resp.value.decode("utf-8"))
        except Exception as e:
            print(e)
    
        return _SUCCESS if res == _RESP_SUCCESS else _FAIL
    
_RESP_SUCCESS = 0
_SUCCESS = 1
_FAIL = 0

def resp_result(res):
    return 'success' if res == 0 else 'fail'

def show_result(res):
    return 'success' if res == 1 else 'fail'