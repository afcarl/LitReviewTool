import psycopg2
import string
import random
import pickle
import json
import datetime
class db_cnxn:

    def __init__(self):
        self.db_name = 'lit_review'
        self.table_names = ['DataPull_ID','DataPull_Detail','DataPull_Journal','DataPull_Author','DataPull_Text','DataPull_Title','DataPull_Keyword']

    def connect_to_db(self):
        #Define our connection string
        conn_string = "host='localhost' dbname=" + self.db_name + "user='postgres' password='gres'"

        # print the connection string we will use to connect
        print("Connecting to database\n" + conn_string)

        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        return conn, cursor

    def run_query(self,cursor, query):
        query_run = cursor.execute(query)
        query_return = cursor.fetchall()
        return query_return

class track_outputs:
    def __init__(self,output_type,input_term,input_db):

        #create identifiers
        character_set = string.ascii_letters
        character_set += string.digits
        unique_identifier = ''
        for _ in range(25):
            unique_identifier += random.choice(character_set)
        self.unique_id = str(unique_identifier)
        self.id_type = str(output_type)
        self.input_term = str(input_term)
        self.input_db = str(input_db)

    #serialize id
    def serialize_output(self,output):
        # pickle_name = ''
        pickle_name = self.unique_id + '.pkl'
        with open(pickle_name, 'wb') as f:
          pickle.dump(output, f)
        # id_dict = {output_type+'id':pickle_name}
        # return id_dict

    def search_properties(self,record_count):
        now = datetime.datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M")
        prop_dict = {'id':self.unique_id,'id_type':self.id_type
        ,'input_term':self.input_term,'input_db':self.input_db,'record_count':record_count
        ,'search_date':time_stamp}
        return prop_dict

    #function to save the unique identifier for the xml as a json
    def update_id_json(self,prop_dict):
        # prop_dict = search_properties(record_count)
        with open("unique_identifiers.json") as f:
            data = json.load(f)
        data.append(prop_dict)
        with open('unique_identifiers.json', 'w') as f:
            json.dump(data, f)


          # def import_xml(path_name):
          #     doc_list_path = path_name
          #     with open(doc_list_path, 'rb') as f:
          #         doc_list = pickle.load(f)
          #     return doc_list
