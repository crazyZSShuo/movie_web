#  前台表单验证
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin


class LoginForm(FlaskForm):
	"""管理员登陆表单"""
	account = StringField(
		label="账号",
		# 验证字段
		validators=[
			DataRequired("请输入账号！")
		],
		description="账号",
		render_kw={
			
			"class": "form-control",
			"placeholder": "请输入账号！",
			"required": "required"  # 必须项，前台会自动判别是否填写；
		}
	)
	pwd = PasswordField(
		label="密码",
		validators=[
			DataRequired("请输入密码！")
		],
		description = "密码",
		render_kw={
			"class" :"form-control",
			"placeholder":"请输入密码！",
			"required":"required"
		}
	)
	submit = SubmitField(
		"登陆",
		render_kw={
			"class":"btn btn-primary btn-block btn-flat"
		}
	)
	
	#  自定义的字段验证器
	def validate_account(self,field):
		account = field.data
		admin = Admin.query.filter_by(name=account).count() # 查找数据库中的存在的数量
		if admin == 0:
			raise ValidationError("账号不存在！") # raise 抛出验证的错误
	
