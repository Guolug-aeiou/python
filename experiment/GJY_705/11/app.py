from flask import Flask, render_template, request, redirect, session

from admin_views import admin
from home_views import home
app = Flask(__name__)
app.secret_key = '123123123123123'
# 注册蓝图
app.register_blueprint(home,url_prefix='/home')
app.register_blueprint(admin,url_prefix='/admin')







if __name__ == '__main__':
    app.run(debug=True)
