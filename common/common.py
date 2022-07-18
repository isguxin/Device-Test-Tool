from subprocess import Popen, PIPE, STDOUT


def shell(command):
    """
    执行 SHELL 命令

    :param command: SHELL 命令
    :return: POPEN 对象
    """
    p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True, encoding="utf-8")
    return p


def adb_cmd(command, device_sn=None):
    """
    拼接 ADB SHELL 命令

    :param command: SHELL 命令
    :param device_sn: 设备 SN 号
    :return: ADB SHELL 命令
    """
    cmd = "adb{} {}".format(" -s {}".format(device_sn) if device_sn is not None else "", command)
    return cmd


if __name__ == '__main__':
    pass
