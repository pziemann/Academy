from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_page():
    return "Main page</p>"

#endpoint get-item creation
@app.route("/get-item", methods=["GET"])
def random_number():
    random_num = randint(1,1000) #Random number 1-1000
    return f"{random_num}"

if __name__ == "__main__":
    app.run(debug=True)