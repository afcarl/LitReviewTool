import psycopg2
import string
import random
import pickle
import os
import json
import datetime

def connect_to_db(db_name):
    #Define our connection string
    conn_string = "host='localhost' dbname=" + db_name + "user='postgres' password='gres'"

    # print the connection string we will use to connect
    print("Connecting to database\n" + conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    return conn, cursor

def run_query(cursor, query):
    query_run = cursor.execute(query)
    query_return = cursor.fetchall()
    return query_return

def create_unique_id():
    character_set = string.ascii_letters
    character_set += string.digits
    unique_identifier = ''
    for _ in range(25):
        unique_identifier += random.choice(character_set)
    return unique_identifier

#serialize id
def serialize_output(unique_id,output):
    # pickle_name = ''
    pickle_name = unique_id + '.pkl'
    with open(pickle_name, 'wb') as f:
      pickle.dump(output, f)
        
#function to save the unique identifier for the xml as a json
def update_id_json(prop_dict):
    if not os.path.isfile(os.path.join(os.getcwd(),'unique_identifiers.json')):
        with open("unique_identifiers.json", mode='w', encoding='utf-8') as f:
            json.dump([], f)
    if os.path.isfile(os.path.join(os.getcwd(),'unique_identifiers.json')):
        with open("unique_identifiers.json") as f:
            data = json.load(f)
        data.append(prop_dict)
        with open('unique_identifiers.json', 'w') as f:
            json.dump(data, f)
