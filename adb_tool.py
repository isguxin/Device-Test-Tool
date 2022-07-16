from common import Common


class ADBTool:

    @classmethod
    def cmd(cls, command, device_sn=None):
        adb_command = "adb{} {}".format(" -s {}".format(device_sn) if device_sn is not None else "", command)
        return adb_command

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
    def kill_adb_server(cls):
        """
        关闭 adb 服务

        :return: None
        """
        command = "adb kill-server"
        Common.shell(command, is_output=False)

    @classmethod
    def start_adb_server(cls):
        """
        启动 adb 服务

        :return: None
        """
        command = "adb start-server"
        Common.shell(command, is_output=False)

    @classmethod
    def connect_device(cls, device_sn):
        """
        连接设备

        :param device_sn: 设备SN号
        :return: 连接设备回显
        """
        command = "adb connect {}".format(device_sn)
        connect_device = Common.shell(command)
        return connect_device

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

    @classmethod
    def root_device(cls, device_sn=None):
        """
        获取 Android 管理员的权限

        :param device_sn: 设备SN
        :return: 获取管理员权限回显
        """
        command = ADBTool.cmd("root", device_sn)
        root_device = Common.shell(command)
        return root_device


if __name__ == '__main__':
    print(ADBTool.root_device(device_sn="127.0.0.1:7555"))
