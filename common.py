from subprocess import Popen, PIPE


class Common:

    @classmethod
    def shell(cls, command, is_output=True, is_output_list=False):
        """
        执行shell命令

        :param command: shell命令
        :param is_output: 是否有回显
        :param is_output_list: 回显格式是否为列表格式
        :return: 有回显则返回回显，没有回显则返回为空
        """
        if is_output:
            if not is_output_list:
                command_result = Popen(command, stdin=PIPE, stdout=PIPE, shell=True).stdout.read().decode("utf-8")
                return command_result
            else:
                command_result = Popen(command, stdin=PIPE, stdout=PIPE, shell=True).stdout.readlines()
                command_list = [line.decode("utf-8") for line in command_result]
                return command_list
        else:
            Popen(command, stdin=PIPE, stdout=PIPE, shell=True)
            return None


if __name__ == '__main__':
    pass
