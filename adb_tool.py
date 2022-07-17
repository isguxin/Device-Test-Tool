from common import Common


class ADBTool:

    @classmethod
    def show_adb_version(cls):
        """
        展示设备 ADB 版本

        :return: ADB 版本
        """
        command = Common.adb_cmd("version")
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def show_adb_help(cls):
        """
        展示 ADB 帮助信息
        查看 ADB 所支持的所有命令

        :return: ADB 帮助信息
        """
        command = Common.adb_cmd("help")
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def start_adb_server(cls):
        """
        启动 ADB 服务

        :return: None
        """
        command = Common.adb_cmd("start-server")
        Common.shell(command)
        return None

    @classmethod
    def kill_adb_server(cls):
        """
        关闭 ADB 服务

        :return: None
        """
        command = Common.adb_cmd("kill-server")
        Common.shell(command)
        return None

    @classmethod
    def connect_device(cls, device_sn):
        """
        连接指定设备

        :param device_sn: 设备 SN 号
        :return: 连接设备状态
        """
        command = Common.adb_cmd("connect {}".format(device_sn))
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def get_devices_list(cls):
        """
        查看当前连接的设备

        :return: 当前连接的设备 SN 号列表
        """
        command = Common.adb_cmd("devices")
        command_out = Common.shell(command)
        devices_sn_tmp_list = []
        devices_sn_list = []
        tmp_list = command_out.split("\n")[1:]
        for item in tmp_list:
            if len(item) == 0:
                continue
            else:
                devices_sn_tmp_list.append(item.rstrip("\tdevice")
                                           if item.endswith("\tdevice")
                                           else "")
        for sn in devices_sn_tmp_list:
            if sn == "":
                continue
            else:
                devices_sn_list.append(sn)
        return devices_sn_list

    @classmethod
    def root_device(cls, device_sn=None):
        """
        获取 Android 管理员的权限

        :param device_sn: 设备 SN 号
        :return: 获取权限回显
        """
        command = Common.adb_cmd("root", device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def remount_device(cls, device_sn=None):
        """
        获取 System 分区可写权限

        :param device_sn: 设备 SN 号
        :return: 获取权限回显
        """
        command = Common.adb_cmd("remount", device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def get_all_packages(cls, device_sn=None):
        """
        获取设备的所有包名

        :param device_sn: 设备 SN 号
        :return: 设备的所有包名
        """
        command = Common.adb_cmd("shell pm list packages", device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def get_sys_packages(cls, device_sn=None):
        """
        获取设备的系统应用包名

        :param device_sn: 设备 SN 号
        :return: 设备的系统应用包名
        """
        command = Common.adb_cmd("shell pm list packages -s", device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def get_3rd_packages(cls, device_sn=None):
        """
        获取设备的三方应用包名

        :param device_sn: 设备 SN 号
        :return: 设备的三方应用包名
        """
        command = Common.adb_cmd("shell pm list packages -3", device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def install_apk(cls, apk_path, device_sn=None):
        """
        将本地 apk 软件安装到设备上

        :param apk_path: 本地 apk 软件路径
        :param device_sn: 设备 SN 号
        :return: 安装 apk 回显
        """
        command = Common.adb_cmd("install -r -d {}".format(apk_path), device_sn)
        command_out = Common.shell(command)
        return command_out

    @classmethod
    def uninstall_package(cls, package_name, device_sn=None):
        """
        将设备上的 apk 卸载

        :param package_name: apk 包名
        :param device_sn: 设备 SN 号
        :return: 卸载 apk 回显
        """
        command = Common.adb_cmd("uninstall {}".format(package_name), device_sn)
        command_out = Common.shell(command)
        return command_out


if __name__ == '__main__':
    # print(ADBTool.connect_device("127.0.0.1:7555"))
    # print(ADBTool.get_all_packages())
    # print(ADBTool.get_3rd_packages("127.0.0.1:7555"))
    # print(ADBTool.install_apk(r"C:\workspace\apk\com.kugou.android.apk"))
    print(ADBTool.uninstall_package("com.kugou.android"))

