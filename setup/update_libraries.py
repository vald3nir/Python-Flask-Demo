# coding=utf-8
# !/usr/bin/python3

from subprocess import call

import pkg_resources

packages = [dist.project_name for dist in pkg_resources.working_set]

call("pip install --upgrade " + ' '.join(packages), shell=True)
call("pip freeze > ../requirements.txt", shell=True)
