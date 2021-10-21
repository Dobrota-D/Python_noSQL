from flask import Flask
import pymongo

app = Flask(__name__)


def main():
    """"""

    user_name = "martin"
    password = "billybob"
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.pythonanime
    collection = db.directors

    collection.insert_one({"messages": "oui"})
    print("done")


if __name__ == "__main__":
    main()
