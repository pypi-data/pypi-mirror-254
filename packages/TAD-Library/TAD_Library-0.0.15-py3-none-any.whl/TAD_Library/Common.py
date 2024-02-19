import logging
import socket

global client_socket
logger = logging.getLogger(__name__)

def TM_Connect(ip, port):
    """
        Tool과의 연결 함수 입니다.

        :param ip(string) : IP address (ex. "123.456.789.111")

        :param port(int) : port number (ex. 1234)

        :returns : None
    """
    global client_socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

def TM_Disconnect():
    global client_socket
    try:
        client_socket.close()
        return 1
    except:
        return 0

def TM_IsConnect() -> bool:
    """
        Tool 연결 확인 함수 입니다.

        :returns : Pass (True) / Fail (False)
    """
    global client_socket
    try:
        # this will try to read bytes without blocking and also without removing them from buffer (peek only)
        data = client_socket.recv(10, socket.MSG_DONTWAIT | socket.MSG_PEEK)
        if len(data) == 0:
            return True
    except BlockingIOError:
        return False  # socket is open and reading from it would block
    except ConnectionResetError:
        return True  # socket was closed for some other reason
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return False
    return False


def TM_SendCmd(cmd):
    """
        Tool 명령어 전달 함수 입니다.

        :param cmd(bytearray) : Byte Array (ex. [0x01, 0x01, 0x01])

        :returns : Pass (Tool return result) / Fail (0)
    """
    global client_socket
    try:
        client_socket.send(cmd)
        data = client_socket.recv(10)
        return float(data.decode())
    except:
        print("Recv Timeout!")
        return 0

def TM_SetSwitch(btnNum, onoff):
    """
        Tool 버튼 제어 함수 입니다.

        :param btnNum(int) : Button Index(0~11)

        :param state(int) : On(0x01) / Off(0x00)

        :returns : Pass (1) / Fail (0)
    """
    global client_socket
    data = bytearray([0x11, 0x01, btnNum, onoff])

    TM_SendCmd(data)

def TM_PowerSupply(onoff):
   """
       전압 제어 함수 입니다.

       :param On(0x01) / Off(0x00)

       :returns : Pass (Tool return result) / Fail (0)
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x01, onoff])

   return TM_SendCmd(data)

def TM_SetVoltage(voltage):
   """
       전압 제어 함수 입니다.

       :param btnNum(int) : Voltage Value (0~30)

       :returns : Pass (1) / Fail (0)
   """
   global client_socket

   ValueA = int(voltage // 1)
   ValueB = int(round(voltage % 1, 2) * 100)

   data = bytearray([0x11, 0x02, 0x02, int(ValueA), int(ValueB)])

   return TM_SendCmd(data)

def TM_SetAmpere(ampere):
   """
       전류 최대치 지정 함수 입니다.

       :param btnNum(int) : Voltage Value (0~30)

       :returns : Pass (1) / Fail (0)
   """
   global client_socket

   ValueA = int(ampere // 1)
   ValueB = int(round(ampere % 1, 2) * 100)

   data = bytearray([0x11, 0x02, 0x02, int(ValueA), int(ValueB)])

   return TM_SendCmd(data)

def TM_GetVoltage():
   """
       전압 확인 함수 입니다.

       :returns : Voltage Value
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x04])

   return TM_SendCmd(data)

def TM_GetAmpere():
   """
       전류 확인 함수 입니다.

       :returns : Ampere Value
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x05])

   return TM_SendCmd(data)

def TM_GetWatt():
   """
       전력 확인 함수 입니다.

       :returns : Watt Value
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x06])

   return TM_SendCmd(data)

def TM_CurrMeasurementStart():
   """
       미세 전류 측정 시작 함수 입니다.

       :returns : Pass (1) / Fail (0)
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x07])

   return TM_SendCmd(data)

def TM_CurrMeasurementStop():
   """
       미세 전류 측정 중지 함수 입니다.

       :returns : Pass (1) / Fail (0)
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x08])

   return TM_SendCmd(data)

def TM_CurrMeasurementGet():
   """
       미세 전류 측정 값 읽기 함수 입니다.

       :returns : Measurment Value
   """
   global client_socket

   data = bytearray([0x11, 0x02, 0x09])

   return TM_SendCmd(data)

def TM_CurrSetUnit(unit_value):
    """
       미세 전류 단위 설정 함수 입니다.

       :returns : Pass (1) / Fail (0)
    """
    global client_socket

    data = bytearray([0x11, 0x02, 0x0A, unit_value])

    return TM_SendCmd(data)

