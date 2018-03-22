import NCBIPush
import json

uid_path = "J:/LitReviewTool/ToolandDB/unique_identifier_parse.json"
uid_load = json.load(open(uid_path,"r"))

json_path = "J:/LitReviewTool/ToolandDB/config.json"
config = json.load(open(json_path,"r"))
email_id = config['email']
term = config['query']
db_name = config['db_name']
db = config['db']


parsed_path_name = uid_load+ '.pkl'

NCBIPush.ex_main_push(parsed_path_name,term,db_name,db)

