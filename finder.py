import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

# Setting up env variables
connection_string = os.environ.get('CONNECTION_STRING')
database = os.environ.get('DB_NAME')
collection = os.environ.get('DB_COLLECTION')

# Connect to mongodb
client = MongoClient(connection_string)

db = client[database]
col = db[collection]

agg_result= col.aggregate([
  {
    '$search': {
      'index': 'default',
      'text': {
        'query': 'brook',
        'path': {
          'wildcard': '*'
        }
      }
    }
  },
  {
       '$project':{
        'name':1,
        'address':1,
        'cuisine':1,
        'restaurant_id':1

    }
  }
])
for i in agg_result:
    print(i)

