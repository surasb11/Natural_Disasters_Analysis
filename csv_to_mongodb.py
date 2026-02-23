import pandas as pd
import pymongo
import json
import os

# Global database connection to be reused
_db = None

def get_database():
    global _db
    if _db is None:
        mng_client = pymongo.MongoClient('localhost', 27017)
        _db = mng_client['Natural_Disasters']
    return _db

def _import_to_collection(filepath, collection_name):
    """
    Helper function to import a CSV file into a MongoDB collection.
    Reuses the global database connection.
    """
    db = get_database()
    db_cm = db[collection_name]

    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))

    db_cm.delete_many({})
    db_cm.insert_many(data_json)

def import_csvfile(filepath):
    _import_to_collection(filepath, 'temp_change_1960')

def imp_csvfile(filepath1):
    _import_to_collection(filepath1, 'temp_change_1990')

def imp_csvfil(filepath2):
    _import_to_collection(filepath2, 'earthquakes')

def imp_file(filepath3):
    _import_to_collection(filepath3, 'tsunamis')

def imp_files(filepath4):
    _import_to_collection(filepath4, 'volcanoes')

def impr_files(filepath5):
    _import_to_collection(filepath5, 'temp_change_2000')

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
