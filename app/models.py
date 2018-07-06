# coding:utf8
from app import db
from datetime import datetime


#  会员
class User(db.Model):
	__tablename__ = 'user'  # 数据库中的表名
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 昵称
	pwd = db.Column(db.String(100))  # 密码
	email = db.Column(db.String(100), unique=True)  # 邮箱
	phone = db.Column(db.String(11), unique=True)  # 手机号
	info = db.Column(db.Text)  # 个人简介
	face = db.Column(db.String(255), unique=True)  # 头像
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
	
	# 会员日志外键关系关联
	# (解释：userlogs 与 Userlog 进行外键关联，绑定user表)
	userlogs = db.relationship('Userlog', backref='user')
	
	# 评论外键关系关联
	comments = db.relationship('Comment', backref='user')
	
	#  电影收藏关系关联
	moviecols = db.relationship('Moviecol', backref='user')
	
	def __repr__(self):
		return "<User %r>" % self.name


# 会员登陆日志
class Userlog(db.Model):
	__tablename__ = 'userlog'
	id = db.Column(db.Integer, primary_key=True)  # 编号
	
	# db调用ForeignKey外键，去关联user表中的id字段
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
	ip = db.Column(db.String(100))  # 登陆IP
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间
	
	def __repr__(self):
		return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
	__tablename__ = 'tag'
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 标题
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	#  电影外键关系关联
	movies = db.relationship('Movie', backref='tag')
	
	def __repr__(self):
		return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
	__tablename__ = 'movie'
	id = db.Column(db.Integer, primary_key=True)  # 编号
	title = db.Column(db.String(255), unique=True)  # 标题
	url = db.Column(db.String(255), unique=True)  # 地址
	info = db.Column(db.Text)  # 简介
	logo = db.Column(db.String(255), unique=True)  # 封面
	star = db.Column(db.SmallInteger)  # 星级
	playnum = db.Column(db.BigInteger)  # 播放量
	commentnum = db.Column(db.BigInteger)  # 评论量
	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
	area = db.Column(db.String(255))  # 上映地区
	release_time = db.Column(db.Date)  # 上映时间
	length = db.Column(db.String(100))  # 播放时间
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	# 评论外键关系关联
	comments = db.relationship('Comment', backref='movie')
	
	# 电影收藏关系关联
	moviecols = db.relationship('Moviecol', backref='movie')
	
	def __repr__(self):
		return "<Movie %r>" % self.title


# 上映预告
class Preview(db.Model):
	__tablename__ = 'preview'
	id = db.Column(db.Integer, primary_key=True)  # 编号
	title = db.Column(db.String(255), unique=True)  # 标题
	logo = db.Column(db.String(255), unique=True)  # 封面
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	def __repr__(self):
		return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
	__tablename__ = 'comment'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 需设置外键，关联movie表中的id
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 需设置外键，关联user表中的id
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Comment %r>" % self.id


# 电影收藏
class Moviecol(db.Model):
	__tablename__ = 'moviecol'
	id = db.Column(db.Integer, primary_key=True)
	movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 设置外键，关联movie表中的id
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 设置外键，关联user表中的id
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
	__tablename__ = 'auth'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	url = db.Column(db.String(255), unique=True)
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
	__tablename__ = 'role'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	auths = db.Column(db.String(600))  # 角色列表
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
	__tablename__ = 'admin'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	pwd = db.Column(db.String(100), unique=True)
	is_super = db.Column(db.SmallInteger)  # 是否为超级管理员  0表示为超级管理员
	role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	# 管理员登陆日志关系关联
	adminlogs = db.relationship('Adminlog', backref='admin')
	
	# 操作日志关系关联
	oplogs = db.relationship('Oplog', backref='admin')
	
	def __repr__(self):
		return "<Admin %r>" % self.name


# 管理员登陆日志
class Adminlog(db.Model):
	__tablename__ = 'adminlog'
	id = db.Column(db.Integer, primary_key=True)
	admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
	ip = db.Column(db.String(100))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Adminlog %r>" % self.id


# 操作日志
class Oplog(db.Model):
	__tablename__ = 'oplog'
	id = db.Column(db.Integer, primary_key=True)
	admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
	ip = db.Column(db.String(100))
	reason = db.Column(db.String(600))  # 操作原因
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)
	
	def __repr__(self):
		return "<Oplog %r>" % self.id


#  把以上所有模型进行调用运行，生成表
if __name__ == '__main__':
	# db.create_all()  # db调用create_all（）对象来运行上述模型
	role = Role(
		name="超级管理元",
		auths=""
	)
	db.session.add(role)  # 添加字段
	db.session.commit()  # 提交，保存内容
