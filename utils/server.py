'''
获取设备信息
创建可用端口
生成命令  #appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
启动服务
使用多线程启动服务
'''
from utils.sys_cmd import SysCmd
from utils.create_port import CreatePort
from utils.get_device import GetDevice
import time
import multiprocessing


class Server(object):
    def __init__(self):
        self.dos_cmd = SysCmd()
        self.create_port = CreatePort()
        self.device_list = self.get_device()
        self.opera_device = GetDevice()

    def get_device(self):
        '''
        获取设备信息
        :return:
        '''
        device_list = []
        result_list = self.dos_cmd.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    device_list.append(devices_info[0])
            return device_list
        else:
            print('当前无可用设备')
            return None

    def create_port_list(self, start_port):
        '''创建可用端口'''

        port_list = self.create_port.create_port(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        # -bp 是连接Android设备bootstrap的端口号，默认是4724
        # appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log /Users/nianzhidan/PycharmProjects/zyxr/log/test01.log
        '''
        启动appium服务
        :param i: 循环的设备个数
        :return:
        '''
        command_list = []
        port_list = self.create_port_list(4700)
        bp_list = self.create_port_list(4900)
        device_list = self.device_list
        command = 'appium -p ' + str(port_list[i]) + ' -bp ' + str(bp_list[i]) + ' -U ' + str(device_list[i]) + \
                  ' --no-reset --session-override --log /Users/nianzhidan/PycharmProjects/zyxr_new/log/test'+str(i)+'.log'
        command_list.append(command)
        # 把设备相关信息，写入到config文件中
        self.opera_device.write_data(i, device_list[i], bp_list[i], port_list[i])
        return command_list

    def start_server(self, i):
        '''启动appium服务'''
        start_list = self.create_command_list(i)
        print('start_list:', start_list)
        self.dos_cmd.excute_cmd(start_list[0])

    def kill_server(self, i):
        '''杀掉appium服务
        lsof -i:4723
        kill pid
        '''
        port = self.opera_device.get_value('device_info_%s' % i, 'port')
        ret = self.dos_cmd.excute_cmd_result('lsof -i:%s' % port)
        pid = ret[1].split()[1]
        self.dos_cmd.excute_cmd('kill %s' % pid)

    def main(self):
        self.opera_device.clear_data()
        process_list = []
        # 使用多进程来启动多个appium服务
        for i in range(len(self.device_list)):
            print('i: ', i)
            # appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            process_list.append(appium_start)
        for j in process_list:
            j.start()
        time.sleep(20)


if __name__ == '__main__':
    server = Server()
    server.main()
    server.kill_server(0)

