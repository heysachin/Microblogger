# Created by Sachin Dev on 26/05/18

from models.database import Database
from models.post import Post
from models.blog import Blog


Database.initialize()

# post = Post(
#     blog_id='1234',
#     title='Another Great Post',
#     content='This is Sample Content',
#     author='Sachin')
#
# post.save_to_mongo()
# posts = Post.from_blog('1234')
#
# for post in posts:
#     print(post)

blog = Blog(author="Sachin",
            title="New Title",
            description="Sample Description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())