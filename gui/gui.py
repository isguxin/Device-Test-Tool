import ttkbootstrap as t
from ttkbootstrap import DANGER, WARNING, DARK, YES, RIGHT, INFO, END, Y, X, DISABLED, N, S, LIGHT, LEFT
from ttkbootstrap.scrolled import ScrolledText


class MainUI:
    def __init__(self):
        self.root = t.Window(
            title="Device Test Tool V2022.08",
            size=(1350, 900),
            resizable=(False, False),
            alpha=1.0
        )
        """顶部框架"""
        self.display_top = t.Frame(self.root)
        self.display_top.place(x=10, width=1330, y=10, height=60)
        self.show_display_top()
        """左下框架"""
        self.display_lower_left = t.Frame(self.root, style=WARNING)
        self.display_lower_left.place(x=10, width=890, y=70, height=820)
        """右下框架"""
        self.display_lower_right = t.Frame(self.root)
        self.display_lower_right.place(x=900, width=440, y=70, height=820)
        self.show_display_lower_right()

    def show_display_top(self):
        # 标题框架
        title_frame = t.Frame(self.display_top)
        title_frame.place(x=0, width=1330, y=0, height=50)

        # 标题
        title = t.Label(title_frame, text="Device Test Tool", font=("等线", 15))
        title.pack(side=LEFT, anchor=S)

        # 版本信息
        version_info = t.Label(title_frame, text="V2022.08", font=("等线", 8))
        version_info.pack(side=RIGHT, anchor=S)

        # 分割线框架
        split_line_frame = t.Frame(self.display_top)
        split_line_frame.place(x=0, width=1330, y=50, height=10)

        # 分割线
        split_line = t.Separator(split_line_frame)
        split_line.place(x=0, width=1330, y=0)

    def show_display_lower_left(self):
        pass

    def show_display_lower_right(self):
        # 获取设备列表框架
        device_list_label_frame = t.LabelFrame(self.display_lower_right, text="获取您的设备SN")
        device_list_label_frame.place(x=10, width=430, y=10, height=100)

        self.get_device_sn_button = t.Button(device_list_label_frame, text="刷新", width=8, style=INFO)
        self.get_device_sn_button.pack(side=RIGHT, padx=10)

        self.device_sn = t.StringVar()
        get_device_sn_entry = t.Entry(device_list_label_frame, textvariable=self.device_sn, state=DISABLED)
        get_device_sn_entry.pack(side=RIGHT, padx=10, fill=X, expand=YES)
        self.device_sn.set("No devices/emulators found")

        # 执行ADB命令框架
        execute_cmd_label_frame = t.LabelFrame(self.display_lower_right, text="执行 ADB SHELL 命令")
        execute_cmd_label_frame.place(x=10, width=430, y=120, height=100)

        self.execute_cmd_button = t.Button(execute_cmd_label_frame, text="执行", width=8, style=INFO)
        self.execute_cmd_button.pack(side=RIGHT, padx=10)

        self.command = t.StringVar()
        execute_cmd_entry = t.Entry(execute_cmd_label_frame, textvariable=self.command)
        execute_cmd_entry.pack(side=RIGHT, padx=10, fill=X, expand=YES)

        # 日志框架
        self.log_text = ScrolledText(self.display_lower_right, padding=0, bootstyle=INFO, autohide=True)
        self.log_text.place(x=10, width=430, y=230, height=590)

        self.clear_log_button = t.Button(self.display_lower_right, text="清空", width=4, style=LIGHT)
        self.clear_log_button.pack(side=RIGHT, padx=35, pady=10, anchor=S)

    def log(self, text):
        """
        在日志框架中回显日志

        :param text: 日志内容
        :return: None
        """
        self.log_text.text.insert(END, "{}\n".format(text))
        self.log_text.text.see(END)


if __name__ == '__main__':
    app = MainUI()
    app.root.mainloop()
