from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Main page</p>"

@app.route("/get-item")
def random_numer():
    return "Hello world</p>"

if __name__ == "__main__":
    app.run()