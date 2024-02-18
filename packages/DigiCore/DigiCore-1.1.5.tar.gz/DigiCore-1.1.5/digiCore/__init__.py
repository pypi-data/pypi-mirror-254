"""
Decorate 中间件

"""
import random
import time
from loguru import logger
from functools import wraps


class ServiceDBinfo():

    @classmethod
    def get_tidb_info(cls):
        """
        获取生产环境tidb配置
        """
        hostnames = ['192.168.0.200','192.168.0.201','192.168.0.202']
        return {
            "hostname": random.choice(hostnames),
            "username": "root",
            "port": 4000,
            "password": "DoocnProTidb200."
        }


    @classmethod
    def get_redis_info(cls):
        """
        获取生产环境redis配置
        """
        return {
                "hostname": "192.168.0.201",
                "port": 16379,
                "password": "DoocnProRedis201."
            }


    @classmethod
    def get_mongodb_info(cls):
        """
        获取生产环境mongodb配置
        """
        return "mongodb://root:DoocnProMongoDB201.@192.168.0.201:57017/"



class Decorate():
    @classmethod
    def def_retry(cls, msg=None, error_type=None, max_retry_count: int = 5, time_interval: int = 2):
        """
        任务重试装饰器
        Args:
        max_retry_count: 最大重试次数 默认5次
        time_interval: 每次重试间隔 默认2s
        """

        def _retry(task_func):
            @wraps(task_func)
            def wrapper(*args, **kwargs):
                for retry_count in range(max_retry_count):
                    try:
                        task_result = task_func(*args, **kwargs)
                        return task_result
                    except Exception as e:
                        logger.error(msg if msg else f"{max_retry_count}： 函数报错，正在重试！")
                        logger.error(f'error message:{e.args}')
                        time.sleep(time_interval)
                return error_type if error_type else 4001

            return wrapper

        return _retry