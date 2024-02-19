import os
from functools import wraps
from time import perf_counter

from loguru import logger


class MyLogger:
    """
    根据时间、文件大小切割日志
    """

    def __init__(self, log_dir='logs', max_size=20, retention='7 days'):
        self.log_dir = log_dir
        self.max_size = max_size
        self.retention = retention
        self.logger = self.configure_logger()

    def configure_logger(self):
        """

        Returns:

        """
        # 创建日志目录
        os.makedirs(self.log_dir, exist_ok=True)

        shared_config = {
            "level": "DEBUG",
            "enqueue": True,
            "backtrace": True,
            "format": "{time:YYYY-MM-DD HH:mm:ss,SSS} | {level} | {message}",
        }

        # 添加按照日期和大小切割的文件 handler
        logger.add(
            sink=f"{self.log_dir}/{{time:YYYY-MM-DD}}.log",
            rotation=f"{self.max_size} MB",
            retention=self.retention,
            **shared_config
        )

        # 配置按照等级划分的文件 handler 和控制台输出
        logger.add(sink=self.get_log_path, **shared_config)

        return logger

    def get_log_path(self, message: str) -> str:
        """
        根据等级返回日志路径
        Args:
            message:

        Returns:

        """
        log_level = message.record["level"].name.lower()
        log_file = f"{log_level}.log"
        log_path = os.path.join(self.log_dir, log_file)

        return log_path

    def __getattr__(self, level: str):
        return getattr(self.logger, level)

    def log_decorator(self, msg="执行方法异常"):
        """
         日志装饰器，记录函数的名称、参数、返回值、运行时间和异常信息
    Args:
        logger: 日志记录器对象

    Returns:
        装饰器函数

        """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):

                start = perf_counter()  # 开始时间
                try:
                    result = func(*args, **kwargs)
                    # end = perf_counter()  # 结束时间
                    # duration = end - start
                    # self.logger.info(f"{func.__name__} 返回结果：{result}, 耗时：{duration:4f}s")
                    return result
                except Exception as e:
                    self.logger.info(f'-----------执行异常分割线-开始-----------')
                    self.logger.info(f'调用 {func.__name__} args: {args}; kwargs:{kwargs}')
                    self.logger.exception(f"{func.__name__}: {msg}")
                    self.logger.info(f"-----------执行异常分割线-结束-----------")
                    # raise e

            return wrapper

        return decorator


log = MyLogger()
