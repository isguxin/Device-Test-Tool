from info.device_sn import DeviceSN


class UI(DeviceSN):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = UI()
    app.root.mainloop()
