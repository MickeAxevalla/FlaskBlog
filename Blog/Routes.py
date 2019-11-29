from flask import render_template, redirect, url_for, request
from Blog import Blog
from Blog.Models import User, Post, db


@Blog.route('/')
def index():
    posts = Post.query.all()
    posts.reverse()
    return render_template("home.html", posts=posts)


@Blog.route('/about')
def about():
    return render_template("about.html")


@Blog.route('/interests')
def interests():
    return render_template("interests.html")


@Blog.route('/contact')
def contact():
    return render_template("contact.html")


@Blog.route('/awesome/<name>')
def awesome(name):
    return render_template("awesome.html", name=name)


@Blog.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == "POST":
        user = User.query.filter_by(id=request.form.get('user')).first()
        title = request.form.get('title')
        content = request.form.get('content')
        post = Post(title=title, content=content, user_id=user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        users = User.query.all()
        return render_template("newpost.html", users=users)
