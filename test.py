from app import app
from unittest import TestCase
from models import db

class RouteTestCase(TestCase):
  """Tests"""

  def setUp(self) -> None:
    print("setting up")
    return super().setUp()


  def tearDown(self) -> None:
    print("tearing down")
    db.session.rollback()
    return super().tearDown()

  
  def test_home(self):
    with app.test_client() as client:
      resp = client.get("/")

      self.assertEqual(resp.status_code, 302)


  def test_get_users(self):
    with app.test_client() as client:
      resp = client.get("/users")

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<a href="/users/new"><button class="btn btn-primary">Create new user</button></a>', resp.get_data(as_text=True))


  def test_new_user(self):
    with app.test_client() as client:
      resp = client.get("/users/new")

      self.assertEqual(resp.status_code, 200)
      self.assertIn('<label>First Name</label><input type="text" name="first-name">', resp.get_data(as_text=True))


  def test_post_new_user(self):
    with app.test_client() as client:
      resp = client.post("/users/new", data={"first-name": "Mr.", "last-name": "Magoo", "image-url": ""})

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, "/users")

      resp = client.get("/users")

      self.assertEqual(resp.status_code, 200)
      self.assertIn("Mr. Magoo", resp.get_data(as_text=True))

      resp = client.get("/users/1")

      self.assertEqual(resp.status_code, 200)
      self.assertIn("Mr. Magoo", resp.get_data(as_text=True))

      resp = client.get("/users/1/edit")
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<label>First Name</label><input type="text" name="first-name" value="Mr.">', resp.get_data(as_text=True))
      self.assertIn('<label>Last Name</label><input type="text" name="last-name" value="Magoo">', resp.get_data(as_text=True))

      resp = client.post("/users/1/edit", data={"first-name": "Bullwinkle", "last-name": "Moose", "image-url": ""})

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, "/users")

      resp = client.get("/users")

      self.assertEqual(resp.status_code, 200)
      self.assertIn("Bullwinkle Moose", resp.get_data(as_text=True))

      # delete
      resp = client.post("/users/1/delete")

      self.assertEqual(resp.status_code, 302)
      self.assertEqual(resp.location, "/users")


      resp = client.get("/users")

      self.assertEqual(resp.status_code, 200)
      # from home, make sure list is empty
      response_text = resp.get_data(as_text=True)
      response_text = response_text.replace("\n", "").replace(" ", "")

      self.assertIn("<ul></ul>", response_text)