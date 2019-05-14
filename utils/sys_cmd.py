import os


class SysCmd(object):
    # 执行并获取结果
    def excute_cmd_result(self, command):
        '''需要获取执行结果，如获取device设备, 检查端口占用'''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    # 仅执行
    def excute_cmd(self, command):
        os.system(command)

if __name__ == '__main__':
    dos = SysCmd()
    # print(dos.excute_cmd_result('adb devices'))
    # print(dos.excute_cmd_result('lsof -i:8080'))
    # print(dos.excute_cmd('lsof -i:8080'))
    print(dos.excute_cmd_result('lsof -i tcp:4723'))

    server_list = dos.excute_cmd_result('lsof -i tcp:4723')
    if server_list:
        print(server_list[1].split(' ')[2])

        print('ok')