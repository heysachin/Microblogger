# Created by Sachin Dev on 26/05/18

from models.database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date,
            'id': self._id
        }

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    @classmethod
    def from_mongo(cls, _id):
        post_data = Database.find_one(collection='posts', query={'id': _id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
