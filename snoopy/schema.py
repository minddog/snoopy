
def get_protocol(filename):
    def parse(data):
        # TODO: This is a stub out new protocol handling
        pass

    return parse


class Responder(object):
    def __init__(self, logger, _protocol='default'):
        self.logger = logger
        self.parser = get_protocol("schemas/{}.avpr".format(_protocol))

    def respond(self, req):
        self.logger.debug("Parsing request")
        self.parser(req)

