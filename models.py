"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  """Connect to database"""
  
  db.app = app
  db.init_app(app)


class User(db.Model):
  """A User"""

  __tablename__ = "users"

  def __repr__(self):
    return f"Id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, image_url: {self.image_url}"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=True)