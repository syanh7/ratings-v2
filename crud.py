from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    user = User(email=email, password=password)
    #test_user = User(email='test@test.test', password='test')

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    movie = Movie(title=title, 
                overview=overview,
                release_date = release_date,
                poster_path = poster_path
                )
    
    db.session.add(movie)
    db.session.commit()

    return movie


def create_rating(score, user, movie):
    rating = Rating(score=score,
                    user=user,
                    movie=movie)
    
    db.session.add(rating)
    db.session.commit()
    
    return rating

def get_movies():

    #returns a list of movie records
    return Movie.query.all()


def get_movie_by_id(movie_id):
    #Query Movie database to grab movie record by ID
    movie = Movie.query.get(movie_id)

    return movie


def get_users():

    #returns a list of user records
    return User.query.all()


def get_user_by_id(user_id):
    #Query User database to grab movie record by PK
    user = User.query.get(user_id)

    return user

def get_user_by_email(email):
    """Return a user by email"""

    user = User.query.filter(User.email == email).first()

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
