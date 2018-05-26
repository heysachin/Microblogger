# Created by Sachin Dev on 26/05/18

from models.database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date,
            'id': self.id
        }

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
