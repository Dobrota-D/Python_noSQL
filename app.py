from flask import Flask

app = Flask(__name__)


@app.route("/<id>", methods=["DELETE"])
def delete(id):
    import os
    number = input("which file do you want to delete ?")
    print(number)
    if os.path.exists("users/" + number + ".txt"):
        os.remove("users/" + number + ".txt")
    else:
        print("The file does not exist")
