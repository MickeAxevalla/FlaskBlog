from flask import render_template, redirect, url_for, request, flash
from Blog import Blog, bcrypt
from Blog.Models import User, Post, db
from Blog.Forms import LoginForm
from flask_login import login_user, current_user, logout_user

@Blog.route('/')
def home():
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


@Blog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
        else:
            flash("Felaktig inloggning!", "text-error")

    return render_template('login.html', form=form)

@Blog.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('login'))

