def main():
    # 导入日志模块（自动执行logging/__init__.py初始化逻辑）
    # import logging # 不这样导入
    # 导入日志处理器扩展模块（包含TimedRotatingFileHandler等高级处理器）
    import logging.handlers
    # 获取根日志记录器（未指定名称时返回RootLogger）
    # logger = logging.getLogger()
    logger = logging.getLogger("logging_diy/test01_logger.py")
    # 设置记录器的最低处理级别为DEBUG（DEBUG及以上级别日志都会被处理）
    logger.setLevel(logging.DEBUG)
    # 创建控制台处理器（将日志输出到sys.stderr）
    sh = logging.StreamHandler()
    # 创建时间轮转文件处理器（按分钟切割日志，保留2个历史文件）
    th = logging.handlers.TimedRotatingFileHandler(
        filename='handler_log.log',  # 主日志文件名
        when='M',  # 时间单位：M=分钟，S=秒，H=小时，D=天
        interval=1,  # 间隔1个时间单位切割一次
        backupCount=10  # 保留最近10个备份文件
    )

    # 设置处理器级别
    sh.setLevel(logging.INFO)
    th.setLevel(logging.DEBUG)
    # 添加格式器
    fmt = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)-8s | %(module)s.%(funcName)s:%(lineno)d | %(threadName)s | %(message)s")
    # 设置控制台处理器的格式
    sh.setFormatter(fmt)
    # 设置文件处理器的格式
    th.setFormatter(fmt)
    # 将控制台处理器添加到日志记录器
    logger.addHandler(sh)
    # 将文件处理器添加到日志记录器
    logger.addHandler(th)

    # 输出不同级别的日志（DEBUG级别因默认控制台级别WARNING不会显示）
    logger.info('info消息')  # 信息级别日志
    logger.debug('debug消息')  # 调试级别日志（需处理器级别允许）
    # logger.error('error消息')     # 错误级别
    # logger.warning('warning消息') # 警告级别
    # logger.critical('critical消息') # 严重级别


if '__main__' == __name__:
    main()
