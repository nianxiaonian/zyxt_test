import yaml

class GetDevice(object):
    '''
    操作device相关config文件
    '''
    def read_data(self):
        '''
        读取设备配置文件中数据
        :return:
        '''
        with open('/Users/nianzhidan/PycharmProjects/zyxr_new/config/device_info.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_value(self, key, port):
        '''
        获取value
        :return:
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        '''
        写入数据
        :return:
        '''
        data = {
            'device_info_'+str(i):{
                'deviceName': device,
                'bp': bp,
                'port': port,
            }
        }
        with open('/Users/nianzhidan/PycharmProjects/zyxr_new/config/device_info.yaml', 'a') as f:
            yaml.dump(data, f)

    def clear_data(self):
        '''
        清空数据
        :return:
        '''
        with open('/Users/nianzhidan/PycharmProjects/zyxr_new/config/device_info.yaml', 'w') as f:
            f.truncate()

    def get_lines(self):
        '''
        获取行数
        :return:
        '''
        data = self.read_data()
        return len(data)

if __name__ == '__main__':
    opera_device = GetDevice()
    opera_device.clear_data()
    opera_device.write_data(0, 112222333333, 4900, 4700)
    opera_device.get_lines()
    print(opera_device.get_value('device_info_0', 'port'))
    print(opera_device.get_lines())


