# --------------------------------------------------------------------------

class ObjectDTO:

    def __init__(self, created_at=None) -> None:
        self.created_at = created_at

    def to_json(self):
        return {"created_at": self.created_at}

    def __str__(self) -> str:
        return str(self.to_json())


# --------------------------------------------------------------------------

class UserDTO(ObjectDTO):

    def __init__(self, user_id, name, password, email, created_at=None) -> None:
        super().__init__(created_at)
        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email

    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
            "created_at": self.created_at
        }

    def get_data_mutable(self):
        return {
            "name": self.name,
            "email": self.email,
        }

# --------------------------------------------------------------------------
