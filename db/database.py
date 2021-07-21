# coding=utf-8
# !/usr/bin/python3

import pymongo


class Database:
    def __init__(self, database="Flask-Demo", collection="null") -> None:
        super().__init__()
        user_id = "dev:v39QiKuCWUHUcGdj@flask-demo-cluster.kwy4z.mongodb.net"
        client_url = "mongodb+srv://" + user_id + "/" + database + "?retryWrites=true&w=majority"
        client = pymongo.MongoClient(client_url)
        db = client[database]
        self.collection = db[collection]

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, new_value):
        self.collection.update_one(query, new_value, upsert=True)

    def insert_one(self, query):
        self.collection.insert_one(query)

    def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def last(self, limit=5):
        return list(self.collection.find().sort([('_id', pymongo.DESCENDING)]).limit(limit))

    def clear(self):
        self.collection.drop()

    def remove(self, query):
        self.collection.remove(query)
