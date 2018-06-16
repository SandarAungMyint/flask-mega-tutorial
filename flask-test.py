from flask import Flask

myapp = Flask(__name__)
@myapp.route("/")
def hello():
    return """
    <html>
    <head><title>This is my flask app.</title></head>
    <body><h1>Hello From Flask</h1></body>
    </html>
    """

    if ___name__ == "__main__":
        myapp.run(debug=True)
