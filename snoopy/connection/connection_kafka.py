from kafka import KeyedProducer, KafkaClient
from . import ProducerConnection
from ..exceptions import ProducerConnectionError
from kafka.common import KafkaUnavailableError
import gevent
from gevent.monkey import patch_all; patch_all()

class KafkaConnection(ProducerConnection):
    producer = None
    client = None

    __default_options = {
        'host': None,
        'port': None,
        'batch': False,
        'batch_every_n': 20,
        'batch_send_every_t': 60,
    }

    def __init__(self, options, logger):
        self.logger = logger
        self.connect(options)

    def _connect(self, options):
        try:
            self.client = KafkaClient("{}:{}".format(options.get('host'), options.get('port')))
            self.producer = KeyedProducer(self.client, batch_send=options.get('batch'),
                                        batch_send_every_n=options.get('batch_every_n'),
                                        batch_send_every_t=options.get('batch_send_every_t'))
        except KafkaUnavailableError, e:
            self.logger.warn("Unable to connect: ", e)
            raise ProducerConnectionError(e)

    def _send(self, topic, key, value):
        def _sender_handler(e):
            if type(e) is TypeError:
                print "Type Error"

        if False in map(lambda x: type(x) != unicode, (topic, key, value)):
            raise TypeError("Make sure topic, key, and value are all utf-8 encoded.")

        if(self.producer is None):
            raise ProducerConnectionError("Unable to connect to Producer")

        _sender = gevent.spawn(self.producer.send, topic, key, value)
        _sender.link_exception(_sender_handler)