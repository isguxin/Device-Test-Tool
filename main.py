from info.device_info import DeviceInfo
from info.device_sn import DeviceSN
from info.log_info import LogInfo


class UI(DeviceInfo, DeviceSN, LogInfo):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = UI()
    app.root.mainloop()
