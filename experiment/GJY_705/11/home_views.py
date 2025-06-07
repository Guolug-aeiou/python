from flask import render_template, Blueprint, request, redirect,session
from pymysql_utils import MySQLUtils

home = Blueprint('home', __name__)

db = MySQLUtils('localhost', 'root', 'root', 'mini_blog')

@home.route("/register",methods=['POST','GET'])
def register():
    if request.method == "POST":
        db.update("INSERT INTO users(`username`,`password`,`nickname`,`email`) VALUES(%s,%s,%s,%s)",
                        (request.form.get('username'), request.form.get('password'), request.form.get('nickname'), request.form.get('email')))
        return redirect('/home/login')
    if request.method == "GET":
        return render_template('/home/register.html')
@home.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.date)
        return redirect("/home/article")
    if request.method == "GET":
        users = db.select_list("SELECT * FROM users")
        articles = db.select_list("SELECT * FROM articles ORDER BY `reads` DESC LIMIT 5")
        categories = db.select_list("SELECT * FROM articles ORDER BY `create_date` DESC LIMIT 5")
        return render_template("home/index.html", users=users, articles=articles, categories=categories)


@home.route("/article_list/<int:user_id>")
def article_list(user_id):
    nickname = db.select_list("SELECT nickname FROM users where id = %s", user_id)[0]["nickname"]
    categories = db.select_list("SELECT * FROM categories")
    articles = db.select_list("select * from articles where author_id = %s", user_id)
    hot_log_five = db.select_list("select * from articles where author_id = %s ORDER BY `reads` DESC LIMIT 5", user_id)
    return render_template("home/article-list.html", nickname=nickname, categories=categories, articles=articles,
                           hot_log_five=hot_log_five)


@home.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_name = db.select_list("SELECT * FROM users WHERE username = %s", request.form.get("userName"))
        if request.form.get("userName") == login_name[0]["username"] and request.form.get("userPwd") == login_name[0][
            "password"]:
            # 使用 session 来存储临时数据
            session['user'] = {'username': request.form.get("userName"),
                               'password': request.form.get("userPwd"),
                               'nickname': login_name[0]["nickname"]}
            return redirect("/admin/articles")
        else:
            print("错误")
            return render_template("home/login.html")
    elif request.method == "GET":
        return render_template("home/login.html")
