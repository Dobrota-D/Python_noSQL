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
    print(anime_list)

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
    print(director_list)
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

    body = request.get_json

    new_anime = {
        "_id": body["_id"],
        "title": body["title"],
        "genre": body["genre"],
        "animation_studio": body["animation_studio"],
        "director": body["director"],
        "release_date": body["release_date"],
        "episodes": body["episodes"],
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
    body = request.json
    new_directors = {
        "_id": body["_id"],
        "firstname": body["firstname"],
        "lastname": body["lastname"], "age": body["age"],

        "gender": body["gender"],
        "creation": body["creation"],
        "birthdate": body["birthdate"],
        "animation_studio": body["animation_studio"],
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
    patch_animes()


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
