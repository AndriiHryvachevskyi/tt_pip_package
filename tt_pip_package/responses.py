from addict import Dict

class User:
    def __init__(self, data: Dict):
        self.id = data.get("id")
        self.name = data.get("name")
        self.username = data.get("username")
        self.email = data.get("email")
        self.phone = data.get("phone")
        self.website = data.get("website")

    def __repr__(self) -> str:
        return (
            f"User(id={self.id}, name={self.name}, username={self.username} "
            f"email={self.email}, phone={self.phone}, website={self.website}) "
        )