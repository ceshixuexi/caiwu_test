import logging.handlers
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

#初始化日志配置
def init_log_config():
    #创建日志器
    #创建处理器
    #创建格式化器
    #把格式化器添加到处理器中
    #把处理器添加到日志器
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    sh=logging.StreamHandler()
    log_path=BASE_DIR+'../log/caiwu.log'
    fh=logging.handlers.TimedRotatingFileHandler(log_path,when="midnight",interval=1,backupCount=5,encoding='UTF-8')
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s[%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s")
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)

