"""Models for Blogly."""
# from turtle import title
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

def connect_db(app):
  """Connect to database"""
  
  db.app = app
  db.init_app(app)


class User(db.Model):
  """A User"""

  __tablename__ = "users"

  def __repr__(self):
    return f"Id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, image_url: {self.image_url}, posts: {self.posts}"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=True)

  posts = db.relationship('Post', cascade="all, delete, delete-orphan")


class Post(db.Model):
  """A Post made by a User"""

  __tablename__ = "posts"

  def __repr__(self):
    content_str = self.content
    if len(self.content) > 30:
      content_str = f"{self.content}..."

    return f"Id: {self.id} title: {self.title} created_at: {self.created_at}  content: {content_str}"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String, nullable=False)
  content = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now())
  author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

  author = db.relationship("User")
  # author = db.relationship("User", backref=db.backref('posts', cascade="all,delete"))