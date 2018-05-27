

# Created by Sachin Dev on 27/05/18
from models.blog import Blog
from models.database import Database


class Menu(object):
    def __init__(self):
        self.user = input("Enter Your Author Name : ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome Back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter Blog Title : ")
        description = input("Enter Blog Description : ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        read_or_write = input("Do You Want to read (R) or Write (W) Blogs ? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
            pass
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for Blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'],blog['title'],blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID Of the Blog You'd Like to Read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date : {}, Title: {}\n\n{}".format(post['created_date'],post['title'],post['content']))