from digiCore import ServiceDBinfo
from digiCore.dsd_kafka import KafkaDao
from digiCore.dsd_mongodb import MongoDao
from digiCore.dsd_mysql import TiDBDao
from digiCore.dsd_redis import RedisDao


class InstantiationDB:
    """
    实例化数据库对象
    """
    def load_tidb_ob(self):
        """
        实例化tidb数据库对象
        :return:
        """
        service = ServiceDBinfo.get_tidb_info()
        tidb_ob = TiDBDao(
            host=service['hostname'],
            user=service['username'],
            port=service['port'],
            passwd=service['password']
        )
        return tidb_ob

    def load_redis_ob(self):
        """
        实例化redis对象
        :param service:
        :return:
        """
        service = ServiceDBinfo.get_redis_info()
        redis_ob = RedisDao(
            host=service['hostname'],
            port=service['port'],
            password=service['password'],
            db=5
        )
        return redis_ob

    def load_mongodb_ob(self):
        """
        实例化mongodb对象
        :param service:
        :return: mongodb://root:DoocnProMongoDB201.@192.168.0.201:57017/
        """
        mongodb_url = ServiceDBinfo.get_mongodb_info()
        mongo_ob = MongoDao(
            mongodb_url=mongodb_url
        )
        return mongo_ob

    def load_kafka_ob(self, topic: str,
                      partition: int,
                      brokers=None,
                      sub_server='Test'):
        """
        实例化kafka对象
        :return:
        """
        if brokers is None:
            brokers = ['192.168.0.201:9092', '192.168.0.200:9092', '192.168.0.12:9092']

        kafka_ob = KafkaDao(topic,partition,brokers,sub_server)
        return kafka_ob
