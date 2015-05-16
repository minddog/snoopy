class DefaultConfiguration(object):
    DEBUG = True
    PRODUCER_CONFIGURATION = {
        'type': 'kafka', # Kafka is the only type at the moment
        'host': '192.168.59.103',
        'port': '9092',
    }
    LOGFILE_PATH = "snoopy-server.log"