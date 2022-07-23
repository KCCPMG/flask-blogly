from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# sample data
henry = User(first_name='Henry', last_name='Rollins')
chuck = User(first_name='Chuck', last_name='Dukowski')
dez = User(first_name='Dez', last_name='Cadena')
greg = User(first_name='Greg', last_name='Ginn')
robo = User(first_name='Robo', last_name='ROBO')

db.session.add(henry)
db.session.add(chuck)
db.session.add(dez)
db.session.add(greg)
db.session.add(robo)



db.session.commit()


