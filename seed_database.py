"""Automate dropping database, creating database and creating all tables"""

import os, json, model, crud, server 
from random import choice, randint
from datetime import datetime


#drop database and create new empty db
os.system('dropdb ratings')
os.system('createdb ratings')

#connect our app to db created
model.connect_to_db(server.app)
#use our models and create all the tables
#in the database
model.db.create_all()

#load data from data/movies.json and save it to a variable movie_data
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
format = '%Y-%m-%d'

#creating new entries in movies table
#goes through each dictionary item from json file
for movie in movie_data:
    #passes arguments to create movie from json file by dict key
    #title, overview, release_date formated as datetime obj, poster_path
    db_movie = crud.create_movie(movie['title'], 
                                 movie['overview'], 
                                 datetime.strptime(movie['release_date'], format), 
                                 movie['poster_path'])

    #add each db movie into a list
    movies_in_db.append(db_movie)

#creating fake users for the user table
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    #create user entry, return the user in var user
    user = crud.create_user(email, password)

    for i in range(10):
        #create rating from random score 1-5
        #pass user created earlier to rating
        #choose and pass random movie from list
        crud.create_rating(randint(1,5), 
                           user, 
                           choice(movies_in_db))