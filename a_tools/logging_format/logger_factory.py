import logging
import sys
from pathlib import Path
from typing import Optional, Union
from colorama import Fore, Style, init

# 初始化 colorama（用于控制台颜色）
init(autoreset=True)


class LoggerFactory:
    """日志工厂类，用于创建预配置的日志对象"""

    # 日志级别颜色映射
    LOG_COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,
    }

    # 单例模式缓存
    _loggers = {}

    @classmethod
    def get_logger(
            cls,
            name: str = "root",
            level: Union[int, str] = logging.DEBUG,
            log_file: Optional[Union[str, Path]] = None,
            fmt: Optional[str] = None,
            datefmt: str = "%Y-%m-%d %H:%M:%S"
    ) -> logging.Logger:
        """获取或创建预配置的日志对象

        Args:
            name: 日志器名称（用于区分不同模块）
            level: 日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
            log_file: 日志文件路径（None 表示不输出到文件）
            fmt: 自定义日志格式（None 使用默认格式）
            datefmt: 时间格式
        """
        # 如果已存在同名日志对象，直接返回
        if name in cls._loggers:
            return cls._loggers[name]

        # 创建日志对象
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # 避免重复添加处理器
        if logger.handlers:
            return logger

        # 默认日志格式
        default_fmt = (
            f"{Fore.WHITE}{Style.DIM}%(asctime)s{Style.RESET_ALL} | "
            f"%(color)s%(levelname)-8s{Style.RESET_ALL} | "
            f"{Fore.BLUE}%(module)s.%(funcName)s:%(lineno)d{Style.RESET_ALL} | "
            f"{Fore.MAGENTA}%(threadName)s{Style.RESET_ALL} | "
            f"%(color)s%(message)s{Style.RESET_ALL}"
        )

        # 创建控制台处理器（带颜色）
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(cls._colored_formatter(fmt or default_fmt, datefmt))
        logger.addHandler(console_handler)

        # 创建文件处理器（无颜色）
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_fmt = fmt or (
                "%(asctime)s | %(levelname)-8s | %(module)s.%(funcName)s:%(lineno)d | "
                "%(threadName)s | %(message)s"
            )
            file_handler.setFormatter(logging.Formatter(fmt=file_fmt, datefmt=datefmt))
            logger.addHandler(file_handler)

        # 缓存日志对象
        cls._loggers[name] = logger
        return logger

    @classmethod
    def _colored_formatter(cls, fmt: str, datefmt: str) -> logging.Formatter:
        """创建带颜色的日志格式化器"""

        class ColoredFormatter(logging.Formatter):
            def format(self, record):
                # 动态注入颜色字段
                record.color = cls.LOG_COLORS.get(record.levelno, Fore.WHITE)
                return super().format(record)

        return ColoredFormatter(fmt=fmt, datefmt=datefmt)