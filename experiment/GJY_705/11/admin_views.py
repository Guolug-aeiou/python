
from  flask import Blueprint,render_template

admin = Blueprint('admin', __name__)

@admin.route("/articles")
def admin_articles():
    return render_template("admin/admin-articles.html")