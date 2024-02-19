import os.path
import sys
from socket import *
from time import sleep
from TCP_Packet_Lib import *
from threading import Thread
import io
import glob;

class TT:
    __ip_address = '127.0.0.1'
    port = 111
    __max_packet_size = 2048
    __client_socket = None
    __server_socket = None
    __tcp_thread_exit_flag = False

    @classmethod
    def Start_Server(cls, device, callback):
        try:
            cls.__server_socket = socket(AF_INET, SOCK_STREAM)
            cls.__server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            # if device == WEBCAM:
            #     self.server_socket.bind(self.ip_address, WEBCAM_PORT)
            # elif device == CANOE_COM:
            #     self.server_socket.bind(self.ip_address, CANOE_COM_PORT)
            # elif device == SSH:
            #     self.server_socket.bind(self.ip_address, SSH_PORT)
            # elif device == AVN:
            #     self.server_socket.bind(self.ip_address, AVN_PORT)
            # elif device == DLT:
            #     self.server_socket.bind(self.ip_address, DLT_PORT)
            # elif device == CCA:
            #     self.server_socket.bind(self.ip_address, CCA_PORT)
            if device == SSH:
                cls.__server_socket.bind((cls.__ip_address, SSH_PORT))
            else:
                printAK('Start_Server device type error: %s' % str(device))
                return False
            server_connection_thread = Thread(target=cls.__Server_ConnectionThread, args=(callback,))
            server_connection_thread.daemon = True
            server_connection_thread.start()
            return True
        except Exception as e:
            printAK('Start_Server error occurred: %s' % str(e))
            return False

    @classmethod
    def __Server_ConnectionThread(cls, callback):
        try:
            cls.__tcp_thread_exit_flag = False
            while not cls.__tcp_thread_exit_flag:
                cls.__server_socket.listen()
                client_socket, addr = cls.__server_socket.accept()
                server_thread = Thread(target=cls.__Server_Thread, args=(client_socket, callback,))
                server_thread.daemon = True
                server_thread.start()
        except Exception as e:
            printAK('Server_ConnectionThread error occurred: %s' % str(e))

    @classmethod
    def __Server_Thread(cls, client_socket, callback):
        try:
            cls.__tcp_thread_exit_flag = False
            while not cls.__tcp_thread_exit_flag:
                packet = client_socket.recv(cls.__max_packet_size)
                if (len(packet) == 0):
                    break
                print('Recv: ' + ''.join('%02x ' % i for i in packet))
                ret_packet = callback(packet)
                print('ret:  ' + ''.join('%02x ' % i for i in ret_packet))
                client_socket.send(bytes(ret_packet))
        except Exception as e:
            printAK('Server_Thread error occurred: %s' % str(e))

    @classmethod
    def __send(cls, packet):
        recv_packet = bytes()
        try:
            packet = TCP_Packet.check_length(packet)
            # print('Send  : ' + ''.join('%02x ' % i for i in packet))
            # print(TCP_Packet.check_packet(packet))
            # print(self.client_socket.send(bytes(packet)))
            cls.__client_socket.send(bytes(packet))
            recv_packet = cls.__client_socket.recv(cls.__max_packet_size)
            if recv_packet[0] == 0x11:
                # print('Recv  : ' + ''.join('%02x ' % i for i in recv_packet))
                pass
            elif recv_packet[0] == 0x12:  # 230622 Protocol 기준
                print('RecvEx: ' + ''.join('%02x ' % i for i in recv_packet))
                ex_packet = cls.__client_socket.recv(cls.__max_packet_size)
                # print('RecvEx:%d' %len(ex_packet))
                # print('RecvEx: ' + ''.join('%02x ' % i for i in ex_packet))
                recv_packet += ex_packet[7:-2]
                send_count = 1
                while ex_packet[2] == 0x01:
                    ex_packet = cls.__client_socket.recv(cls.__max_packet_size)
                    # print('RecvEx:%d' % len(ex_packet))
                    # print('RecvEx: ' + ''.join('%02x ' % i for i in ex_packet))
                    recv_packet += ex_packet[7:-2]
                    send_count += 1
                print('RecvEx Send %d times' % send_count)
        except Exception as e:
            printAK('send error occurred: %s' % str(e))
        sleep(0.1)
        return recv_packet

    @staticmethod
    def __get_status(status):
        _status = str(status).lower()
        if _status in ['on', '1', 'true']:
            return 0x01
        elif _status in ['off', '0', 'false']:
            return 0x00
        else:
            printAK('get_status value error: %s' % _status)
            return ERROR

    @staticmethod
    def __get_direction(direction):
        _direction = str(direction).lower()
        if _status in ['anti_clockwise', 'anti clockwise', 'left']:
            return 0x01
        elif _status in ['clockwise', 'right']:
            return 0x00
        else:
            printAK('value error: %s' % _status)
            return ERROR

    @staticmethod
    def __get_monitor(monitor):
        _monitor = str(monitor).lower()
        if _monitor in ['front', 'avn', '0']:
            return 0x00
        elif _monitor in ['rear_left', 'rear left', 'left', '1']:
            return 0x01
        elif _monitor in ['rear_right', 'rear right', 'right', '2']:
            return 0x02
        elif _monitor in ['cluster', '3']:
            return 0x03
        elif _monitor in ['hud', '4']:
            return 0x04
        else:
            printAK('get_monitor value error: %s' % _monitor)
            return ERROR

    @classmethod
    def ButtonEvent(cls, btn_num, btn_value):
        try:
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_BtnEvent)
            packet = TCP_Packet.add_sub_command(packet, btn_num, int, 1)
            packet = TCP_Packet.add_sub_command(packet, btn_value, int, 1)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_ButtonEvent error occurred: %s' % str(e))
            return 0

    @classmethod
    def Connect(cls, ip, port):
        try:
            cls.__client_socket = socket(AF_INET, SOCK_STREAM)
            cls.__client_socket.connect((ip, port))
            return 1
        except Exception as e:
            printAK('ConnectCCA error occurred: %s' % str(e))
            return 0

    @classmethod
    def Disconnect(cls):
        try:
            printAK('DisconnectCCA')
            cls.__client_socket.close()
            return 1
        except Exception as e:
            printAK('DisconnectCCA error occurred: %s' % str(e))
            return 0

    @classmethod
    def PowerSupply(cls, on_off):
        try:
            printAK('TT Power supply control Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_PowerSupply)
            packet = TCP_Packet.add_sub_command(packet, on_off, int, 1)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_PowerSupply error occurred: %s' % str(e))
            return 0

    @classmethod
    def SetVoltage(cls, voltage):
        try:
            printAK('TT Set voltage Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_SetVoltage)
            voltage_round = round(voltage, 2)
            packet = TCP_Packet.add_sub_command(packet, voltage_round, float)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_SetVoltage error occurred: %s' % str(e))
            return 0

    @classmethod
    def GetVoltage(cls):
        try:
            printAK('TT Get voltage Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_GetVoltage)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if sub_command[0][0] == 0x01:
                return sub_command[1].decode('utf-8')
            else:
                printAK('%d -> FAIL' % sub_command[0][0])
                return ''
        except Exception as e:
            printAK('TT_GetVoltage error occurred: %s' % str(e))
            return 0

    @classmethod
    def GetAmpere(cls):
        try:
            printAK('TT Get ampere Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_GetAmpere)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if sub_command[0][0] == 0x01:
                return sub_command[1].decode('utf-8')
            else:
                printAK('%d -> FAIL' % sub_command[0][0])
                return ''
        except Exception as e:
            printAK('TT_GetAmpere error occurred: %s' % str(e))
            return 0

    @classmethod
    def GetWatt(cls):
        try:
            printAK('TT Get watt Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_GetWatt)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if sub_command[0][0] == 0x01:
                return sub_command[1].decode('utf-8')
            else:
                printAK('%d -> FAIL' % sub_command[0][0])
                return ''
        except Exception as e:
            printAK('TT_GetWatt error occurred: %s' % str(e))
            return 0

    @classmethod
    def StartMeasurement(cls):
        try:
            printAK('TT Measurement Start Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_MeasurementStart)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_MeasurementStart error occurred: %s' % str(e))
            return 0

    @classmethod
    def StopMeasurement(cls):
        try:
            printAK('TT Measurement Stop Event')
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_MeasurementStop)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_MeasurementStop error occurred: %s' % str(e))
            return 0

    @classmethod
    def SetMeasurementUnit(cls, UnitValue):
        try:
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_MeasurementUnit)
            packet = TCP_Packet.add_sub_command(packet, UnitValue, int, 1)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)
            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')
            return sub_command[0][0]
        except Exception as e:
            printAK('TT_MeasurementUnit error occurred: %s' % str(e))
            return 0

    @classmethod
    def GetMeasurementData(cls, UnitValue:int):
        try:
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_MeasurementGet)
            packet = TCP_Packet.add_sub_command(packet, UnitValue, int, 1)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)

            if sub_command[0][0] == 0x01:
                unit = 'A'
                if (UnitValue == 1):
                    unit = 'A'
                elif (UnitValue == 2):
                    unit = '㎃'
                elif (UnitValue == 3):
                    unit = '㎂'

                return sub_command[1].decode('utf-8')+unit
            else:
                printAK('%d -> FAIL' % sub_command[0][0])
                return '', ''
        except Exception as e:
            printAK('TT_MeasurementGet error occurred: %s' % str(e))
            return 0

    @classmethod
    def StartPWM(cls, ch, onTime, offTime, repeatCnt, lastmode):
        try:
            packet = TCP_Packet.get_base_packet('TAD_TT', CMD_TT_PWM)
            packet = TCP_Packet.add_sub_command(packet, ch, int, 1)
            packet = TCP_Packet.add_sub_command(packet, onTime, int, 1)
            packet = TCP_Packet.add_sub_command(packet, offTime, int, 1)
            packet = TCP_Packet.add_sub_command(packet, repeatCnt, int, 1)
            packet = TCP_Packet.add_sub_command(packet, lastmode, int, 1)
            recv = cls.__send(packet)
            sub_command = TCP_Packet.GetSubCommand(recv)

            if (sub_command[0][0] == 0x1):
                printAK(sys._getframe(0).f_code.co_name + '-> PASS')
            else:
                printAK(sys._getframe(0).f_code.co_name + '-> FAIL')

            return sub_command[0][0]

        except Exception as e:
            printAK('TT_MeasurementGet error occurred: %s' % str(e))
            return 0