import sys
sys.path.append("..") 
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class LoginPage:
	def __init__(self,i):
		base_driver =BaseDriver()
		self.driver = base_driver.android_driver(i)
		self.get_by_local = GetByLocal(self.driver)

	def get_username_element(self):
		return self.get_by_local.get_element('username')

	def get_password_element(self):
		return self.get_by_local.get_element('password')

	def get_login_button_element(self):
		return self.get_by_local.get_element('login_button')

	def get_forget_password_element(self):
		return self.get_by_local.get_element('forget_password')

	def get_register_element(self):
		return self.get_by_local.get_element('register')


	def get_toast_element(self, message):
		xpath_element = "//*[contains(@text," + message + ")]"
		#toast_element = ("xpath", "//*[contains(@text,'+message+')]")
		toast_element = ("xpath", xpath_element)
		#print(type(toast_element))
		#print(WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_element)))

		return WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_element))

