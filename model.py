"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

class User(db.Model):
    """Create instance of table"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True,
                        autoincrement=True,)

    email = db.Column(db.String(50), nullable=False, unique = True,)

    password = db.Column(db.String(50), nullable=False, unique = False,)

    #creates instance method to display info about the user
    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"



class Ratings(db.Model):
    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key = True,
                        autoincrement=True,)

    score = db.Column(db.Integer)

    movie_id = db.Column(db.Integer)  

    user_id = db.Column(db.Integer)

    
    def __repr__(self):
        return f'<rating ID={self.rating_id} score={self.score}>'

class Movie(db.Model):

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key = True,
                        autoincrement=True,)

    title = db.Column(db.String)

    overview = db.Column(db.Text)  

    release_date = db.Column(db.DateTime)  

    poster_path = db.Column(db.String)
    
    def __repr__(self):
        return f'<Movie ID={self.movie_id} title={self.title}>'

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
