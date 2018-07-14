import os
import logging
from flask import Flask, Response, request, jsonify
from tasks import long_running_task
from celery import chord


app = Flask(__name__)
app.config['DEBUG'] = True
logger = logging.getLogger(__name__)


@app.route('/', methods=['POST'])
def index():
    task = long_running_task.s().delay()
    return jsonify({'id': '', 'status': ''}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)