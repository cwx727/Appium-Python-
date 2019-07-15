import time
from appium import webdriver
import sys
sys.path.append("..") 
from util.write_user_command import WriteUserCommand


class BaseDriver:
	def android_driver(self,i):
		'''
		手机的driver信息
		'''
		write_file = WriteUserCommand()
		device = write_file.get_value('user_info_'+str(i), 'daviceName')
		port = write_file.get_value('user_info_'+str(i), 'port')
		systemport = write_file.get_value('user_info_'+str(i), 'systemport')
		
		capabilities = {
		  "platformName": "Android",
		  "automationName": "UiAutomator2",
		  "deviceName": device,
		  #"deviceName":"2a25e47b7d29",
		  "app": "E:\\mukewang.apk",
		  #"app": "E:\\慕课网.apk",
		  "appActivity" : ".user.login.MCLoginActivity",
		  "noReset":"true",
		  "systemPort":systemport,
		}
		driver = webdriver.Remote("http://127.0.0.1:" +port+"/wd/hub",capabilities)
		time.sleep(10)
		return driver

	def ios_driver(self):
		pass

	def get_driver(self):
		pass