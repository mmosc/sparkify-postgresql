# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplay_table"
user_table_drop = "DROP table IF EXISTS user_table"
song_table_drop = "DROP table IF EXISTS song_table"
artist_table_drop = "DROP table IF EXISTS artist_table"
time_table_drop = "DROP table IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table (songplay_id int, start_time numeric, user_id int, level varchar, song_id int, artist_id int, session_id int, location varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_table (user_id int, first_name varchar, last_name varchar, gender varchar, level int);""")


song_table_create = ("""CREATE TABLE IF NOT EXISTS song_table (song_id int, title varchar, artist_id int, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist_table (artist_id int, name varchar, location varchar, latitude numeric, longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_table (start_time numeric, hour int, day int, week int, month int, year int, weekday varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay_table (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent);""")

user_table_insert = ("""INSERT INTO user_table (user_id, first_name, last_name, gender, level);""")

song_table_insert = ("""INSERT INTO song_table (song_id, title, artist_id, year, duration);""")

artist_table_insert = ("""INSERT INTO artist_table (artist_id, name, location, latitude, longitude);""")


time_table_insert = ("""INSERT INTO time_table (start_time, hour, day, week, month, year, weekday);""")

# FIND SONGS

song_select = ("""SELECT * FROM song_table""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]#[songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, time_table_create, artist_table_drop,song_table_drop,user_table_drop]

