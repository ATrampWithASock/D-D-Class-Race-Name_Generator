from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def character():
    ch_class = requests.get("http://classapi:5000/class")
    race = requests.get("http://raceapi:5000/race")
    firstname = requests.post("http://nameapi:5000/name", race=race.text)
    surname = requests.post("http://nameapi:5000/name", ch_class=ch_class.text)
    return render_template("homepage.html", ch_class=ch_class.text, race=race.text, firstname=firstnamename.txt, surname-surname.txt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)