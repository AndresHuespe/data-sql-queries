# pylint: disable=C0103, missing-docstring
import sqlite3
path = "movies.sqlite"
conn = sqlite3.connect(path)


def detailed_movies(db):
    #return the list of movies with their genres and director name
    db = conn.cursor()
    db.execute("""SELECT m.title, m.genres, d.name
FROM movies m
JOIN directors d ON
m.director_id = d.id """)
    rows = db.fetchall()
    return rows


def late_released_movies(db):
    #return the list of all movies released after their director death'''
    db = conn.cursor()
    db.execute("""SELECT m.title, m.start_year, d.death_year
FROM movies m
JOIN directors d
ON d.id = m.director_id
WHERE m.start_year  > d.death_year
ORDER BY m.title""")
    rows = db.fetchall()
    #movies = []
    #for i in range(len(rows)):
    #    movies.append(rows[i][0])
    #return movies
    return [director[0] for director in rows]

def stats_on(db, genre_name):
    db = conn.cursor()
    #return a dict of stats for a given genre'''
    db.execute(f"""SELECT m.genres, COUNT(m.id), AVG(m.minutes)
FROM movies m
WHERE genres = '{genre_name}'
GROUP BY genres""")
    stats = {}
    rows = db.fetchall()
    stats['genre'] = rows[0][0]
    stats['number_of_movies'] = rows[0][1]
    stats['avg_length'] = round(rows[0][2],2)
    return stats


def top_five_directors_for(db, genre_name):
    #return the top 5 of the directors with the most movies for a given genre'''
    db = conn.cursor()
    db.execute(f"""SELECT  d.name, COUNT(m.title) number
FROM movies m
JOIN directors d ON
d.id = m.director_id
WHERE genres = '{genre_name}'
GROUP BY director_id
ORDER BY number DESC, name ASC
LIMIT 5""")
    rows = db.fetchall()
    return rows


def movie_duration_buckets(db):
    #return the movie counts grouped by bucket of 30 min duration'''
    db = conn.cursor()
    db.execute("""SELECT
CASE
    WHEN minutes < 30
        THEN 30
    WHEN minutes >= 30 AND minutes < 60
        THEN 60
    WHEN minutes >= 60 AND minutes <90
        THEN 90
    WHEN minutes >=90 AND minutes <120
        THEN 120
    WHEN minutes >= 120 AND minutes <150
        THEN 150
    WHEN minutes >= 150 AND minutes <180
        THEN 180
    WHEN minutes >= 180 AND minutes <210
        THEN 210
    WHEN minutes >= 210 AND minutes < 240
        THEN 240
    WHEN minutes >= 240 AND minutes < 270
        THEN 270
    WHEN minutes >= 270 AND minutes < 300
        THEN 300
    WHEN minutes >= 300 AND minutes < 330
        THEN 330
    WHEN minutes >= 330 AND minutes < 360
        THEN 360
    WHEN minutes >= 360 AND minutes < 390
        THEN 390
    WHEN minutes >= 390 AND minutes < 420
        THEN 420
    WHEN minutes >= 420 AND minutes < 450
        THEN 450
    WHEN minutes >= 450 AND minutes < 480
        THEN 480
    WHEN minutes >= 480 AND minutes < 510
        THEN 510
    WHEN minutes >= 510 AND minutes < 540
        THEN 540
    WHEN minutes >= 540 AND minutes < 570
        THEN 570
    WHEN minutes >= 570 AND minutes < 600
        THEN 600
    WHEN minutes >= 600 AND minutes < 630
        THEN 630
    WHEN minutes >= 630 AND minutes < 660
        THEN 660
    WHEN minutes >= 660 AND minutes < 690
        THEN 690
    WHEN minutes >= 870 AND minutes < 900
        THEN 900
    WHEN minutes >= 990 AND minutes < 1020
        THEN 1020
    END AS outcome,
    COUNT(title) AS count
FROM movies
GROUP BY outcome
ORDER BY outcome ASC """)
    rows = db.fetchall()
    return rows[1::]


def top_five_youngest_newly_directors(db):
    #return the top 5 youngest directors when they direct their first movie'''
    db = conn.cursor()
    db.execute("""
                SELECT d.name,
m.start_year  - d.birth_year AS age
FROM directors d
JOIN movies m ON
d.id  = m.director_id
WHERE d.birth_year NOTNULL
GROUP BY d.name
ORDER BY age
LIMIT 5""")
    rows = db.fetchall()
    return rows
