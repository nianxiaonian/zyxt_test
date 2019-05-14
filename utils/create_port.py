# win   netstat -ano | find 4723
# mac   lsof -i:4723
from utils.sys_cmd import SysCmd


class CreatePort(object):

    def port_is_used(self, port_num):
        '''判断端口是否被占用'''
        dos = SysCmd()
        command = 'lsof -i:' + str(port_num)
        result = dos.excute_cmd_result(command)
        if len(result) > 0:
            # 端口被占用,kill pid
            pid = result[1].split()[1]
            dos.excute_cmd('kill %s' % pid)
        return False

    def create_port(self, start_port, device_list):
        '''生成可用端口, 有多少个设备生成多少个端口'''
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) == False:
                    port_list.append(start_port)
                    start_port += 1
            return port_list
        else:
            print('当前无可用设备，生成端口失败')
            return None

if __name__ == '__main__':
    create_port = CreatePort()
    print(create_port.port_is_used(4700))
    # print(create_port.create_port(4700, [1, 2, 3]))


