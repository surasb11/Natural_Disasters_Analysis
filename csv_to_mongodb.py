import pandas as pd
import pymongo
import json
import os

def import_csvfile(filepath):
	
	mng_client = pymongo.MongoClient('localhost', 27017)
	mng_db = mng_client['Natural_Disasters'] # Replace mongo db name
	
	# Replace mongo db collection name
	collection_name = 'temp_change_1960'
	
	db_cm = mng_db['temp_change_1960']
	
	cdir = os.path.dirname(__file__)
	file_res = os.path.join(cdir, filepath)
	data = pd.read_csv(file_res)
	data_json = json.loads(data.to_json(orient='records'))
	
	db_cm.remove()
	db_cm.insert(data_json)

def imp_csvfile(filepath1):
	mng_client1 = pymongo.MongoClient('localhost', 27017)
	mng_db1 = mng_client1['Natural_Disasters']
	collection_name1 = 'temp_change_1990'
	db_cm1 = mng_db1['temp_change_1990']
	
	cdir1 = os.path.dirname(__file__)
	file_res1 = os.path.join(cdir1, filepath1)
	data1 = pd.read_csv(file_res1)
	data_json1 = json.loads(data1.to_json(orient='records'))
	
	db_cm1.remove()
	db_cm1.insert(data_json1)

def imp_csvfil(filepath2):
	mng_client2 = pymongo.MongoClient('localhost', 27017)
	mng_db2 = mng_client2['Natural_Disasters']
	collection_name2 = 'earthquakes'
	db_cm2 = mng_db2['earthquakes']
	
	cdir2 = os.path.dirname(__file__)
	file_res2 = os.path.join(cdir2, filepath2)
	data2 = pd.read_csv(file_res2)
	data_json2 = json.loads(data2.to_json(orient='records'))
	
	db_cm2.remove()
	db_cm2.insert(data_json2)

def imp_file(filepath3):
	mng_client3 = pymongo.MongoClient('localhost', 27017)
	mng_db3 = mng_client3['Natural_Disasters']
	collection_name3 = 'tsunamis'
	db_cm3 = mng_db3['tsunamis']
	
	cdir3 = os.path.dirname(__file__)
	file_res3 = os.path.join(cdir3, filepath3)
	data3 = pd.read_csv(file_res3)
	data_json3 = json.loads(data3.to_json(orient='records'))
	
	db_cm3.remove()
	db_cm3.insert(data_json3)
	
def imp_files(filepath4):
	mng_client4 = pymongo.MongoClient('localhost', 27017)
	mng_db4 = mng_client4['Natural_Disasters']
	collection_name4 = 'volcanoes'
	db_cm4 = mng_db4['volcanoes']
	
	cdir4 = os.path.dirname(__file__)
	file_res4 = os.path.join(cdir4, filepath4)
	data4 = pd.read_csv(file_res4)
	data_json4 = json.loads(data4.to_json(orient='records'))
	
	db_cm4.remove()
	db_cm4.insert(data_json4)
	
def impr_files(filepath5):
	mng_client5 = pymongo.MongoClient('localhost', 27017)
	mng_db5 = mng_client5['Natural_Disasters']
	collection_name5 = 'temp_change_2000'
	db_cm5 = mng_db5['temp_change_2000']
	
	cdir5 = os.path.dirname(__file__)
	file_res5 = os.path.join(cdir5, filepath5)
	data5 = pd.read_csv(file_res5)
	data_json5 = json.loads(data5.to_json(orient='records'))
	
	db_cm5.remove()
	db_cm5.insert(data_json5)



if __name__ == "__main__":
	
	# pass csv file path
	filepath = 'csv-files/output_data/avr_temp_from_1960_df.csv'
	filepath1 = 'csv-files/output_data/avr_temp_from_1990_df.csv'
	filepath2 = 'csv-files/output_data/earthquakes_df.csv'
	filepath3 = 'csv-files/output_data/tsunami_df.csv'
	filepath4 = 'csv-files/output_data/volcanoes_df.csv'
	filepath5 = 'csv-files/output_data/avr_temp_from_2000_df.csv'

	import_csvfile(filepath)
	imp_csvfile(filepath1)
	imp_csvfil(filepath2)
	imp_file(filepath3)
	imp_files(filepath4)
	impr_files(filepath5)

