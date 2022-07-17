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

    # @classmethod
    # def get_devices_list(cls):
    #     """
    #     获取设备连接的device列表
    #
    #     :return: 连接的device列表
    #     """
    #     command = "adb devices"
    #     adb_devices_list = Common.shell(command, is_output_list=True)
    #     devices_sn_list = []
    #     tmp_list = []
    #     for line in adb_devices_list:
    #         t = line.split()
    #         if len(t) == 0:
    #             continue
    #         else:
    #             tmp_list.append(t[0])
    #     for device_sn in tmp_list:
    #         if device_sn == "List" or len(device_sn) == 0:
    #             continue
    #         else:
    #             devices_sn_list.append(device_sn)
    #     return devices_sn_list
    #
    # @classmethod
    # def root_device(cls, device_sn=None):
    #     """
    #     获取 Android 管理员的权限
    #
    #     :param device_sn: 设备SN
    #     :return: 获取管理员权限回显
    #     """
    #     command = ADBTool.cmd("root", device_sn)
    #     root_device = Common.shell(command)
    #     return root_device
    #
    # @classmethod
    # def remount_device(cls, device_sn=None):
    #     """
    #     获取 System 分区可写权限
    #
    #     :param device_sn: 设备SN
    #     :return: 获取 System 分区可写权限回显
    #     """
    #     command = ADBTool.cmd("remount", device_sn)
    #     remount_device = Common.shell(command)
    #     return remount_device
    #
    # @classmethod
    # def get_all_packages_list(cls, device_sn=None):
    #     """
    #     显示所有包名
    #
    #     :param device_sn: 设备SN
    #     :return: 系统所有报名列表
    #     """
    #     command = ADBTool.cmd("shell pm list packages", device_sn)
    #     all_packages_list = Common.shell(command, is_output_list=True)
    #     packages_list = []
    #     for line in all_packages_list:
    #         tmp_pkg_name = line[8:] if line.startswith("package:") else line
    #         pkg_name = tmp_pkg_name[:-3] if tmp_pkg_name.endswith("\r\r\n") else tmp_pkg_name
    #         packages_list.append(pkg_name)
    #     return packages_list
    #
    # @classmethod
    # def install_apk(cls, apk_path, device_sn=None):
    #     command = ADBTool.cmd("install -r -d {}".format(apk_path), device_sn)
    #     install_apk = Common.shell(command, is_output_list=True)
    #     return install_apk
    #
    # @classmethod
    # def uninstall_package(cls, package_name, device_sn=None):
    #     command = ADBTool.cmd("uninstall {}".format(package_name), device_sn)
    #     uninstall_package = Common.shell(command, is_output_list=True)
    #     return uninstall_package


if __name__ == '__main__':
    print(ADBTool.get_devices_list())

