# Testing adding comments from Rachel
"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ View homepage"""
    
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """list all movies"""
    
    #get list of movie records
    movies = crud.get_movies()

    #movie['title'] -> display
    #on click -> movies/movie['movie_id']

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')  #movie_id = end of url path
def movie_details(movie_id):
    """Summary of movie details"""
    
    #get one movie record from id
    movie = crud.get_movie_by_id(movie_id)


    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def all_users():
    """list all users"""
    
    #get list of user records
    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')  
def user_details(user_id):
    """Summary of user details"""
    
    #get one movie record from id
    user = crud.get_user_by_id(user_id)


    return render_template('user_details.html', user=user)


@app.route('/users', methods=["POST"])
def create_user():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash("This account already exists")
    else:
        user = crud.create_user(email, password)
        flash("Account created, please log in")
    
    return redirect('/')


@app.route('/login', methods=["POST"])
def login_user():
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        if password == user.password:
            #add pk to session
            #flash to user that they logged in
            session['user_id'] = user.user_id
            flash("Logged in successfully")
        else:
            #password isn't correct
            #flash password is incorrect
            flash("Password is incorrect!")
            
    else:
        flash("This account doesn't exist, please create an account")
    
    return redirect('/')


@app.route('/ratings/<movie_id>', methods=["POST"])
def rate_movie(movie_id):
    #gets movie record from movie_id passed by url
    
    score = request.form.get('score')

    #checks if user is logged in, if they are
    #submits the rating
    #if not, redirects to homepage
    if session.get('user_id', 0) != 0:
        rating = crud.create_rating_from_session(score, 
                                            movie_id, 
                                            session['user_id'])
    else:
        flash("Please login before submitting ratings")

    return redirect(f'/movies/{movie_id}')
    
#app route to ratings with endpoint movie_id
#pass movie_id into func

    #get the movie record by movie_id
    #get the user record by user_id, stored in session

    #get score from post request form

    #creating rating using crud method



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
