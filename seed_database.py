"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import Crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

    movies_in_db = []
    
    for movie in movie_data:
        movie_title = movie['title']
        movie_overview = movie['overview']
        movie_poster_path = movie['poster_path']
        
        movie_release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

        db_movie = Crud.create_movie(movie_title, movie_overview,movie_release_date,movie_poster_path) 
        
        movies_in_db.append(db_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = Crud.create_user(email=email, password=password)

    for n in range(10):
        random_movie=choice(movies_in_db)
        score=randint(1,5)
            
        Crud.create_rating(user, random_movie, score)

