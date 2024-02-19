import struct
from datetime import datetime
from enum import Enum

WEBCAM = 0x00
CANOE_COM = 0x01
SSH = 0x02
AVN = 0x03
DLT = 0x04
CCA = 0x05
HDMI = 0x06
CANXL = 0x07
CLOCK = 0x08
TAD_TT = 0x09
ERROR = 0xF0

WEBCAM_PORT = 1001
CANOE_COM_PORT = 1002
SSH_PORT = 1003
AVN_PORT = 1004
DLT_PORT = 1005
CCA_PORT = 1006
HDMI1_PORT = 1007
HDMI2_PORT = 1008
HDMI3_PORT = 1009
CANXL_PORT = 1010
CLOCK_PORT = 1011
TAD_TT_PORT = 1012

CMD_GetWebcamImage = 0x0000 # Cam
CMD_SaveWebcamVideo = 0x0001
CMD_CamConnect = 0x0002
CMD_CamDisconnect = 0x0003
CMD_SetCamRecordingTime = 0x0004
CMD_CamCompare = 0x0005 #PRK
CMD_CamBuffer = 0x0006 #PRK
CMD_CamHeartbeat = 0x01FF

CMD_SetTestbench_Bplus = 0x0000 # CANoe COM
CMD_SetTestbench_Acc = 0x0001
CMD_SetTestbench_IGN = 0x0002
CMD_GetCANSignal = 0x0003
CMD_SetCANSignal = 0x0004
CMD_StartCANoeCfg = 0x0005
CMD_CANoeConnect = 0x0006
CMD_CANoeDisconnect = 0x0007
CMD_CANoeHeartbeat = 0x01FF
CMD_SendSSHCmd = 0x0000 # SSH
CMD_SSHConnect = 0x0001
CMD_SSHDisconnect = 0x0002
CMD_SSHConvertFile01 = 0x0003
CMD_SSHHeartbeat = 0x01FF

CMD_ReqImgSave = 0x0000 # AVN
CMD_ReqImgBuffer = 0x0001
CMD_ReqTouch = 0x0002
CMD_ReqDrag = 0x0003
CMD_ReqHardkey = 0x0004
CMD_ReqSystemResource = 0x0005
CMD_AVNConnect = 0x0006
CMD_AVNDisconnect = 0x0007
CMD_ReqMainVersion = 0x0008
CMD_ReqSubVersion = 0x0009
CMD_ReqRefreshImage = 0x000A
CMD_AVNHeartbeat = 0x01FF

CMD_WaitDLTLog = 0x0000 # DLT
CMD_SaveDLTLog = 0x0001
CMD_DLTConnect = 0x0002
CMD_DLTDisconnect = 0x0003
CMD_SetDLTRecordingTime = 0x0004
CMD_DLTHeartbeat = 0x01FF
CMD_CompareImage = 0x0002 # CCA
CMD_CompareAVNScreen = 0x0003
CMD_SetCCAManualControl = 0x0004
CMD_BenchConnect = 0x0005
CMD_BenchDisconnect = 0x0006
CMD_SetBenchBPlus = 0x0007
CMD_SetBenchAcc = 0x0008
CMD_SetBenchIgn = 0x0009
CMD_GetBenchVolt = 0x000A
CMD_GetBenchCurr = 0x000B
CMD_GetBenchWatt = 0x000C
CMD_ReqReportWriteStart = 0x000D
CMD_ReqReportWriteStop = 0x000E
CMD_ReqReportWrite = 0x000F

CMD_TT_BtnEvent = 0x0000
CMD_TT_SetVoltage = 0x0001
CMD_TT_GetVoltage = 0x0002
CMD_TT_GetAmpere = 0x0003
CMD_TT_GetWatt = 0x0004
CMD_TT_MeasurementStart = 0x0005
CMD_TT_MeasurementStop = 0x0006
CMD_TT_MeasurementGet = 0x0007
CMD_TT_MeasurementUnit = 0x0008
CMD_TT_PowerSupply = 0x0009
CMD_TT_PWM = 0x000A

def printAK(text):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('[%s] %s' % (now, text))


class TCP_Packet:
    target_devices = [WEBCAM, CANOE_COM, SSH, AVN, DLT, CCA, HDMI, CANXL, CLOCK, TAD_TT]

    @classmethod
    def check_packet(cls, packet):
        try:
            start_packet = packet[0]
            target_device = packet[1]
            length = (packet[2] << 8) + packet[3]
            end_packet = packet[5+length]
            if start_packet != 0x11:
                return False
            if target_device not in cls.target_devices:
                return False
            if not(length == 2 or 4 <= length <= 0x209):
                return False
            if end_packet != 0xff:
                return False
            return True
        except Exception as e:
            print('Check Packet error occurred: %s' %str(e))

    @classmethod
    def get_device(cls, device):
        _device = str(device).upper()
        if _device in ['WEBCAM', str(WEBCAM)] and WEBCAM in cls.target_devices:
            return WEBCAM
        elif _device in ['CANOE_COM', str(CANOE_COM)] and CANOE_COM in cls.target_devices:
            return CANOE_COM
        elif _device in ['SSH', str(SSH)] and SSH in cls.target_devices:
            return SSH
        elif _device in ['AVN', str(AVN)] and AVN in cls.target_devices:
            return AVN
        elif _device in ['DLT', str(DLT)] and DLT in cls.target_devices:
            return DLT
        elif _device in ['CCA', str(CCA)] and CCA in cls.target_devices:
            return CCA
        elif _device in ['HDMI', str(HDMI)] and HDMI in cls.target_devices:
            return HDMI
        elif _device in ['TAD_TT', str(TAD_TT)] and TAD_TT in cls.target_devices:
            return TAD_TT
        else:
            return ERROR

    @classmethod
    def get_base_packet(cls, target_device=None, command_code=None):
        base_packet = [0x11, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff]
        if target_device is not None:
            device_code = cls.get_device(target_device)
            if device_code == ERROR:
                print('Wrong target_deivce')
            else:
                base_packet[1] = device_code
        if command_code is not None:
            command_code1 = command_code >> 8
            command_code2 = command_code & 0xff
            base_packet[4] = command_code1
            base_packet[5] = command_code2
        return base_packet

    @staticmethod
    def set_device(packet, target_device):
        _packet = packet
        device_code = cls.get_device(target_device)
        if device_code == ERROR:
            print('Wrong target_deivce')
        else:
            _packet[1] = device_code
        return _packet

    @staticmethod
    def set_command(packet, command_code):
        _packet = packet
        command_code1 = command_code >> 8
        command_code2 = command_code & 0xff
        _packet[4] = command_code1
        _packet[5] = command_code2
        return _packet

    @staticmethod
    def add_sub_command(packet, value, value_type, size=0):
        if type(size) is not int or size > 0xff:
            print('Wrong sub command size')
            return packet
        _packet = packet[:-2]
        if value_type == int:
            _packet += [size]
            #sub_command = []
            if size == 1:
                #sub_command.append(value)
                _packet += [value]
            elif size == 2:
                #sub_command.append(value.to_bytes(2, byteorder='little'))
                _packet += value.to_bytes(2, byteorder='little', signed=True)
            elif size == 4:
                #sub_command.append(value.to_bytes(4, byteorder='little'))
                _packet += value.to_bytes(4, byteorder='little', signed=True)
            else:
                raise 'Wrong size exception:%d' %size
            # while size > 0:
            #     sub_command.insert(0, value&0xff)
            #     value >>= 8
            #     size -= 1
            #_packet += sub_command
        elif value_type == str:
            data = value.encode('utf-8')
            #_packet += [len(data)]
            #_packet += data
            _data = data[:255]
            _packet += [len(_data)]
            _packet += _data
        elif value_type == float:
            _packet += [0x04]
            _packet += bytearray(struct.pack('f', value))
        else:
            print('Wrong sub command type')
        _packet += packet[-2:]
        return _packet

    @staticmethod
    def check_length(packet):
        _packet = packet
        length = len(packet[4:-2])
        if length > 0xffff:
            print('Wrong length:%d' %length)
            return _packet
        _packet[2] = length >> 8
        _packet[3] = length & 0xff
        return _packet

    @staticmethod
    def GetSubCommand(packet):
        sub_command = []
        #length = (packet[2] << 8) + packet[3]
        #sub_command_array = packet[6:6+length]
        sub_command_array = packet[6:-2]
        sub_command_index = 0
        while(sub_command_index < len(sub_command_array)):
            size = sub_command_array[sub_command_index]
            sub_command.append(sub_command_array[sub_command_index+1:sub_command_index+1+size])
            sub_command_index += (size+1)
        return sub_command

### AVN ###

class Hardkey(Enum):
    mkbd_home = MKBD_HOME = 0x600A
    mkbd_map = MKBD_MAP = 0x600B
    mkbd_nav = MKBD_NAV = 0x600C
    mkbd_radio = MKBD_RADIO = 0x600D
    mkbd_media = MKBD_MEDIA = 0x600E
    mkbd_custom = MKBD_CUSTOM = 0x6011
    mkbd_setup = MKBD_SETUP = 0x6012
    mkbd_search = MKBD_SEARCH = 0x6013
    mkbd_seek_up = MKBD_SEEK_UP = 0x6014
    mkbd_track_up = MKBD_TRACK_UP = 0x6015
    mkbd_seek_down = MKBD_SEEK_DOWN = 0x6016
    mkbd_track_down = MKBD_TRACK_DOWN = 0x6017
    mkbd_power = MKBD_POWER = 0x601D
    mkbd_tune_push = MKBD_TUNE_PUSH = 0x601E
    mkbd_volume_knob = MKBD_VOLUME_KNOB = 0x6001
    mkbd_tune_knob = MKBD_TUNE_KNOB = 0x6004

    swrc_ptt = SWRC_PTT = 0x7022
    swrc_mode = SWRC_MODE = 0x7023
    swrc_mute = SWRC_MUTE = 0x7024
    swrc_seek_up = SWRC_SEEK_UP = 0x700F
    swrc_seek_down = SWRC_SEEK_DOWN = 0x7010
    swrc_custom = SWRC_CUSTOM = 0x7011
    swrc_send = SWRC_SEND = 0x7025
    swrc_end = SWRC_END = 0x7026
    swrc_volume_knob = SWRC_VOLUMNE_KNOB = 0x7001
    swrc_trip_menu = SWRC_TRIP_MENU = 0x7031
    swrc_trip_up = SWRC_TRIP_UP = 0x7032
    swrc_trip_down = SWRC_TRIP_DOWN = 0x7033
    swrc_trip_ok = SWRC_TRIP_OK = 0x7034
    swrc_trip_lfa = SWRC_TRIP_LFA = 0x7035
    swrc_trip_cancel = SWRC_TRIP_CANCEL = 0x7036
    swrc_trip_set = SWRC_TRIP_SET = 0x7037
    swrc_trip_res = SWRC_TRIP_RES = 0x7038
    swrc_trip_cruise = SWRC_TRIP_CRUISE = 0x7039
    swrc_trip_cruise_sld = SWRC_TRIP_CRUISE_SLD = 0x703A
    swrc_trip_scc = SWRC_TRIP_SCC = 0x703B
    swrc_trip_padd_dn = SWRC_TRIP_PADD_DN = 0x703C
    swrc_trip_padd_up = SWRC_TRIP_PADD_UP = 0x703D
    swrc_trip_error = SWRC_TRIP_ERROR = 0x703E
    swrc_trip_reserved = SWRC_TRIP_RESERVED = 0x703F
    swrc_optical_swipe_up = SWRC_OPTICAL_SWIPE_UP = 0x7051
    swrc_optical_swipe_down = SWRC_OPTICAL_SWIPE_DOWN = 0x7052
    swrc_optical_swipe_left = SWRC_OPTICAL_SWIPE_LEFT = 0x7053
    swrc_optical_swipe_right = SWRC_OPTICAL_SWIPE_RIGHT = 0x7054
    swrc_optical_touch = SWRC_OPTICAL_TOUCH = 0x7055
    swrc_optical_ok = SWRC_OPTICAL_OK = 0x7056

class Dir(Enum): # Direction
    clockwise = CLOCKWISE = 0x00
    anti_clockwise = ANTI_CLOCKWISE = 0x01
    none = NONE = None

class Monitor(Enum):
    front = FRONT = 0x00
    rear_left = REAR_LEFT = 0x01
    rear_right = REAR_RIGHT = 0x02
    cluster = CLUSTER = 0x03
    hud = HUD = 0x04
