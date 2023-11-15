from entities.user import User
from repositories.user_repository import user_repository as default_user_repository
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if username in self._user_repository.find_all():
            raise UserInputError("Username already in use")

        if password != password_confirmation:
            raise UserInputError("Passwords not matching")

        user_rule = "^[a-z]{3,}$"
        password_rule = "^(?=.*[^a-zA-Z])(.{8,})$"

        if not re.match(user_rule, username) or not re.match(password_rule, password):
            raise UserInputError("Username or password invalid")


user_service = UserService()
