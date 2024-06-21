import datetime
import logging
import os

from config import conf
from config.conf import ConfigYaml

# 定义日志级别的映射
log_level_map = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}


# 获取初始日志信息
conf_reader = ConfigYaml()
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
log_path = conf.BASE_DIR + os.sep + conf_reader.get_conf_value('log')['log_dir']
log_extension = conf_reader.get_conf_value('log')['log_extension']
log_file = os.path.join(log_path, current_time + log_extension)
log_level = conf_reader.get_conf_value('log')['log_level']


class Logger:
    def __init__(self, log_file, log_name, log_level, log_path):
        self.log_file = log_file  # 完整的文件路径
        self.log_name = log_name
        self.log_level = log_level
        self.log_path = log_path

        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_level_map[self.log_level.lower()])

        # 确保日志文件和目录存在
        self._ensure_log_file_exists()

        # 配置日志处理器
        # if not self.logger.hasHandlers():
        self._configure_handlers()

    def _configure_handlers(self):
        """配置日志处理器"""
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 输出控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level_map[self.log_level.lower()])
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        # 写入文件
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_handler.setLevel(log_level_map[self.log_level.lower()])
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _ensure_log_file_exists(self):
        """确保日志文件存在，如果不存在则创建。"""
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)  # 确保目录存在，无需检查
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                pass  # 只创建文件，不写入内容


# 对外方法
def my_log(log_name=current_time):
    return Logger(log_file=log_file, log_name=log_name, log_level=log_level, log_path=log_path).logger


if __name__ == '__main__':
    my_log("2024-06-21.log").warning("测试日志")
