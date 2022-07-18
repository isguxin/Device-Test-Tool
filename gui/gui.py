import ttkbootstrap as t
from ttkbootstrap import DANGER, WARNING, DARK, YES, RIGHT, INFO, END
from ttkbootstrap.scrolled import ScrolledText

class MainUI:
    def __init__(self):
        self.root = t.Window(
            title="Device Test Tool V2022.08",
            size=(1200, 900),
            resizable=(False, False),
            alpha=1.0
        )
        """顶部框架"""
        self.display_top = t.Frame(self.root, style=DANGER)
        self.display_top.place(x=10, width=1180, y=10, height=60)
        """左下框架"""
        self.display_lower_left = t.Frame(self.root, style=WARNING)
        self.display_lower_left.place(x=10, width=710, y=70, height=820)
        """右下框架"""
        self.display_lower_right = t.Frame(self.root, style=DARK)
        self.display_lower_right.place(x=720, width=470, y=70, height=820)
        self.show_display_lower_right()

    def show_display_top(self):
        pass

    def show_display_lower_left(self):
        pass

    def show_display_lower_right(self):
        # 获取设备列表框架
        device_list_label_frame = t.LabelFrame(self.display_lower_right, text="获取您的设备SN")
        device_list_label_frame.place(x=10, width=460, y=10, height=100)

        # 执行ADB命令框架
        execute_cmd_label_frame = t.LabelFrame(self.display_lower_right, text="执行 ADB SHELL 命令")
        execute_cmd_label_frame.place(x=10, width=460, y=120, height=100)

        # 日志框架
        self.log_text = ScrolledText(self.display_lower_right, padding=0, bootstyle=INFO, autohide=True)
        self.log_text.place(x=10, width=460, y=230, height=590)

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
