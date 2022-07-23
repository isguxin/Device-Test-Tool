import configparser


class ConfigUtil:

    def __init__(self, file_path):
        """
        初始化

        :param file_path: config文件路径
        """
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path, encoding="utf-8")

    def get_sections_list(self):
        """
        获取config文件中的section

        :return: config文件section列表
        """
        sections_list = self.config.sections()
        return sections_list

    def get_options_name(self, section_name):
        """
        获取config文件中对应section下的所有option

        :param section_name: section名称
        :return: section下的所有option列表
        """
        options_list = self.config.options(section_name)
        return options_list

    def get_option_value(self, section_name, option_name):
        """
        获取config文件中对应option的value值

        :param section_name: section名称
        :param option_name: option名称
        :return: option对应的值
        """
        option_value = self.config.get(section_name, option_name)
        return option_value


if __name__ == '__main__':
    config = ConfigUtil("../device-test-tool.ini")
    print(config.get_sections_list())
    print(config.get_options_name("设备操作"))
    print(config.get_option_value("设备操作", "重新启动"))
