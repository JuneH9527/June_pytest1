import os
from utils.YamlUtil import YamlReader


_file_name = 'config.yml'  # 配置文件名
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
_config_path = os.path.dirname(__file__)
_config_file = _config_path + os.sep + _file_name   # 配置文件路径


class ConfigYaml:
    def __init__(self, file_path=None):
        self.config = {}

        # 提供一个默认配置文件路径
        default_config_path = _config_file
        if file_path is None:
            file_path = default_config_path

        # 对传入的file_path进行有效性检查
        if not isinstance(file_path, str):
            raise ValueError("File path must be a string.")

        try:
            config_file = get_config_file()
            self.config = YamlReader(config_file).read()
        except (FileNotFoundError, PermissionError) as e:
            # 对于文件不存在或无权限读取的情况，给出友好的错误提示并处理
            print(f"Error accessing the config file: {e}")
            self.config = {}  # 初始化为空字典以避免后续访问引发错误
        except Exception as e:
            print(f"Error: {e}")
            self.config = {}  # 初始化为空字典以避免后续访问引发错误

    def get_conf_value(self, key):
        return self.config[key]


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


if __name__ == '__main__':
    conf_reader = ConfigYaml()
