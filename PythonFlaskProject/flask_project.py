from flask import Flask, url_for
from random import randint
import logging
import os

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

#Main page
@app.route("/", methods=["GET"])
def main_page():

    log_messages = log_levels()
    env_info = get_envs()
    endpoints_info = get_endpoints()
    return f"<h1>Log levels:</h1>{log_messages}<br><h1>Environment variables:</h1>{env_info}<br><h1>Endpoints:</h1><br>{endpoints_info}"
# Endpoint get-item creation
@app.route("/get-item", methods=["GET"])
def random_number():
    random_num = randint(0, 1000)  # Random number 0-1000    
    return f"{random_num}"


# Function to retrieve log levels and messages
def log_levels():
    default_levels = []
    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        level_name = logging.getLevelName(level)
        default_levels.append(f"{level_name}: {level}")
    return "<br>".join(default_levels)
def get_envs():
    env_info = []
    for key, value in os.environ.items():
        env_info.append(f"{key}: {value}")
    return "<br>".join(env_info)

def get_endpoints():
    endpoints_info = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            endpoint_url = url_for(rule.endpoint)
            endpoints_info.append(f"{rule.endpoint}: {endpoint_url}")
    return "<br>".join(endpoints_info)

if __name__ == "__main__":
    app.run(debug=True)
