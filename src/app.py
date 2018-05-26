# Created by Sachin Dev on 26/05/18

from models.database import Database
from models.post import Post

Database.initialize()

# post = Post(
#     blog_id='1234',
#     title='Another Great Post',
#     content='This is Sample Content',
#     author='Sachin')
#
# post.save_to_mongo()

posts = Post.from_blog('1234')

for post in posts:
    print(post)
    