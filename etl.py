import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import datetime

def process_song_file(cur, filepath):
    '''
    Reads the  elements of the song dataset, extracts data and inserts them into the songs and artists table
    
    Accepts:
    cur: database cursor
    filepath: path to the .json file'''
    # open song file
    df = pd.read_json(filepath,lines=True)

    # insert song record
    song_data = ((df[['song_id','title','artist_id','year','duration']]).values)[0]
    song_data = list(song_data)
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = ((df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']]).values)[0]
    artist_data = list(artist_data)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    Reads the  elements of the log dataset, extracts data and inserts them into the times, users and songplays
    
    Accepts:
    cur: database cursor
    filepath: path to the .json file'''
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df.page=='NextSong']

    # convert timestamp column to datetime
    t = df
    t['ts_date']=t['ts'].map(lambda x: datetime.datetime.fromtimestamp(x/1000.0))
    
    # insert time data records
    #time_data = 
    #column_labels = 
    t['hour']=t['ts_date'].dt.hour
    t['day']=t['ts_date'].dt.day
    t['week']=t['ts_date'].dt.week
    t['month']=t['ts_date'].dt.month
    t['year']=t['ts_date'].dt.year
    t['weekday']=t['ts_date'].dt.weekday
    
    time_df = t[['ts_date','hour','day','week','month','year','weekday']]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record

        songplay_data = (row.ts_date,row.userId,row.level,songid, artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    Extract data from the directories containing each record of the activity/songs and inserts them into the tables
    
    Accepts:
    cur: database cursor
    conn: connection to the database
    filepath: path to the directory containing the records
    func: function to apply, depending on which type of records are to be processed. Can be either process_song_file or process_log_file
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()