import pymongo
from flask import Flask, request

"""
Her we gonna init the link between the mongodb database and the app.py, by using the admin account in the user_name
password to access the database and collections and use flask for the root the local server.
"""

user_name = "martin"
password = "billybob"
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.pythonanime
collection_animes = db.animes
collection_directors = db.directors

app = Flask(__name__)


@app.route("/animes", methods=["GET"])
def display_anime():
    """
        We are going to sort anime by decreasing order
    """
    # life = collection_animes.find().sort("firstname", -1)
    anime_list = list(collection_animes.find())

    return \
        {
            "anime_list": anime_list
        }


@app.route("/directors", methods=["GET"])
def display_director():
    """
        We are going to sort director by decreasing order
    """
    # life = collection_directors.find().sort("firstname", -1)
    director_list = list(collection_directors.find())

    return \
        {
            "director_list": director_list
        }


"""

  We are going to create a new anime in the anime collection
    
 """


@app.route("/animes", methods=["POST"])
def create_anime():
    """

    we create a new anime with several args

    """
    new_anime = {
        "_id": "12",
        "title": "one piece",
        "genre": "adventure",
        "animation_studio": "jesaispas",
        "director": "uda",
        "release_date": "2088",
        "episodes": "1000",
    }
    """

    this will push the new anime in the animes collection 

    """
    collection_animes.insert_one(new_anime)
    """

    this will return a message if anime is created   

    """

    return {'code': 200, 'msg': 'new anime has been created'}


@app.route("/directors", methods=["POST"])
def create_directors():
    """

    we create a new anime with several args

    """
    new_directors = {
        "_id": "12",
        "firstname": "michaïle",
        "lastname": "jorge",
        "age": "12",
        "gender": "none",
        "creation": "violet",
        "birthdate": "2001",
        "animation_studio": "kanaba",
    }
    """

    this will push the new anime in the animes collection 

    """
    collection_directors.insert_one(new_directors)
    """

    this will return a message if anime is created   

    """

    return {'code': 200, 'msg': 'new directors has been add'}


if __name__ == "__main__":
    create_directors()
