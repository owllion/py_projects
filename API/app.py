from flask import Flask

app = Flask(__name__)


@app.route('/test/<int:age>')
def hello_world(age):
    return f'Hello, World! My age is {age}'
