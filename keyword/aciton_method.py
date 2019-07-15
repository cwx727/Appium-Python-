import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionMethod:
	def __init__(self):
		self.driver = BaseDriver().android_driver(0)
		self.get_by_local = GetByLocal(self.driver)

	def input_key(self,*args):#利用*args传入不确定个数参数，下面的args[0]取到第一个参数的值
		'''
		输入框
		'''
		element = self.get_by_local.get_element(args[0])
		if element == None:
			return args[0],"元素未找到"
		element.send_keys(args[1])

	def  on_click(self,*args):
		'''
		点击
		'''
		element = self.get_by_local.get_element(args[0])
		if element == None:
			return args[0],"元素未找到"
		element.click()

	def  sleep_time(self,*args):
		'''
		等待
		'''
		time.sleep(int(args[0]))

	def get_size(self,*args):
		'''
		获取屏幕宽高
		'''
		size = self.driver.get_window_size()
		width = size['width']
		height = size['height']
		return width,height

	def swipe_left(self,*args):
		'''
		向左滑动
		'''
		x1 = self.get_size()[0]/10*9
		y1 = self.get_size()[1]/2
		x = self.get_size()[0]/10

		self.driver.swipe(x1,y1,x,y1)
		print(x1,y1,x)
		print('OK')

	def swipe_right(self,*args):
		'''
		向右滑动
		'''
		x1 = self.get_size()[0]/10
		y1 = self.get_size()[1]/2
		x = self.get_size()[0]/10*9
		self.driver.swipe(x1,y1,x,y1)

	def swipe_up(self,*args):
		'''
		向上滑动
		'''
		x1 = self.get_size()[0]/2
		y1 = self.get_size()[1]/10*9
		y = self.get_size()[1]/10
		self.driver.swipe(x1,y1,x1,y)

	def swipe_down(self,*args):
		'''
		向下滑动
		'''
		x1 = self.get_size()[0]/2
		y1 = self.get_size()[1]/10
		y = self.get_size()[1]/10*9
		self.driver.swipe(x1,y1,x1,y)


	def get_element(self,*args):
		'''
		获取元素，返回如driver.find_element_by_XX(expect_key)
		'''
		element = self.get_by_local.get_element(args[0])
		if element == None:
			return None
		return element

	def get_toast(self,*args):
		toast_element = ("xpath", "//*[contains(@text,args[0])]")
		print(type(toast_element))

		print(WebDriverWait(self.driver, 10,0.1).until(EC.presence_of_element_located(toast_element)))
		element = WebDriverWait(self.driver, 10,0.1).until(EC.presence_of_element_located(toast_element))
		if element == None:
			return None
		return element

