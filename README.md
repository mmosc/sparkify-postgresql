# Project Overview

PostgreSQL project in the Data Engineering Udacity Nanodegree.  

## Introduction

At Sparkify, our app allows the user to stream music. We want to analyze the data on songs and user activity on their new music streaming app. In particular, we want to understand what songs users are listening to. This repository allows to create a Postgres database with tables designed to optimize queries on song play analyses.

## Dataset
Data reside in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. 

### Song Dataset
Sparkify song dataset (which truely is a subset of the real data from the [Million Song Dataset](http://millionsongdataset.com/)) consists of files in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.
```python
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```
And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.
```python
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```
### Log Dataset
The user activity dataset consists of log files from our music streaming app in JSON format generated by the Sparkify app (Truely: [event simulator](https://github.com/Interana/eventsim)) based on the songs in the dataset above. 

These log files are partitioned by year and month. For example, here are filepaths to two files in this dataset.
```python
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.
![alt text](./log-data.png)

## Files 
In addition to the data files, there are six files:
1. ```test.ipynb``` displays the first few rows of each table to check the database.
2. ```create_tables.py``` drops and creates the tables. It is used to reset the tables before running the ETL scripts.
3. ```etl.ipynb``` reads and processes a single file from ```song_data``` and ```log_data``` and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. ```etl.py``` reads and processes files from ```song_data``` and ```log_data``` and loads them into the tables. It can be filled out based on the ETL notebook.
5. ```sql_queries.py``` contains all the sql queries, and is imported into the last three files above.
6. ```README.md``` this readme.


## Database Schema
The Database schema contains the following tables
#### Fact Table 
1. **songplays** - records in log data associated with song plays i.e. records with page ```NextSong```
* *songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*
#### Dimenson Tables
2. **users** - users in the app 
* *user_id, first_name, last_name, gender, level*
3. **songs** - songs in music database
* *song_id, title, artist_id, year, duration
4. **artists** - artists in music database
* *artist_id, name, location, latitude, longitude*
5. **time** - timestamps of records in **songplays** broken down into specific units
* *start_time, hour, day, week, month, year, weekday
It is organised as a start schema. The Entity Relation Diagram is as follows
![alt text](./sparkify_schema.png)

The diagram is generated using (Visual Paradigm)[https://online.visual-paradigm.com/diagrams/features/erd-tool/]. Primary keys are in bold font. I did not manage to do-undo italics to distinguish numerical entries...


## ETL Pipeline
 and writing an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


## Usage
### Fill in the DB
1. Run ```create_tables.py``` to create the ```sparkifydb```. This is the database to which the other files connect.
2. Run ```etl.py``` process the data and insert them into the database.
### Queries
Example queries for each of the tables can be found in the ```test.ipynb``` file. As additional example, here's a query for what songs  