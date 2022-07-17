from subprocess import Popen, PIPE, TimeoutExpired


class Common:

    @classmethod
    def shell(cls, command):
        """
        执行 SHELL 命令

        :param command: SHELL 命令
        :return: 命令执行回显
        """
        p = Popen(command, stdin=PIPE, stdout=PIPE, shell=True, encoding="utf-8")
        p_out, p_err = p.communicate()
        return p_out

    @classmethod
    def adb_cmd(cls, command, device_sn=None):
        """
        拼接 ADB SHELL 命令

        :param command: ADB 后的命令内容
        :param device_sn: 设备 SN 号
        :return: 拼接后的 ADB SHELL 命令内容
        """
        adb_command = "adb{} {}".format(" -s {}".format(device_sn) if device_sn is not None else "", command)
        return adb_command

if __name__ == '__main__':
    command = Common.adb_cmd("devices")
    command_out = Common.shell(command)
    print(command_out)
