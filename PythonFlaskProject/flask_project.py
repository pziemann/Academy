from flask import Flask, url_for
from random import randint
import logging
import os
import flask
import platform

app_version = "1.0.1"

logging.basicConfig(level=logging.DEBUG)
#Version of the application
print(f"Starting Flask application version {app_version}")
#Initialize the app
app = Flask(__name__)

#Main page
@app.route("/", methods=["GET"])
def main_page():
    log_messages = log_levels()
    env_info = get_envs()
    endpoints_info = get_endpoints()
    return f"<h1>Log levels:</h1>{log_messages}<br><h1>Environment variables:</h1>{env_info}<br><h1>Endpoints:</h1><br>{endpoints_info}"

#Endpoint get-item creation
@app.route("/get-item", methods=["GET"])
def random_number():
    random_num = randint(0, 1000)  # Random number 0-1000    
    return f"{random_num}"

#Route to give name, surname in the endpoint
@app.route("/namesurname/")
@app.route("/namesurname/<name>")
def name_surname(name):
    return "Hello, " + name

#Author
@app.route("/author")
def author_print():
    return "Paweł Ziemann"

#Flask version
@app.route("/flask-version", methods=["GET"])
def show_flask_version():
    flask_version = flask.__version__
    return f"Flask Version: {flask_version}"

#Python version
@app.route("/python-version", methods=["GET"])
def show_python_version():
    python_version = platform.python_version()
    return f"Python Version: {python_version}"

#Function to retrieve log levels (default log levels)
def log_levels():
    default_levels = []
    for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        level_name = logging.getLevelName(level)
        default_levels.append(f"{level_name}: {level}")
    return "<br>".join(default_levels)

#Function to retrieve envs
def get_envs():
    env_info = []
    for key, value in os.environ.items():
        env_info.append(f"{key}: {value}")
    return "<br>".join(env_info)

#Function to get endpoints
def get_endpoints():
    endpoints_info = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            endpoint_url = url_for(rule.endpoint)
            endpoints_info.append(f"{rule.endpoint}: {endpoint_url}")
    return "<br>".join(endpoints_info)
