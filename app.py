from flask import Flask, request
import pymongo

app = Flask(__name__)


def main():
    """"""

    user_name = "martin"
    password = "billybob"
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.pythonanime
    collection_animes = db.animes
    collection_directors = db.directors

    @app.route("/", methods=["POST", "GET"])
    def saluy():
        args = request.args
        print(args)
        return args


if __name__ == "__main__":
    main()
