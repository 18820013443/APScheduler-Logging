import logging

'''
https://www.jianshu.com/p/feb86c06c4f4
'''

# 创建记录器
logger = logging.getLogger()

# 创建处理器
fileHandler = logging.FileHandler(filename='log.txt', mode='a', encoding='utf-8', delay=False)

# 创建格式化器
fmt = "[%(asctime)-15s]-%(levelname)s-%(filename)s-%(lineno)d-%(process)d-%(message)s"
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt, datefmt)

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

# 打印日志信息
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
