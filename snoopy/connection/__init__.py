import json
import gevent

class ProducerConnection(object):

    def __init__(self, options, logger):
        self.logger = logger
        self.connect(options)

    @staticmethod
    def create(options, logger):
        if options.get('type') == 'kafka':
            from . import connection_kafka
            return connection_kafka.KafkaConnection(options, logger)

    def connect(self, options={}):
        self.logger.debug("Connecting to {}".format(options))
        gevent.spawn(self._connect, options)

    def send(self, topic, key, value):
        self.logger.debug("Sending Topic={}/Key={}\nValue={}".format(topic, key, value))
        return self._send(topic, key, value)
