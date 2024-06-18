import logging

# 设置日志的基本参数（也可在后续对logger进行单独设置）
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("log_demo")
print(type(logger))
logger.debug("debug")
logger.info("info")
logger.warning("warning")
