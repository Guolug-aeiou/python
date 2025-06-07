from flask import Flask
# 创建应用
app = Flask(__name__)
# 路由
@app.route('/')
def fun():
    return '<h1>hello world</h1>'
@app.route('/wd')
def funwd():
    return '<h1>hello Flask!</h1>'
# 运行应用
app.run()
