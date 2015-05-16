from api import app

def find_producer(key):
    return app.CLIENT_CONNECTIONS['producer']
