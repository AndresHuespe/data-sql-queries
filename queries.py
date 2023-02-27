# pylint: disable=C0103, missing-docstring
import sqlite3
path = "movies.sqlite"
conn = sqlite3.connect(path)
db = conn.cursor()

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    db.execute("""SELECT m.title, m.genres, d.name
FROM movies m 
JOIN directors d ON
m.director_id = d.id """)
    rows = db.fetchall()
    return rows


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    db.execute("""SELECT m.title, m.start_year, d.death_year
FROM movies m
JOIN directors d 
ON d.id = m.director_id 
WHERE m.start_year  > d.death_year
ORDER BY m.title""")
    rows = db.fetchall()
    movies = []
    for i,j in enumerate(rows):
        movies.append(rows[i][0])
    return movies


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    pass  # YOUR CODE HERE


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    pass  # YOUR CODE HERE


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    pass  # YOUR CODE HERE
