from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("home/index.html")


@app.route("/index/<int:page>")
def index_param(page):
    return f"<h1>{page}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
