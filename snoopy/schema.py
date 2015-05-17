from collections import namedtuple
from .exceptions import MissingArgumentException


def get_protocol_parser(filename):
    def parse(data):
        # Convert to utf8 values
        def utf8_convert(key):
            if data[key]:
                data[key] = data[key].encode('utf-8')
        map(utf8_convert, data.iterkeys())

        # TODO: This is a stub out new protocol handling, currently passthrough with no validation
        Payload = namedtuple('Payload', data)
        payload = Payload(**data)

        if None in (payload.topic, payload.key, payload.value):
            raise MissingArgumentException

        return payload

    return parse


class Responder(object):
    def __init__(self, logger, _protocol='default'):
        self.logger = logger
        self.parser = get_protocol_parser("schemas/{}.avpr".format(_protocol))

    def respond(self, req):
        self.logger.debug("Parsing request")
        return self.parser(req)

