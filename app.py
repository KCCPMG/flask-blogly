"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.drop_all()
db.create_all()

# seed sample documents
from seed import *



@app.route('/', methods=['GET'])
def get_home():
  """
  Redirect to list of users. (We'll fix this in a later step).
  """
  return redirect('/users')



@app.route('/users', methods=['GET'])
def get_users():
  """
  Show all users, make links to view the detail page for the user, have a link for the add-user form
  """

  users = User.query.filter()
  if users == None:
    users = []

  return render_template("users.html", users=users)



@app.route('/users/new', methods=['GET'])
def get_new_user():
  """
  Show an add form for users
  """

  return render_template("new_user.html")



@app.route('/users/new', methods=['POST'])
def post_new_user():
  """
  Process the add form, adding a new user and going back to /users
  """
  first_name = request.form["first-name"]
  last_name = request.form["last-name"]
  image_url = request.form["image-url"]

  print(first_name, last_name, image_url)

  new_user = User(first_name = first_name, last_name=last_name, image_url=image_url)

  db.session.add(new_user)
  db.session.commit()

  return redirect("/users")



@app.route('/users/<int:userid>', methods=['GET'])
def get_user_by_userid(userid):
  """
  Show information about the given user, have a button to get to their edit page, and a button to delete the user
  """

  user = User.query.get(userid)

  return render_template('display_user.html', user=user)



@app.route('/users/<int:userid>/edit', methods=['GET'])
def get_user_edit_form(userid):
  """
  Show the edit page for a user, have a cancel button that returns to the detail page for a user, and a save button that updates the user.
  """
  user = User.query.get(userid)

  return render_template("edit_user.html", user=user)


@app.route('/users/<int:userid>/edit', methods=['POST'])
def post_user_edit_form(userid):
  """
  Process the edit form, returning the user to the /users page.
  """
  user = User.query.get(userid)

  user.first_name = request.form["first-name"]
  user.last_name = request.form["last-name"]
  user.image_url = request.form["image-url"]

  db.session.commit()

  return redirect("/users")



@app.route('/users/<userid>/delete', methods=['POST'])
def delete_user(userid):
  """Delete the user"""
  user = User.query.get(userid)
  db.session.delete(user)


  db.session.commit()

  return redirect("/users")


@app.route('/users/<int:userid>/posts/new', methods=['GET'])
def get_blog_post_form(userid):
  """Show form to add a post for that user."""

  return render_template('new_blog_form.html', userid=userid)


@app.route('/users/<int:userid>/posts/new', methods=['POST'])
def take_blog_post_form(userid):
  """Take blog post"""
  post = Post(title=request.form['title'], content=request.form['content'],  author_id=userid)

  db.session.add(post)
  db.session.commit()

  return redirect(f"/users/{userid}")


@app.route('/posts/<int:postid>', methods=['GET'])
def get_post(postid):
  """Show blog post"""
  post = Post.query.get(postid)

  return render_template('display_post.html', post=post)


@app.route('/posts/<int:postid>/edit', methods=['GET'])
def get_edit_post(postid):
  """get edit post form"""
  post=Post.query.get(postid)
  return render_template('edit_blog_form.html', post=post)


@app.route('/posts/<int:postid>/edit', methods=['POST'])
def post_edit_post(postid):
  """accept post for post edit"""
  post=Post.query.get(postid)
  
  post.title = request.form['title']
  post.content = request.form['content']

  db.session.commit()
  return redirect(f"/users/{post.author_id}")


@app.route('/posts/<int:postid>/delete', methods=['POST'])
def delete_post(postid):
  """Delete a post"""
  post = Post.query.get(postid)
  user_id = post.author_id
  db.session.delete(post)
  db.session.commit()
  
  return redirect(f"/users/{user_id}")