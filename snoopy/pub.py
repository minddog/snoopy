from snoopy.connection import ProducerConnection
import hashlib

SECRETS = {}

class SnoopyStream(object):
    def __init__(self, topic, signature, _filter):
        self.topics = list()
        self.invalid = validate_signature(signature, topic)

    def add_topic(self, topic, signature):
        SECRETS[get_topic_address(topic)] = signature
        self.topics.append((topic, get_topic_address(topic)))

def get_topic_address(topic_filter):
    return topic_filter.replace('*', '__all__')

def create_authorized_stream(topic, signature, _filter=None):
    return SnoopyStream(topic, signature, _filter)

def sign_secret(secret, topic='*'):
    # TODO: Migrate from dirty cheap signatures to CA-based
    md5 = hashlib.md5()
    topic_address = get_topic_address(topic)
    md5.update("{}-{}".format(topic_address, secret))
    return md5.hexdigest()

def validate_signature(signature, topic):
    return signature == SECRETS[topic]