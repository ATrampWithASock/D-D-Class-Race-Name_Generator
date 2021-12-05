from flask import Flask, Response
from random import randinit

app = Flask(__name__)

@app.route("/class", methods=["GET"])
def ch_class():
    classes = ["ranger","fighter","wizard","druid","barbarian","warlock"]
    random = classes[randint(0,5)]
    return Response(random, mimetype="text/plain")