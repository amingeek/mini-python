class UserRepository:
    def __init__(self):
        self._users = []

    def save(self, username):
        self._users.append(username)

    def get_all(self):
        return self._users
