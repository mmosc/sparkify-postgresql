# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial NOT NULL  PRIMARY KEY,
    start_time timestamp NOT NULL,
    user_id int NOT NULL,
    level varchar NOT NULL,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar,
    user_agent varchar);""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY,
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    gender varchar,
    level varchar NOT NULL);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year int,
    duration float NOT NULL);""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar NOT NULL,
    location varchar,
    latitude numeric,
    longitude numeric);""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times (
    start_time timestamp PRIMARY KEY, 
    hour int NOT NULL, 
    day int NOT NULL, 
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday varchar NOT NULL);""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time,
    user_id, 
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent) \
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""
INSERT INTO users (
    user_id,
    first_name,
    last_name,
    gender,
    level) \
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT users_pkey
DO UPDATE
    SET level = EXCLUDED.level;""")

song_table_insert = ("""
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration) \
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT songs_pkey
DO NOTHING""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id,
    name,
    location,
    latitude,
    longitude) \
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT artists_pkey
DO NOTHING""")


time_table_insert = ("""
INSERT INTO times (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday) \
VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT times_pkey 
DO NOTHING""")

# FIND SONGS
# timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent

song_select = ("""
SELECT s.song_id,a.artist_id 
    FROM (songs s 
        JOIN artists AS a ON a.artist_id= s.artist_id)
    WHERE s.title=%s AND a.name= %s AND s.duration=%s 
    GROUP BY s.song_id, a.artist_id""")


#Since the log file does not specify an ID for either the song or the artist, you'll need to get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time.

#    Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
#    Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]#[songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, time_table_create, artist_table_drop,song_table_drop,user_table_drop]

