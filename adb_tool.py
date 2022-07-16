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


if __name__ == '__main__':
    print(ADBTool.show_adb_version())
