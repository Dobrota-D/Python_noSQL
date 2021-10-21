from flask import Flask, request
import pymongo


user_name = "martin"
password = "billybob"
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.pythonanime
collection_animes = db.animes
collection_directors = db.directors

app = Flask(__name__)

@app.route("/animes", methods=["GET"])
def afficher_anime():


    """
        We are going to sort anime by alphebitical and acreasing order
    """
    yes = collection_animes.find().sort("title")

    #for x in yes:
        #print(x)

    """
        We are going to sort anime by decreasing order
    """
    yes = collection_animes.find().sort("title", -1)

    #for x in yes:
        #print(x)

    """
         We are going to sort directors by alphebitical and acreasing order
    """
    yes = collection_directors.find().sort("firstname")

    #for x in yes:
        #print(x)

    """
        We are going to sort directors by decreasing order
    """
    #life = collection_directors.find().sort("firstname", -1)
    anime_list = list(collection_animes.find())

    return \
        {
            "anime_list": anime_list
        }

@app.route("/animes", methods=["POST"])
def create_anime():
    """

    :return:
    """
    new_anime = {
        '_id': 'e'
    }
    #collection_animes.insert_one(new_anime)

    return { 'code': 200, 'msg': 'Nouvel animé créé' }


if __name__ == "__main__":
    afficher_anime()

