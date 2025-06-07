from flask import Flask, render_template
from pymysql_utils import MySQLUtils

app = Flask(__name__)


@app.route("/index")
def index():
    db = MySQLUtils('localhost', 'root', '123456', 'mini_blog')
    nicknames = db.select_list("SELECT nickname FROM users")
    articles = db.select_list("SELECT * FROM articles ORDER BY `reads` DESC LIMIT 5")
    categories = db.select_list("SELECT * FROM articles ORDER BY `create_date` DESC LIMIT 5")
    return render_template("home/index.html", nicknames=nicknames, articles=articles,categories=categories)


if __name__ == '__main__':
    app.run(debug=True)
