# search.py
class search(object):

    def __init__(self):
        self.input_term = 'public health'
        self.input_db = 'pubmed'
        # self.search_param = 5

    def pub_count(self,search_param):
        if self.input_db:
#             search_param = 5
            record_count = search_param+5
        else:
            record_count = 5
        return record_count

    def create_param_dict(cls):
        record_count = self.pub_count(self,search_param)
#         LOST HERE!
        param_dict = {'term':input_term,'db':input_db,'record_count':record_count}
        return param_dict
