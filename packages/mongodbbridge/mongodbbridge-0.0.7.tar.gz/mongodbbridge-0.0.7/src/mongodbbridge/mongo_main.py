import pymongo
import pandas as pd
from pymongo.mongo_client import MongoClient
import json

class MongoOperation:
    __collection = None 
    __database = None
    
    def __init__(self, client_url: str, database_name: str, collection_name: str=None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = None
        self.database = None
        self.collection = None
       
    def create_mongo_client(self):
        if self.client is None:
            self.client = MongoClient(self.client_url)
        return self.client
    
    def create_database(self):
        if self.database is None:
            client = self.create_mongo_client()
            self.database = client[self.database_name]
        return self.database 
    
    def create_collection(self):
        if self.collection is None:
            database = self.create_database()
            self.collection = database[self.collection_name]
            MongoOperation.__collection = self.collection
        
        if MongoOperation.__collection != self.collection:
            database = self.create_database()
            self.collection = database[self.collection_name]
            MongoOperation.__collection = self.collection
            
        return self.collection
    
    def insert_record(self, record: dict, collection_name: str) -> None:
        if not isinstance(record, dict):
            raise TypeError("Record must be a dictionary")
        
        collection = self.create_collection()
        collection.insert_one(record)
    
    def bulk_insert(self, datafile, collection_name: str = None) -> None:
        if datafile.endswith('.csv'):
            dataframe = pd.read_csv(datafile, encoding='utf-8')
        elif datafile.endswith(".xlsx"):
            dataframe = pd.read_excel(datafile, encoding='utf-8')
        else:
            raise ValueError("Unsupported file format")
            
        datajson = json.loads(dataframe.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(datajson)

    def query_data(self, query: dict, collection_name: str) -> list:
        collection = self.create_collection()
        result = list(collection.find(query))
        return result
    
    def update_record(self, filter_query: dict, update_data: dict, collection_name: str) -> None:
        collection = self.create_collection()
        collection.update_one(filter_query, {"$set": update_data})
    
    def delete_record(self, query: dict, collection_name: str) -> None:
        collection = self.create_collection()
        collection.delete_many(query)
