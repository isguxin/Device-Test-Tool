from subprocess import Popen, PIPE, STDOUT


def shell(command):
    p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True, encoding="utf-8")
    return p


def adb_cmd(command, device_sn=None):
    cmd = "adb{} {}".format(" -s {}".format(device_sn) if device_sn is not None else "", command)
    return cmd


if __name__ == '__main__':
    pass
