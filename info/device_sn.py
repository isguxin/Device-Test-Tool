from common.adb_tool import ADBTool
from gui.main_gui import MainUI


class DeviceSN(MainUI):
    def __init__(self):
        super().__init__()

        self.get_device_sn_button["command"] = lambda: self.thread_it(self.get_devices_sn_list)

    def get_devices_sn_list(self):
        """
        获取设备的 SN 号

        :return: None
        """
        devices_sn_list = ADBTool.get_devices_sn_list()
        if len(devices_sn_list) == 0:
            self.get_device_sn_combobox["values"] = ["No devices found"]
            self.get_device_sn_combobox.current(0)
            self.log("未连接设备")
        else:
            self.get_device_sn_combobox["values"] = devices_sn_list
            self.get_device_sn_combobox.current(0)
            self.log("有{}台设备连接：".format(len(devices_sn_list)))
            self.log("SN列表：{}".format(devices_sn_list))
            self.log("默认选择SN：{}".format(self.get_device_sn_combobox.get()))
            self.get_device_sn_combobox.bind('<<ComboboxSelected>>', self.ensure)
        self.log("------------------------------------------")

    def ensure(self, event):
        """
        日志展示选中的设备 SN 号

        :param event: 动作
        :return: None
        """
        sn = self.get_device_sn_combobox.get()
        if sn == "No devices found":
            return
        else:
            self.log("已选择SN：{}".format(sn))
        self.log("------------------------------------------")
