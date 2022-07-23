from models import User, Post, db
# from app import app

# Create all tables
db.drop_all()
db.create_all()

# sample data
henry = User(first_name='Henry', last_name='Rollins', image_url="https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280x1280/products/46523/46391/ss2158728_-_photograph_of_henry_rollins_available_in_4_sizes_framed_or_unframed_buy_now_at_starstills__54545__29662.1394484410.jpg?c=2?imbypass=on")
chuck = User(first_name='Chuck', last_name='Dukowski', image_url="https://cdn.gemtracks.com/img/artist/848.jpg")
dez = User(first_name='Dez', last_name='Cadena', image_url="https://images.equipboard.com/uploads/source/image/109891/dez-cadena-was-the-third-vocalist-and-later-rhythm-guitarist-for-hardcore-punk-band-black-flag-from-1980-to-1983-and-played-guitar-with-the-misfits-from-2001-to-2015.jpg")
greg = User(first_name='Greg', last_name='Ginn', image_url="https://lastfm.freetls.fastly.net/i/u/ar0/19a4700b78e5436e82c3eeb4ca0827a9.jpg")
robo = User(first_name='Robo', last_name='ROBO', image_url="https://64.media.tumblr.com/58e9139333949cd4fe2cdb9ad510e8ea/tumblr_ml5cdz1baz1s474z1o1_500.jpg")

db.session.add(henry)
db.session.add(chuck)
db.session.add(dez)
db.session.add(greg)
db.session.add(robo)

modern_man = Post(title="Modern Man", content="He's too straight and you can't wait a modern...man", author_id=2)

db.session.add(modern_man)

db.session.commit()


