import os
import logging.handlers

# 当前文件绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def basic_log_config():
    # 1、创建日志器
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 2、创建处理器对象
    # 2.1、输出控制台的处理器
    stream_log = logging.StreamHandler()
    # 2.2、每日输出一个日志文件
    time_log = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/po_test.log", when="D",
                                                         interval=1, backupCount=2, encoding="utf-8")
    time_log.setLevel(level=logging.INFO)
    # 3、创建格式化器对象
    fmt = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)"
                                "s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 4、将格式化器对象绑定到处理器上
    stream_log.setFormatter(fmt)
    time_log.setFormatter(fmt)
    # 5、把处理器添加到日志器
    logger.addHandler(stream_log)
    logger.addHandler(time_log)
