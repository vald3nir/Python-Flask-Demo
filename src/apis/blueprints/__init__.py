from src.apis.blueprints.auth import auth_blueprint
from src.apis.blueprints.home import home_blueprint
from src.apis.blueprints.users import user_blueprint

# ------------------------------------------------------------------
# Blueprints
# ------------------------------------------------------------------

blueprints = [
    home_blueprint,
    user_blueprint,
    auth_blueprint,
]
