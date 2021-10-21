from flask import Flask, request
import pymongo

app = Flask(__name__)

user_name = "martin"
password = "billybob"
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{password}@cluster0.zpvod.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.pythonanime
collection_animes = db.animes
collection_directors = db.directors

collection_animes.insert_one({"messages": "oui"})
print("done")


    @app.route("/", methods=["POST", "GET"])
    def saluy():
        args = request.args
        print(args)
        return args


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=3000,
        debug=True
    )
