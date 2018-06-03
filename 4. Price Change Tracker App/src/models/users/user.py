# Created by Sachin Dev on 01/06/18
import uuid

from common.database import Database
from common.utils import Utils
import models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        Method Verifies if email and combo is valid
        if email exist and password associated with that email is correct
        :param email: The user's email
        :param password: A sha512 hashed password
        :return True if valid, False otherwise
        """

        user_data = Database.find_one("users", {"email": email})  # Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # Tell user that their email doesnt exist
            raise UserErrors.UserError("User Doesn't Exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user that the password is wrong
            raise UserErrors.UserError("Password is wrong")

        return True

    @staticmethod
    def register_user(email, password):
        """
        Registers user using Email and Password
        :param email: users email id (can be invalid)
        :param password: sha512-hashed password
        :return: True if registered succesfully
        """
        user_data = Database.find_one('users', {"email": email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("The e-mail already Exists")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("This e-mail is not in the right format.")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
