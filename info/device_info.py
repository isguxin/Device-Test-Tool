import ttkbootstrap as t

from gui.main_gui import MainUI


class DeviceInfo(MainUI):
    def __init__(self):
        super().__init__()

        self.device_info_checkbutton_content = [
            [t.StringVar(), "123"]
        ]

        self.device_info_checkbutton_0_0["text"] = "设备的版本"
        self.device_info_checkbutton_0_0["variable"] = self.device_info_checkbutton_content[0][0]

