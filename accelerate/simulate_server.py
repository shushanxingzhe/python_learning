import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'


if __name__ == '__main__':
    app.run(threaded=True)
