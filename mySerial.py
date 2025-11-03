# -*- coding: utf-8 -*-
import threading
import time

import serial
import serial.tools.list_ports


class SerThread(threading.Thread):
    def __init__(self, port=None, comb=None, textBrowser=None, lineEdit=None):
        super().__init__()
        # 绑定窗体的下拉列表
        self.comb = comb
        self.textBrowser = textBrowser
        self.lineEdit = lineEdit
        
        # 初始化串口句柄
        self.serialPort = SerialPort(port, baudrate=115200, timeout=1)
        self.serialPort.serial.stopbits = serial.STOPBITS_TWO
        
        # 绑定串口接收、发送、更新进程回调函数
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.send_thread = threading.Thread(target=self.send_data)
        self.updata_serial_port_thread = threading.Thread(target=self.update_serial_port)
        
        # 串口接收、发送、更新进程开启标志
        self.receive_data_flag = False
        self.send_data_flag = False
        self.update_flag = False
        
        # 接收数据缓存
        self.data_buffer = ""


    def receive_data_old(self):
        while self.receive_data_flag:
            data = self.serialPort.read_data()            
            if data:
                print("Received data:", data)
            else:
                # print("No data received.")
                pass
            time.sleep(0.1)

    def receive_data(self):
        buffer = bytearray()
        
        # while self.receive_data_flag:
        while True:
            data = self.serialPort.read_data_all()
            if data:
                buffer.extend(data)
                # print(f"检测到数据: {data.hex(' ').upper()}")
                # print(f"当前 buffer 内容: {buffer.hex(' ').upper()}")
                while len(buffer) >= 4:
                    # 检查帧头
                    if buffer[0] == 0x5A and buffer[1] == 0xA5:
                        frame_len = buffer[2]  # 第3字节是长度
                        # print(f"检查帧头[{frame_len}]")
                        total_len = frame_len + 3  # 帧头2 + 长度1 + 内容
                        if len(buffer) >= total_len:
                            frame = buffer[:total_len]
                            buffer = buffer[total_len:]
                            
                            hex_str = frame.hex(' ').upper()
                            print(f"[FRAME] {hex_str}")
                            
                            if self.textBrowser:
                                self.textBrowser.append(hex_str)
                        else:
                            break
                    else:
                        # 如果开头不是帧头，就丢弃一个字节（防止乱序）
                        buffer.pop(0)
            # time.sleep(0.01)

    def send_data(self):
        while self.send_data_flag:
            if self.data_buffer:
                self.serialPort.write_data(self.data_buffer)
                self.data_buffer = ""
            time.sleep(0.1)

    def update_serial_port(self):
        while self.update_flag:
            if self.serialPort.enumerate_ports():
                print("get New Serial port")
                self.comb.clear()
                self.comb.addItems(self.serialPort.serial_descript_list)
            time.sleep(0.1)

    def run(self):
        self.receive_data_flag = True
        self.send_data_flag = True
        self.update_flag = True
        self.receive_thread.start()
        self.send_thread.start()
        self.updata_serial_port_thread.start()

    def stop(self):
        self.receive_data_flag = False
        self.send_data_flag = False
        self.update_flag = True
        
        # 等待线程安全退出
        # if self.receive_thread.is_alive():
        #     self.receive_thread.join(timeout=1)
        # if self.send_thread.is_alive():
        #     self.send_thread.join(timeout=1)
        # if self.updata_serial_port_thread.is_alive():
        #     self.updata_serial_port_thread.join(timeout=1)
        
        # 关闭串口
        if self.serialPort.serial.is_open:
            self.serialPort.serial.close()



class SerialPort:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        
        self.serial_list = []
        self.serial_descript_list = []
        
        # 存放串口描述和接口的字典
        self.serial_dict = {}

    # 枚举串口并更新到列表
    def enumerate_ports(self):
        # 串口表有更新标志
        getnewport = False
        # 获取串口表
        new_serial_list = serial.tools.list_ports.comports()
        if new_serial_list != self.serial_list:
            getnewport = True
            print("Serial ports updated")
        # 如果串口有变动，更新串口列表和串口词典
        if getnewport:
            self.serial_list = new_serial_list
            self.updata_serial_dict()
        return getnewport

    def updata_serial_dict(self):
        newDict = self.make_serial_dict()  # 获取最新的串口字典
        
        # 比较新旧字典变动
        added_ports = [portDescript for portDescript in newDict if portDescript not in self.serial_dict]
        removed_ports = [portDescript for portDescript in self.serial_dict if portDescript not in newDict]
        
        # 更新旧字典内容
        for port in added_ports:
            self.serial_dict[port] = newDict[port]
            print("Added Serial Port: ", port, newDict[port])
        for port in removed_ports:
            self.serial_dict.pop(port)
            print("Removed Serial Port: ", port)

    # 创建字典 description ： device
    def make_serial_dict(self):
        serial_dict = {}
        self.serial_descript_list = []
        for port in self.serial_list:
            self.serial_descript_list.append(port.description)
            serial_dict[port.description] = port.device
        return serial_dict

    def set_ports(self, port):
        self.port = port

    def set_baudrate(self, baudrate):
        self.baudrate = baudrate

    def set_stopbits(self, stopbits):
        self.stopbits = stopbits

    def open_port(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.serial.is_open:
                print(f"Serial port {self.port} opened successfully.")
        except serial.SerialException as e:
            print(f"Failed to open serial port {self.port}. Error: {e}")

    def close_port(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"Serial port {self.port} closed.")
        else:
            print("No open serial port.")

    def write_data(self, data):
        if self.serial and self.serial.is_open:
            try:
                self.serial.write(data)
                print(f"Sent data: {data}")
            except serial.SerialException as e:
                print(f"Failed to send data. Error: {e}")
        else:
            pass
            # print("No open serial port.")

    def read_data(self, num_bytes=1):
        if self.serial and self.serial.is_open:
            try:
                received_data = ""
                received_data = self.serial.readline()
                if received_data:
                    print(f"Received data: {received_data.decode('gb2312')}")
                    return received_data.decode('gb2312')
                else:
                    # print("No open serial port.")
                    return None
            except BaseException as e:
                print(f"Failed to receive data. Error: {e}")
        else:
            return None
        

    def read_data_all(self):
        """读取串口缓冲区的所有数据（二进制读取，不依赖换行符）"""
        if not self.serial or not self.serial.is_open:
            return None
        try:
            data = self.serial.read_all()
            if data:
                # print(f"[HEX] Received raw: {data.hex(' ').upper()}")
                return data
        except OSError as e:
            print(f"Serial closed during read: {e}")
            return None
        except Exception as e:
            print(f"Failed to read all data. Error: {e}")
            return None
        
    
