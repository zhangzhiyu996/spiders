from pymongo import MongoClient
import json
import pprint
#client = MongoClient()
client = MongoClient('mongodb://localhost:8005/')
db = client['RAW_DATA']
osv = db['osv']
with open("osvdata-all0.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        content = json.loads(i)
        #pprint.pprint(osv.find_one({'id':content['id']}))
        post_id = osv.insert_one(dict(content)).inserted_id
