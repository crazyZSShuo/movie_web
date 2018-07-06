#  蓝图 方便管理各个模块
from . import home
from flask import render_template
from flask import redirect, url_for  # 重定向，路由生成器


#  前台主页
@home.route('/')
def index():
	return render_template('home/index.html')


#  登陆
@home.route('/login/')
def login():
	return render_template('home/login.html')


#  登出，并重定向到登陆页面
@home.route('/logout/')
def logout():
	return redirect(url_for('home.login'))


#  注册页面
@home.route('/regist/')
def regist():
	return render_template('home/regist.html')


#  会员中心页面
@home.route('/user/')
def user():
	return render_template('home/user.html')


#  密码修改页面
@home.route('/pwd/')
def pwd():
	return render_template('home/pwd.html')


#  评论记录
@home.route('/comments/')
def comments():
	return render_template('home/comments.html')


#  登陆日志
@home.route('/loginlog/')
def loginlog():
	return render_template('home/loginlog.html')


#  电影收藏
@home.route('/moviecol/')
def moviecol():
	return render_template('home/moviecol.html')

#  已看过的
@home.route('/watched/')
def watched():
	return render_template('home/watched.html')

#  搜索按钮
@home.route('/search/')
def search():
	return render_template('home/search.html')

#  播放页面
@home.route('/play/')
def play():
	return render_template('home/play.html')
