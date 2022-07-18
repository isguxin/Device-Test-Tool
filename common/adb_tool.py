from common.common_util import Common


class ADBTool:

    @classmethod
    def get_devices_sn_list(cls):
        command = Common.adb_cmd("devices")
        command_out = Common.shell(command).stdout.readlines()
        tmp_list = []
        for line in command_out:
            tmp_list.append(line.split())
        devices_sn_list = []
        for i in range(1, len(tmp_list)):
            if len(tmp_list[i]) == 0:
                continue
            elif tmp_list[i][1] != "device":
                continue
            else:
                devices_sn_list.append(tmp_list[i][0])
        return devices_sn_list


if __name__ == '__main__':
    pass
