import flask
from flask import Flask
import pymongo
app = Flask(__name__)

def main():

    user_name = "dobrota"
    password = "larry"
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )

    db = client.testdb
    collection = db.users
    for i in range(1, 11):
        user = {
            "_id" : i,
            "first_name" :
        }