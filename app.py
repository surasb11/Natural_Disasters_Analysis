import os
import json
import pymongo
from flask import Flask
from flask import request

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.Natural_Disasters
collection = db.temp_change_1990

@app.route("/", methods=['POST'])
def insert_document():
	req_data = request.get_json()
	collection.insert_one(req_data).inserted_id
	return ('', 204)

@app.route('/')
def get():
	documents = collection.find()
	response = []
	for document in documents:
		document['_id'] = str(document['_id'])
		response.append(document)
	return json.dumps(response)
