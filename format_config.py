import re
import json
import itertools
from functools import reduce
import collections
from itertools import chain
# from funcy import flatten, isa

class database:
	def __init__(self,input_term,input_db):
		self.input_term = input_term
		self.input_db = input_db

	def format_query(self):
		i_format = self.input_term.upper()
		pat = r' AND '
		formatted_terms = [r.replace(" ", "+") for r in re.split(pat,i_format)]
		formatted_query = ' AND '.join(formatted_terms)
		return formatted_query

	def format_db(self):
		formatted_db = self.input_db.lower()
		return formatted_db
