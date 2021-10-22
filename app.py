import pymongo
from flask import Flask, request
import json

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


@app.route("/animes/<_id>", methods=["PATCH"])
def patch_animes():
    id_select = int(id)
    # if the request method is PATCH
    if request.method == "PATCH":
        # if the requested id is found
        if collection_animes.find({"_id": f"{id_select}"}):
            # return a json with the new values of a animes
            animes = json.loads(request.data.decode("utf-8"))
            # compare the modifications with existing values
            if animes != collection_animes:
                anime_title = animes["title"]
                anime_release_date = animes["release_date"]
                anime_genre = animes["genre"]
                anime_episodes = animes["episodes"]
                anime_director = animes["director"]
                anime_animation_studio = animes["animation_studio"]
                # update the database with the new values using the update_one() method
                # The first parameter is a query object defining which document to update : id
                # The second parameter is an object defining the new values of the document : new values
                collection_animes.update_one({"_id": id_select}, {
                    "$set": {"title": anime_title, "release_date": anime_release_date, "genre": anime_genre,
                             "episodes": anime_episodes, "director": anime_director,
                             "animation_studio": anime_animation_studio}})


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
        "_id": "11",
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


if __name__ == "__main__":
    patch_animes()
