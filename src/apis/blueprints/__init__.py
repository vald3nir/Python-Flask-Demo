from src.apis.blueprints.auth import auth_blueprint
from src.apis.blueprints.users import user_blueprint

# ------------------------------------------------------------------
# Blueprints
# ------------------------------------------------------------------

blueprints = [
    user_blueprint,
    auth_blueprint,
]
