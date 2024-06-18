import logging

# 创建日志对象
logger = logging.getLogger("log_stream_demo")
logger_file = logging.getLogger("log_file_demo")
# 设置日志级别
logger.setLevel(logging.DEBUG)
logger_file.setLevel(logging.DEBUG)
# 创建日志输出对象
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log_file_demo.log")
# 设置日志输出格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# 添加日志输出对象
logger.addHandler(stream_handler)
logger_file.addHandler(file_handler)

logger.debug("test")
logger_file.debug("file_test")
logger_file.info("123")
logger_file.warning("wa")

