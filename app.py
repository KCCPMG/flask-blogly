"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.drop_all()
db.create_all()

# sample populating
# henry = User(first_name='Henry', last_name='Rollins', image_url="https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280x1280/products/46523/46391/ss2158728_-_photograph_of_henry_rollins_available_in_4_sizes_framed_or_unframed_buy_now_at_starstills__54545__29662.1394484410.jpg?c=2?imbypass=on")
# chuck = User(first_name='Chuck', last_name='Dukowski', image_url="https://cdn.gemtracks.com/img/artist/848.jpg")
# dez = User(first_name='Dez', last_name='Cadena', image_url="https://images.equipboard.com/uploads/source/image/109891/dez-cadena-was-the-third-vocalist-and-later-rhythm-guitarist-for-hardcore-punk-band-black-flag-from-1980-to-1983-and-played-guitar-with-the-misfits-from-2001-to-2015.jpg")
# greg = User(first_name='Greg', last_name='Ginn', image_url="https://lastfm.freetls.fastly.net/i/u/ar0/19a4700b78e5436e82c3eeb4ca0827a9.jpg")
# robo = User(first_name='Robo', last_name='ROBO', image_url="https://64.media.tumblr.com/58e9139333949cd4fe2cdb9ad510e8ea/tumblr_ml5cdz1baz1s474z1o1_500.jpg")

# db.session.add(henry)
# db.session.add(chuck)
# db.session.add(dez)
# db.session.add(greg)
# db.session.add(robo)

# db.session.commit()
# end sample populating


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
  User.query.filter_by(id=userid).delete()

  db.session.commit()

  return redirect("/users")