import os
import sys
import time
import logging
from logging.handlers import RotatingFileHandler

import psycopg2
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(filename="logs/std.log",
					format='%(asctime)s %(message)s',
					filemode='w')

logger=logging.getLogger()

#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

big_array = np.ones(1000 * 1024**2, dtype=np.uint8)

def check_config_file():

    if not os.path.exists('config.cfg'):
        logger.info("Config file does not exist")
        sys.exit("Config file does not exist")

def create_db_connection():

    try:
        conn = psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        return False

@app.route('/')
def hello_world():

    logger.info("Application is working")
    return 'I am working :))))'


@app.route('/health')
def health_check():

    try:
        conn = psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        db_status = 'up'
        return jsonify({'status': 'up', 'database': db_status}), 200

    except psycopg2.Error:
        db_status = 'down'
        return jsonify({'status': 'down', 'database': db_status}), 500


if __name__ == '__main__':
    check_config_file()
    time.sleep(15)
    create_db_connection()
    big_array2 = np.ones(4000 * 1024 ** 2, dtype=np.uint8)

    app.run(host='0.0.0.0', port=5005)
