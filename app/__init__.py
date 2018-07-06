from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie_web"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "you not guess" # csrf  密码保护
app.debug = True
db = SQLAlchemy(app)


#  404页面
@app.errorhandler(404)
def page_not_found(error):
	return render_template('home/404.html'),404


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
