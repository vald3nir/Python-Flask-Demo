# coding=utf-8
# !/usr/bin/python3

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello MOACI!"


@app.route('/signal', methods=['POST'])
def post_signal():
    content = {}
    if request.is_json:
        content = request.get_json()
        current_signal_temp = (content["current_signal_temp"])
        print(current_signal_temp)
    return content


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
