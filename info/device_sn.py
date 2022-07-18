from gui.main_gui import MainUI


class DeviceSN(MainUI):
    def __init__(self):
        super().__init__()

        self.get_device_sn_button["command"] = self.get_devices_sn_list

    def get_devices_sn_list(self):
        devices_sn_list = ["127:0.0.1:7555", "123123123"]
        self.get_device_sn_combobox["values"] = devices_sn_list
        self.get_device_sn_combobox.current(0)
        self.get_device_sn_combobox.bind("<<ComboboxSelected>>", self.ensure)

    def ensure(self, event):
        self.log(self.get_device_sn_combobox.get())


