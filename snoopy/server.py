from flask import Flask, jsonify, request
from snoopy import producer
from snoopy import exceptions
from snoopy.connection import ProducerConnection
from snoopy.api import app
from snoopy import schema
import gevent
from gevent.wsgi import WSGIServer
from gevent.monkey import patch_all; patch_all()
import argparse

@app.route("/info")
def info():
    return jsonify(status="Alive!")

@app.route("/event", methods=["POST"])
def enqueue_event():
    try:
        responder = schema.Responder(app.logger)
        producer_type = request.form.get('type', None)
        payload = responder.respond({
            'topic': request.form.get('topic', None),
            'key': request.form.get('key', None),
            'value': request.form.get('value', None),
        })

        app.logger.debug("Request to enqueue event: {}/{}={}".format(payload.topic, payload.key, payload.value))

        # Identify Producer based on Type
        response = producer.find_producer(producer_type).send(payload)
        print response
    except exceptions.MissingArgumentException, e:
        return jsonify(message=e.message, status=e.status_code), e.status_code
    except exceptions.ProducerNotFoundException, e:
        return jsonify(message=e.message, status=e.status_code), e.status_code
    except exceptions.ProducerConnectionError, e:
        return jsonify(message=e.message, status=e.status_code), e.status_code

    return jsonify(status=200)

def parse_args():
    parser = argparse.ArgumentParser(description="Snoopy Daemon")
    parser.add_argument('--producer-host', dest='producer_host', action='store')
    parser.add_argument('--producer-type', dest='producer_type', action='store', default='kafka')
    parser.add_argument('--producer-port', dest='producer_port', action='store')
    args = parser.parse_args()
    app.config.from_object('snoopy.config.DefaultConfiguration')
    app.config.update(PRODUCER_CONFIGURATION_HOST=args.producer_host,
                      PRODUCER_CONFIGURATION_PORT=args.producer_port,
                      PRODUCER_CONFIGURATION_TYPE=args.producer_type)

def start_server():
    parse_args()
    app.debug = True
    http_server = WSGIServer(('0.0.0.0', 5000), app)

    options = {
        'type': app.config.get('PRODUCER_CONFIGURATION_TYPE'),
        'host': app.config.get('PRODUCER_CONFIGURATION_HOST'),
        'port': app.config.get('PRODUCER_CONFIGURATION_PORT'),
    }

    app.CLIENT_CONNECTIONS['producer'] = ProducerConnection.create(options, logger=app.logger)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server()
