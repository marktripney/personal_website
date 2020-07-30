from datetime import date
from flask import Flask, render_template, url_for

app = Flask(__name__)
year = date.today().year


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="home")


@app.route("/work")
def work():
    return render_template("work.html", title="work")


@app.route("/writing")
def writing():
    return render_template("writing.html", title="writing")


if __name__ == "__main__":
    app.run()
