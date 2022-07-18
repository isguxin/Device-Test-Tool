import threading

import ttkbootstrap as t
from ttkbootstrap import DANGER, WARNING, DARK, YES, RIGHT, INFO, END, Y, X, DISABLED, N, S, E, LIGHT, LEFT
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
        self.show_display_lower_left()
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
        # 获取设备信息框架
        get_device_info_label_frame = t.LabelFrame(self.display_lower_left, text="获取设备信息")
        get_device_info_label_frame.place(x=0, width=880, y=10, height=150)

        # 设备信息框架
        device_info_display_frame = t.Frame(get_device_info_label_frame, style=DANGER)
        device_info_display_frame.place(x=0, width=750, y=5, height=115)

        self.device_info_checkbutton_0_0 = t.Checkbutton(device_info_display_frame, width=10, style="round-toggle")
        self.device_info_checkbutton_0_0.grid(row=0, column=0, padx=10, pady=2)

        self.device_info_checkbutton_0_1 = t.Checkbutton(device_info_display_frame, width=10, style="round-toggle")
        self.device_info_checkbutton_0_1.grid(row=0, column=1, padx=10, pady=2)

        self.device_info_checkbutton_0_2 = t.Checkbutton(device_info_display_frame, width=10, style="round-toggle")
        self.device_info_checkbutton_0_2.grid(row=0, column=2, padx=10, pady=2)

        self.device_info_checkbutton_0_3 = t.Checkbutton(device_info_display_frame, width=10, style="round-toggle")
        self.device_info_checkbutton_0_3.grid(row=0, column=3, padx=10, pady=2)

        self.device_info_checkbutton_1_0 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_1_0.grid(row=1, column=0, padx=5, pady=2)

        self.device_info_checkbutton_1_1 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_1_1.grid(row=1, column=1, padx=5, pady=2)

        self.device_info_checkbutton_1_2 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_1_2.grid(row=1, column=2, padx=5, pady=2)

        self.device_info_checkbutton_1_3 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_1_3.grid(row=1, column=3, padx=5, pady=2)

        self.device_info_checkbutton_1_4 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_1_4.grid(row=1, column=4, padx=5, pady=2)

        self.device_info_checkbutton_2_0 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_2_0.grid(row=2, column=0, padx=5, pady=2)

        self.device_info_checkbutton_2_1 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_2_1.grid(row=2, column=1, padx=5, pady=2)

        self.device_info_checkbutton_2_2 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_2_2.grid(row=2, column=2, padx=5, pady=2)

        self.device_info_checkbutton_2_3 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_2_3.grid(row=2, column=3, padx=5, pady=2)

        self.device_info_checkbutton_2_4 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_2_4.grid(row=2, column=4, padx=5, pady=2)

        self.device_info_checkbutton_3_0 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_3_0.grid(row=3, column=0, padx=5, pady=2)

        self.device_info_checkbutton_3_1 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_3_1.grid(row=3, column=1, padx=5, pady=2)

        self.device_info_checkbutton_3_2 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_3_2.grid(row=3, column=2, padx=5, pady=2)

        self.device_info_checkbutton_3_3 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_3_3.grid(row=3, column=3, padx=5, pady=2)

        self.device_info_checkbutton_3_4 = t.Checkbutton(device_info_display_frame, width=8, style="round-toggle")
        self.device_info_checkbutton_3_4.grid(row=3, column=4, padx=5, pady=2)

        # 获取按钮
        self.get_device_info_button = t.Button(get_device_info_label_frame, text="查询", width=8, style=INFO)
        self.get_device_info_button.pack(side=RIGHT, padx=10)

        # 设备操作框架
        device_operator_label_frame = t.LabelFrame(self.display_lower_left, text="操作您的设备")
        device_operator_label_frame.place(x=0, width=260, y=170, height=100)

        self.restart_device_button = t.Button(device_operator_label_frame, text="Restart", width=8, style=INFO)
        self.restart_device_button.pack(side=LEFT, padx=10)

        self.remount_device_button = t.Button(device_operator_label_frame, text="Remount", width=8, style=INFO)
        self.remount_device_button.pack(side=RIGHT, padx=10)

        # 设备日志操作框架

        # 环境安装框架

        # DFX框架


    def show_display_lower_right(self):
        # 获取设备列表框架
        device_list_label_frame = t.LabelFrame(self.display_lower_right, text="获取您的设备SN")
        device_list_label_frame.place(x=10, width=430, y=10, height=100)

        self.get_device_sn_button = t.Button(device_list_label_frame, text="刷新", width=8, style=INFO)
        self.get_device_sn_button.pack(side=RIGHT, padx=10)

        self.get_device_sn_combobox = t.Combobox(device_list_label_frame, style=INFO, values=["No devices found"])
        self.get_device_sn_combobox.pack(side=RIGHT, padx=10, fill=X, expand=YES)
        self.get_device_sn_combobox.current(0)

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
        self.log_text.text.insert(END, "Information display\n")
        self.log_text.text.insert(END, "------------------------------------------\n")

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

    @staticmethod
    def thread_it(func, *args):
        """
        UI与操作分离多进程

        :param func: 方法
        :param args: 参数
        :return: None
        """
        thread = threading.Thread(target=func, args=args)
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    app = MainUI()
    app.root.mainloop()
