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




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
