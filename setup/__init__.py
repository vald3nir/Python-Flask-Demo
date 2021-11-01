# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    "gunicorn",  # Server HTTP
    "Flask", "Flask-Cors",  # Flask libraries
    "Flask-PyMongo", "pymongo[srv]",  # Databases
    "jwt",  # Web Token
    "googletrans==4.0.0-rc1",  # Translate strings
]

call("pip install --upgrade " + ' '.join(libraries), shell=True)
call("pip freeze > ../requirements.txt", shell=True)
