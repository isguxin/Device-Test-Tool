from gui.main_gui import MainUI
from ttkbootstrap.constants import END


class LogInfo(MainUI):
    def __init__(self):
        super().__init__()

        self.clear_log_button["command"] = lambda: self.thread_it(self.clear_log)

    def clear_log(self):
        """
        清除日志内容

        :return: None
        """
        self.log_text.text.delete(0.0, END)
        self.log_text.text.insert(END, "Information display\n")
        self.log_text.text.insert(END, "------------------------------------------\n")
