from flask import Flask 

app = Flask(__name__)

@myapp.route("/")
def home():
    return "Hello World"

@myapp.route("/index")
def index():
    return "This is index"
if __name__ == "___main__":
    myapp.run(debub=True)
