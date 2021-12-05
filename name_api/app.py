from flask import Flask, Response, request
from random import randint

app = Flask(__name__)

@app.route("/firstname", methods=["POST"])
def firstname():
    race = request.data.decode("utf-8")
    if race == "Human":
        firstname = "Stor"
    elif race == "Dwarf":
        firstname = "Dagney"
    elif race == "Elf":
        firstname = "Sharos"
    elif race == "Orc":
        firstname = "Turrf"
    elif race == "Half-Elf":
        firstname = "Faeryl"
    elif race == "Dragonborn":
        firstname = "Karim"
    else:
        firstname = "This was not a selectable race"
    return Response(firstname, mimetype='text/plain')

@app.route("/surname", methods=["POST"])
def surname():
    ch_class = request.data.decode("utf-8")
    if ch_class == "ranger":
        surname = "Hornraven"
    elif ch_class == "fighter":
        surname = "Axebreaker"
    elif ch_class == "wizard":
        surname = "Arcanos"
    elif ch_class == "druid":
        surname = "Hallowhawk"
    elif ch_class == "barbarian":
        surname = "Shieldshatterer"
    elif ch_class == "warlock":
        surname = "Darkspawn"
    else:
        surname = "This was not a selectable class"
    return Response(surname, mimetype='text/plain')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)