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

@app.route('/movies/<movie_id>')
def movie_details():
    """movie details"""
    pass


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
