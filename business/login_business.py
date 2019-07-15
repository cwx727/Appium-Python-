import sys
sys.path.append("..") 
from handle.login_handle import LoginHandle
import time

class LoginBusiness:
	def __init__(self,i):
		self.login_handle = LoginHandle(i)

	def login_pass(self):
		self.login_handle.send_username('18513199586')
		self.login_handle.send_password('111111')
		self.login_handle.click_login()

	def login_user_error(self):
		self.login_handle.send_username('18513199587')
		self.login_handle.send_password('111111')
		self.login_handle.click_login()
		time.sleep(3)
		user_flag = self.login_handle.get_fail_toast('账号未注册')


		if user_flag:
			return True
		else:
			return False

	def login_password_error(self):
		self.login_handle.send_username('18513199586')
		self.login_handle.send_password('111112')
		self.login_handle.click_login()
		time.sleep(3)
		user_flag = self.login_handle.get_fail_toast('登录密码错误')
		if user_flag:
			return True
		else:
			return False
