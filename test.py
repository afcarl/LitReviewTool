import re
# import json
# import itertools
# from functools import reduce
# import collections
# from itertools import chain
# from funcy import flatten, isa

class database:
	def __init__(self,name):
        	self.name = name

	def format_query(self,input_term):
		i_format = input_term.upper()
		pat = r' AND '
		formatted_terms = [r.replace(" ", "+") for r in re.split(pat,i_format)]
		formatted_query = ' AND '.join(formatted_terms)
		return formatted_query

	def format_dt(self,input_db):
		formatted_db = input_db.lower()
		return formatted_db

