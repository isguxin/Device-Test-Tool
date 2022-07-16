from subprocess import Popen, PIPE


class Common:

    @classmethod
    def shell(cls, command, is_output=True):
        """
        执行shell命令

        :param command: shell命令
        :param is_output: 是否有回显
        :return: 有回显则返回回显，没有回显则返回为空
        """
        if is_output:
            command_result = Popen(command, stdin=PIPE, stdout=PIPE, shell=True).stdout.read().decode("utf_8")
            return command_result
        else:
            Popen(command, stdin=PIPE, stdout=PIPE, shell=True)
            return None


if __name__ == '__main__':
    adb_version = Common.shell("adb version")
    print(adb_version)

