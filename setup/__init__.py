# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    # Server HTTP
    "gunicorn",
    # Flask libraries
    "Flask", "Flask-Cors",
    # Databases
    "Flask-PyMongo", "pymongo[srv]",
    # Web Token
    "jwt",
    # Translate strings
    "textblob",
]

call("pip install --upgrade " + ' '.join(libraries), shell=True)
call("pip freeze > ../requirements.txt", shell=True)
