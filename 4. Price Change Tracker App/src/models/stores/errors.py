

# Created by Sachin Dev on 03/06/18

class StoreException(Exception):
    def __init__(self, message):
        self.message = message


class StoreNotFoundException(StoreException):
    pass