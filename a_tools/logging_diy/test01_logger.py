import logging

# 获取 logger 记录器
logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.DEBUG)
# 获取处理器后添加处理器到logger
logger.addHandler(logging.StreamHandler())
# 输出日志
logger.info('info')
logger.debug('debug')
# logger.error('error')
# logger.warning('warning')
# logger.critical('critical')
