from flask import Flask, Response
from random import randint

app = Flask(__name__)

@app.route("/race", methods=["GET"])
def race():
    races = ["Human","Dwarf","Elf","Orc","Half-Elf","Dragonborn"]
    random = races[randint(0,5)]
    return Response(random, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)