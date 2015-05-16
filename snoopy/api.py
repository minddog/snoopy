from flask import Flask, jsonify, request
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)
app.CLIENT_CONNECTIONS = {}
app.config.from_object('snoopy.config.DefaultConfiguration')
app.logger.addHandler(
    TimedRotatingFileHandler(
        app.config.get('LOGFILE_PATH'),
        when="d",
        interval=1,
        backupCount=5)
)
