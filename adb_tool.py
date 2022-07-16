from common import Common


class ADBTool:

    @classmethod
    def show_adb_version(cls):
        """
        展示设备ADB版本

        :return: ADB版本
        """
        command = "adb version"
        adb_version = Common.shell(command)
        return adb_version

    @classmethod
    def get_devices_list(cls):
        """
        获取设备连接的device列表

        :return: 连接的device列表
        """
        command = "adb devices"
        adb_devices_list = Common.shell(command, is_output_list=True)
        devices_sn_list = []
        tmp_list = []
        for line in adb_devices_list:
            t = line.split()
            if len(t) == 0:
                continue
            else:
                tmp_list.append(t[0])
        for device_sn in tmp_list:
            if device_sn == "List" or len(device_sn) == 0:
                continue
            else:
                devices_sn_list.append(device_sn)
        return devices_sn_list


if __name__ == '__main__':
    print(ADBTool.get_devices_list())
    pass
