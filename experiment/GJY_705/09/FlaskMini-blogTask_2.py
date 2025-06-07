from flask import Flask, render_template

# 创建应用，使用原始字符串避免路径转义问题
app_static = Flask(__name__)


# 创建路由
@app_static.route("/blog")
def index():
    return render_template("home/index.html")


@app_static.route("/login")
def login():
    return render_template("home/login.html")


@app_static.route("/register")
def register():
    return render_template("home/register.html")



# 启动应用，开启调试模式
if __name__ == '__main__':
    app_static.run(debug=True)
