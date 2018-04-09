import re
import json
import itertools
from functools import reduce
import collections
from itertools import chain
# from funcy import flatten, isa


#Format quer term
def format_query(input_term):
    i_format = input_term.upper()
    pat = r' AND '
    formatted_terms = [r.replace(" ","+") for r in re.split(pat,i_format)]
    formatted_query = ' AND '.join(formatted_terms)
    return formatted_query

#Format database term
def format_db(input_db):
    formatted_db = input_db.lower()
    return formatted_db

#append query term to query history
def get_history(input_term):
    query_history_full = []
    config = json.load(open("config.json","r"))
    try:
        history = config['query_history']
    except:
        history = config['query'][0]
    query_history_full.append(history)
    query_history_full.append(input_term)
    query_history = list(flatten(query_history_full))
    return query_history


#make dict for configuration file
def make_config_dict(formatted_term,formatted_db,query_history):
    dicter = {}
    dicter['email'] = "s.rand525@gmail.com"
    # dicter['db_name'] = "J:/LitReviewTool/ToolandDB/LitRevDB.accdb"
    dicter['query'] = formatted_term
    dicter['query_history'] = query_history
    dicter['db'] = formatted_db
    return dicter


#create main function
def main(input_term, input_db):

    #format latest search term
    formatted_term = format_query(input_term)

    #format latest search term
    formatted_db = format_db(input_db)

    #append last query to history
    try:
      query_history = get_history(formatted_term)
    except:
      query_history = []

    #create dictionary to push to configuation file
    dicter = make_config_dict(formatted_term,formatted_db,query_history)


#     #create json with configuration info
    json.dump(dicter, open("config.json","w"))

    return dicter

# input_term = input("Please enter search term. If multiple search terms, separate by AND/OR: ")
# input_db = input("Which database to search? Please enter Pubmed or PMC. ")

#Run main
if __name__ == '__main__':
    dicter = main(input_term, input_db)
