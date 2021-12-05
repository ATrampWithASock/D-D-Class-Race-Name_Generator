from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def character():
    class = requests.get("http://classapi:5000/class")
    race = requests.get("http://raceapi:5000/race")
    name = requests.post("http://nameapi:5000/name", class=class.text, race=race.text)
    return render_template("homepage.html", class=class.text, race=race.text, name=name.txt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)