from Bio import Entrez
import pandas as pd
from pandas import DataFrame
import itertools
import codecs
import io
import sys
import encodings
import time
import os
import math
from itertools import chain
from IPython.display import HTML
from datetime import date
import datetime
import pickle
import types
import lxml.html
from operator import itemgetter
from itertools import groupby
import json
import random
import string
import helper
import new_helper
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class ncbi_search:
    def __init__(self,input_term,input_db,email_id):
        self.input_term = input_term
        self.input_db = input_db
        self.email_id = email_id
        # self.tracker = helper.track_outputs

    #Find # of records within search parameters
    def pub_count(self):
        Entrez.email = self.email_id
        counthandle = Entrez.egquery(term = self.input_term)
        record = Entrez.read(counthandle)
        for row in record["eGQueryResult"]:
            if row['DbName'] == self.input_db:
                record_count = row['Count']
        counthandle.close()
        return record_count

    #function for retrieving and storing ids
    def pub_search(self, record_count, sort = 'relevance', chunksize = 500, sleeptime = 5):
        submitinterv = math.ceil(int(record_count)/chunksize)
        id_list = []
        retstartc = 0
        if record_count < chunksize:
            ret_max = record_count
        elif record_count >= chunksize:
            ret_max = chunksize
        for i in range(submitinterv):
            handle = Entrez.esearch(db=self.input_db,
                                sort='relevance',
                                retstart= retstartc,
                                retmax=ret_max,
                                retmode='xml',
                                term=self.input_term)
            idresults = Entrez.read(handle)
            id_list += idresults['IdList']
            time.sleep(sleeptime)
            retstartc += chunksize
            handle.close()
        return id_list

        def search_properties(self):
            now = datetime.datetime.now()
            time_stamp = now.strftime("%Y-%m-%d %H:%M")
            record_count = self.pub_count()
            prop_dict = {'id':self.unique_id,'id_type':'search'
            ,'input_term':self.input_term,'input_db':self.input_db,'record_count':record_count
            ,'search_date':time_stamp}
            return prop_dict




            #serialize id
            def serialize_output(self,output):
                # pickle_name = ''
                pickle_name = self.unique_id + '.pkl'
                with open(pickle_name, 'wb') as f:
                  pickle.dump(output, f)
                # id_dict = {output_type+'id':pickle_name}
                # return id_dict


            #function to save the unique identifier for the xml as a json
            def update_id_json(self,prop_dict):
                # prop_dict = search_properties(record_count)
                with open("unique_identifiers.json") as f:
                    data = json.load(f)
                data.append(prop_dict)
                with open('unique_identifiers.json', 'w') as f:
                    json.dump(data, f)




#Filter record ids based on existence in database
# def filter_ids(id_list,db_name,db):
#     conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % db_name
#     cnxn = pyodbc.connect(conn_str)
#     cur = cnxn.cursor()
#     aid_list = cur.execute("""select distinct b.AssociatedID from DataPull_ID as a inner join DataPull_Detail as b on a.PullID = b.PullID where a.PullSource = ?""",db).fetchall()
#     existing_ids = {associatedid[0] for associatedid in aid_list}
#     id_list_fetch = [fetch_id for fetch_id in id_list if fetch_id not in existing_ids]
#     return id_list_fetch


#function for fetching xmls for given ids
# def pub_fetch(db, id_list_fetch):
#     ids = ','.join(id_list_fetch)
#     submitinterv = math.ceil(len(id_list_fetch)/10000)
#     sleeptime = 5
#     restartc = 0
#     doc_list = []
#
#     for i in range(submitinterv):
#         fetchHandle = Entrez.efetch(db=db,
#                                   retmode='xml',
#                                   id=ids,
#                                   retstart = restartc,
#                                   retmax=10000)
#         fetchRead = io.TextIOWrapper(fetchHandle.detach(), encoding='utf-8')
#         doc = fetchRead.read()
#         doc_list.append(doc)
#         time.sleep(sleeptime)
#         restartc += 10000
#     doc_full = doc_list
#
#     return doc_full


#
# #function to save the unique identifier for the xml as a json
# def to_json(unique_identifier_fetch):
#     json.dump(unique_identifier_fetch,open("unique_identifier_fetch.json","w"))
#
#
#
# #main function to run all functions and assign unique_identifier to the run
# def main(term,db,db_name,email_id):
#
#     character_set = string.ascii_letters
#     character_set += string.digits
#
#     unique_identifier_fetch = ''
#
#     for _ in range(25):
#         unique_identifier_fetch += random.choice(character_set)
#
#     #Retrieve number of records
#     record_count = pub_count(term,db,email_id)
#
#     #Retrieve record ids
#     id_list = pub_search(term,db,record_count)
#
#     #Filter record ids
#     id_list_fetch = filter_ids(id_list,db_name,db)
#
#     #Fetch xmls for each record id
#     doc_full = pub_fetch(db,id_list_fetch)
#
#     #serialize xml documents (serialize)
#     serialize_xml(unique_identifier_fetch,doc_full)
#
#     return unique_identifier_fetch,id_list_fetch
#
#
# def ex_main(term,db,db_name,email_id):
#   unique_identifier_fetch_list = []
#   run_main = main(term,db,db_name,email_id)
#   unique_identifier_fetch_list.append(run_main[0])
#   unique_identifier_fetch_list.append(len(run_main[1]))
#   to_json(unique_identifier_fetch_list)
#   unique_identifier_fetch = run_main[0]
#   return unique_identifier_fetch
#
#
# if __name__ == '__main__':
#     unique_identifier_fetch = ex_main(term,db,db_name,email_id)
