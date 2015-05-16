from flask import Flask, jsonify, request
from snoopy import producer
from snoopy import exceptions
from snoopy.connection import ProducerConnection
from snoopy.api import app
from snoopy import schema
import gevent
from gevent.wsgi import WSGIServer
from gevent.monkey import patch_all; patch_all()

@app.route("/info")
def info():
    return jsonify(status="Alive!")

@app.route("/event", methods=["POST"])
def enqueue_event():
    #pub = types.lookup_publisher(request.args.get('type'))

    responder = schema.Responder(app.logger)
    response_body = responder.respond(request.form)
    producer_type = request.form.get('type', None)
    topic = request.form.get('topic', None).encode('utf-8')
    key = request.form.get('key', None).encode('utf-8')
    value = request.form.get('value', None).encode('utf-8')

    app.logger.debug("Request to enqueue event: {}/{}={}".format(topic, key, value))

    if None in (topic, key, value):
        return jsonify(error="Insufficient arguments supplied, all fields are required.".format()), 400

    # Identify Producer based on Type
    try:
        response = producer.find_producer(producer_type).send(topic, key, value)
    except exceptions.ProducerNotFoundException, e:
        return jsonify(message=e.message, status=e.status_code), e.status_code
    except exceptions.ProducerConnectionError, e:
        return jsonify(message=e.message, status=e.status_code), e.status_code

    return jsonify(status=200)

def start_server():
    app.debug = True
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    app.CLIENT_CONNECTIONS['producer'] = ProducerConnection.create(app.config.get('PRODUCER_CONFIGURATION'), logger=app.logger)
    #gevent.spawn(consumer.start)
    http_server.serve_forever()

if __name__ == "__main__":
	start_server()
