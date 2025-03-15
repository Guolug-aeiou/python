"""
本模块提供高级日志工厂类，支持彩色控制台输出、文件记录及多日志器管理
"""

import logging
import sys
from pathlib import Path
from typing import Optional, Union
from colorama import Fore, Style, init  # 控制台颜色渲染库

# 初始化colorama以支持Windows系统的ANSI转义序列
init(autoreset=True)  # 自动重置样式避免颜色污染后续输出


class LoggerFactory:
    """
    日志工厂类，采用单例模式和工厂模式设计
    特征：
    1. 支持彩色控制台输出和纯文本文件输出双通道
    2. 内置线程安全的日志器缓存机制
    3. 支持自定义日志格式和时间格式
    4. 兼容多模块独立日志配置需求
    """

    # 日志级别-颜色映射表（DEBUG级：青色，INFO：绿色，WARNING：黄色，ERROR：红色，CRITICAL：品红加亮）
    LOG_COLORS = {
        logging.DEBUG: Fore.CYAN,  # 调试信息（开发阶段可见）
        logging.INFO: Fore.GREEN,  # 常规运行信息
        logging.WARNING: Fore.YELLOW,  # 潜在问题警告
        logging.ERROR: Fore.RED,  # 功能错误（需处理但系统仍可运行）
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,  # 致命错误（系统关键故障）
    }

    # 单例模式缓存字典，维护已创建的日志器实例（键：日志器名称，值：日志器对象）
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
        """
        获取或创建预配置的日志器

        参数：
        name: 日志器名称（不同名称对应独立配置，建议按模块命名）
        level: 日志处理级别（DEBUG/INFO/WARNING/ERROR/CRITICAL 或对应数值）
        log_file: 日志文件路径（None时不启用文件记录）
        fmt: 自定义日志格式字符串（None时使用预设彩色格式）
        datefmt: 时间显示格式（遵循datetime.strftime格式规范）

        返回：
        配置完成的日志器实例（自动缓存复用）
        """
        # 存在缓存直接返回（避免重复配置）
        if name in cls._loggers:
            return cls._loggers[name]

        # 创建指定名称的日志器实例
        logger = logging.getLogger(name)

        # 设置日志处理级别（自动转换字符串格式为数值）
        logger.setLevel(level)

        # 防止重复添加处理器（应对其他代码可能修改根日志器的情况）
        if logger.handlers:
            return logger

        # 默认日志格式（控制台彩色格式）
        default_fmt = (
            f"{Fore.WHITE}{Style.DIM}%(asctime)s{Style.RESET_ALL} | "  # 灰色时间戳
            f"%(color)s%(levelname)-8s{Style.RESET_ALL} | "  # 带色级别
            f"{Fore.BLUE}%(module)s.%(funcName)s:%(lineno)d{Style.RESET_ALL} | "  # 蓝色代码位置
            f"{Fore.MAGENTA}%(threadName)s{Style.RESET_ALL} | "  # 品红线程信息
            f"%(color)s%(message)s{Style.RESET_ALL}"  # 带色日志消息
        )

        # === 控制台处理器配置 ===
        # 创建标准输出流处理器（避免与第三方库的stderr输出冲突）
        console_handler = logging.StreamHandler(sys.stdout)
        # 加载颜色格式化器（动态注入颜色字段）
        console_handler.setFormatter(cls._colored_formatter(fmt or default_fmt, datefmt))
        logger.addHandler(console_handler)

        # === 文件处理器配置 ===
        if log_file:
            # 创建文件处理器（自动处理路径类型）
            file_handler = logging.FileHandler(log_file)
            # 文件日志格式（去除颜色控制字符）
            file_fmt = fmt or (
                "%(asctime)s | %(levelname)-8s | "  # 时间|级别
                "%(module)s.%(funcName)s:%(lineno)d | "  # 模块.函数名:行号
                "%(threadName)s | %(message)s"  # 线程名|消息
            )
            file_handler.setFormatter(logging.Formatter(fmt=file_fmt, datefmt=datefmt))
            logger.addHandler(file_handler)

        # 缓存配置完成的日志器
        cls._loggers[name] = logger
        return logger

    @classmethod
    def _colored_formatter(cls, fmt: str, datefmt: str) -> logging.Formatter:
        """
        创建颜色格式化器的工厂方法

        内部实现：
        1. 继承Formatter类扩展颜色处理能力
        2. 通过动态注入record.color字段实现颜色绑定
        3. 保持与标准Formatter的兼容性
        """

        class ColoredFormatter(logging.Formatter):
            """颜色格式化器（动态绑定颜色到日志记录）"""

            def format(self, record):
                # 根据日志级别获取对应颜色
                record.color = cls.LOG_COLORS.get(record.levelno, Fore.WHITE)
                # 调用父类方法完成标准格式化
                return super().format(record)

        return ColoredFormatter(fmt=fmt, datefmt=datefmt)