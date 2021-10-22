import pymongo
from flask import Flask, request
from markupsafe import escape

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
        "_id": "14",
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


@app.route("/animes/<_id>", methods=["DELETE"])
def delete_anime(_id):
    """This function will delete the anime by using the id in the collection
        _id = this is the id from the anime we want to delete
    """

    collection_animes.delete_one({"_id": int(_id)})

    return {'code': 200, 'msg': 'an anime has been deleted'}


@app.route("/directors/<_id>", methods=["DELETE"])
def delete_director(_id):
    """This function will delete the director by using the id in the collection
        _id = this is the id from the director we want to delete
    """
    collection_directors.delete_one({"_id": int(_id)})

    return {'code': 200, 'msg': 'an director has been deleted'}

def genreate_anime_id ()
    