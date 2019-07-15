import sys
sys.path.append("..") 
from page.login_page import LoginPage

class LoginHandle:
	def __init__(self,i):
		self.login_page = LoginPage(i)

	def send_username(self,username):
		return self.login_page.get_username_element().send_keys(username)

	def send_password(self,password):
		return self.login_page.get_password_element().send_keys(password)

	def click_login(self):
		return self.login_page.get_login_button_element().click()

	def click_forget_password(self):
		return self.login_page.get_forget_password_element().click()	

	def click_register(self):
		return self.login_page.get_register_element().click()

	def get_fail_toast(self,message):
		toast_element = self.login_page.get_toast_element(message)
		if toast_element:
			return True
		else:
			return False

