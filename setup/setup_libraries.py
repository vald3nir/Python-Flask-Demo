from subprocess import call

import pkg_resources

libraries = [
    "Flask",
    "Flask-Cors",
    "Flask-PyMongo",
    "pymongo[srv]"
]
call("pip install " + ' '.join(libraries), shell=True)

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)

call("pip freeze > ../requirements.txt", shell=True)