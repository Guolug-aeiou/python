# 示例：在 app/main.py 中使用
from pathlib import Path

from a_tools.logging_format.logger_factory import LoggerFactory

# 获取日志对象（单例模式）
logger = LoggerFactory.get_logger(
    name="app",
    level="DEBUG",
    log_file=Path(__file__).parent / "app.log",
)

def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    main()