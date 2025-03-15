# 导入日志处理器扩展模块（包含TimedRotatingFileHandler等高级处理器）
import logging.handlers


class LoggerPack:
    logger = None

    @classmethod
    def get_logger_pack(cls):
        if cls.logger is None:
            # 获取根日志记录器（未指定名称时返回RootLogger）
            cls.logger = logging.getLogger("[admin]")
            # 设置处理级别
            cls.logger.setLevel(logging.DEBUG)
            # 创建控制台处理器（将日志输出到sys.stderr）
            sh = logging.StreamHandler()
            # 创建时间轮转文件处理器（按分钟切割日志，保留5个历史文件）
            th = logging.handlers.TimedRotatingFileHandler(
                filename='handler_log.log',  # 主日志文件名
                when='M',  # 时间单位：M=分钟，S=秒，H=小时，D=天
                interval=1,  # 间隔1个时间单位切割一次
                backupCount=5  # 保留最近5个备份文件
            )
            # 设置处理器级别
            sh.setLevel(logging.INFO)
            th.setLevel(logging.INFO)
            # 添加格式器
            fmt = logging.Formatter(
                "%(asctime)s | %(name)s | %(levelname)-8s | %(module)s.%(funcName)s:%(lineno)d | %(threadName)s | %(message)s")
            # 设置控制台处理器的格式
            sh.setFormatter(fmt)
            # 设置文件处理器的格式
            th.setFormatter(fmt)
            # 将控制台处理器添加到日志记录器
            cls.logger.addHandler(sh)
            # 将文件处理器添加到日志记录器
            cls.logger.addHandler(th)
            return cls.logger
        else:
            return cls.logger


if '__main__' == __name__:
    logger = LoggerPack.get_logger_pack()
    logger.info('info')
    logger.error('error')
    logger.warning('warning')
