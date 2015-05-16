class ProducerNotFoundException(Exception):
    message = 'Unable to locate configured producer'
    status_code = 400

class ProducerConnectionError(Exception):
    message = 'Unable to connect to producer'
    status_code = 500