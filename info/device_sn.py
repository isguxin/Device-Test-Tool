from common.adb_tool import ADBTool
from gui.main_gui import MainUI


class DeviceSN(MainUI):
    def __init__(self):
        super().__init__()

        self.get_device_sn_button["command"] = self.get_devices_sn_list

    def ensure(self, event):
        """
        日志展示选中的设备 SN 号

        :param event: 动作
        :return: None
        """
        sn = self.get_device_sn_combobox.get()
        self.log("已选择SN：{}".format(sn))

    def get_devices_sn_list(self):
        """
        获取设备的 SN 号

        :return: None
        """
        # devices_sn_list = ADBTool.get_devices_sn_list()
        devices_sn_list = ["123132", "123123123123123"]
        if len(devices_sn_list) == 0:
            self.get_device_sn_combobox["values"] = ["No devices found"]
            self.log("未连接设备")
        else:
            self.get_device_sn_combobox["values"] = devices_sn_list
            self.get_device_sn_combobox.current(0)
            self.log("设备SN列表：{}".format(devices_sn_list))
            self.log("已选择SN：{}".format(self.get_device_sn_combobox.get()))
            self.get_device_sn_combobox.bind('<<ComboboxSelected>>', self.ensure)
