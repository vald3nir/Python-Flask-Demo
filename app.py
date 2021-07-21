# coding=utf-8
# !/usr/bin/python3

import os

from flask import Flask, render_template

# Flask config
# ---------------------------------------------------------------
app = Flask(__name__)


# app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'
# app.config['CORS_HEADERS'] = 'Content-Type'

# Cors
# ---------------------------------------------------------------
# cors = CORS(app, resources={r"/*": {"origins": "*"}})


# ---------------------------------------------------------------
# Routers
# ---------------------------------------------------------------

# app.register_blueprint(user_router)
# app.register_blueprint(time_series_router)
# app.register_blueprint(eco_friendly_router)


# ---------------------------------------------------------------
# START
# ---------------------------------------------------------------

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html", message="Hello to:")


port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
