

# Created by Sachin Dev on 27/05/18

from flask import Flask, render_template, request, session

from database.database import Database
from models.blog import Blog
from models.user import User

app = Flask(__name__)
app.secret_key='Sachin'
app.debug = True
app.env='development'


@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email=request.form['email']
    password=request.form['password']

    if User.login_valid(email,password):
        User.login(email)
    else:
        session['email']=None
    return render_template("profile.html", email=session['email'])


@app.route('/auth/register',methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email,password)
    return render_template("profile.html", email=session['email'])


@app.route('/blog/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs, email=user.email)


@app.route('/posts<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()

    render_template('/posts.html', posts=posts , blog_name = blog.title)


if __name__ == '__main__':
    app.run(port=4998)
