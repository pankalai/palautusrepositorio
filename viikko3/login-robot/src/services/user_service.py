from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if username in self._user_repository.find_all():
            raise UserInputError("Username already in use")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        user_rule = "^[a-z]{3,}$"
        password_rule = "^(?=.*[^a-zA-Z])(.{8,})$"

        if not re.match(user_rule, username) or not re.match(password_rule, password):
            raise UserInputError("Username or password invalid")
