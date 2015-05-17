class DefaultConfiguration(object):
    DEBUG = True
    PRODUCER_CONFIGURATION_TYPE = 'kafka' # Kafka is the only type at the moment
    PRODUCER_CONFIGURATION_HOST ='192.168.59.103'
    PRODUCER_CONFIGURATION_PORT = '9092'
    LOGFILE_PATH = "snoopy-server.log"