import sys
sys.path.append("..") 
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal
#from util.read_init import ReadIni



def get_driver():
	capabilities = {
	  "platformName": "Android",
	  "automationName": "UiAutomator2",
	  "deviceName": "127.0.0.1:21503",
	  #"deviceName":"2a25e47b7d29",
	  "app": "E:\\mukewang.apk",
	  #"app": "E:\\慕课网.apk",
	  #"appActivity" : ".index.splash.GuideActivity"
	  "noReset":"true"
	}

	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
	time.sleep(3)
	return driver

#获取屏幕宽高
def get_size():
	size = driver.get_window_size()
	width = size['width']
	height = size['height']
	return width,height

#向左滑动
def swipe_left():
	x1 = get_size()[0]/10*9
	y1 = get_size()[1]/2
	x = get_size()[0]/10
	driver.swipe(x1,y1,x,y1)

#向右滑动
def swipe_right():
	x1 = get_size()[0]/10
	y1 = get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1)

#向上滑动
def swipe_up():
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y)

#向下滑动
def swipe_down():
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)

def swipe_on(direction):
	if direction == 'up':
		swipe_up()
	elif direction == 'down':
		swipe_down()
	elif direction == 'left':
		swipe_left()
	elif direction == 'right':
		swipe_right()

#通过resource_id定位
def go_login():
	#print(driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login'))
	driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

#通过class定位
def go_login_by_class():
	#print(driver.find_element_by_class_name('android.widget.TextView'))
	elements = driver.find_elements_by_class_name('android.widget.TextView')
	#print(elements)
	#print(len(elements))
	elements[4].click()

#通过id定位
def login():
	get_by_local = GetByLocal(driver)
	get_by_local.get_element('username').send_keys('18513199586')
	get_by_local.get_element('password').send_keys('111111')
	get_by_local.get_element('login_button').click()

	'''
	driver.find_element_by_id(username).send_keys('18513199586')
	driver.find_element_by_id(password).send_keys('111111')
	driver.find_element_by_id(login_button).click()
	'''

#通过层级定位
def login_by_node():
	element = driver.find_element_by_id('cn.com.open.mooc:id/sv_scrollview')  #查找需要定位的上级元素id
	elements = element.find_elements_by_class_name('android.widget.EditText')
	elements[0].send_keys('18513199586')
	elements[1].send_keys('111111')
	driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()

#通过uiautomator定位
def login_by_uiautomator():
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').clear()
	driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys('18513199586')
	driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys('111111')

def login_by_xpath():
	driver.find_element_by_xpath('//*[contains(@text,"忘记")]').click()#找到页面中text包含“忘记”的元素
	#driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]').click() #查找页面属性是android.widget.TextView，text是忘记密码的元素
	#driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"忘记")]').click()#查找页面属性是android.widget.TextView，text是包含“忘记”的元素
	'''
	#通过子节点，找父节点的兄弟节点
	driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::android.widget.RelativeLayout').send_keys('123')
	driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[@index="2"]').send_keys('111111')
	'''
def get_web_wiev():
	#time.sleep(5)
	webview = driver.contexts

	for view in webview:
		print(view)
		if view == 'NATIVE_APP':
			print("true")
			driver.switch_to.context(view)
			break
	time.sleep(5)
	driver.find_element_by_id('cn.com.open.mooc:id/icon_close').click()

def get_toast():
	time.sleep(5)
	#driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18513199587')


	#driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()
	get_by_local = GetByLocal(driver)
	get_by_local.get_element('username').send_keys('18513199587')
	get_by_local.get_element('password').send_keys('111111')
	get_by_local.get_element('login_button').click()
	time.sleep(2)

	toast_element = ("xpath", "//*[contains(@text,'账号未注册')]")
	print(type(toast_element))

	print(WebDriverWait(driver, 10,0.1).until(EC.presence_of_element_located(toast_element)))

driver = get_driver()
'''
swipe_on('left')
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('right')
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('up')
time.sleep(2)
'''

go_login()
#go_login_by_class()
get_toast()
#login_by_node()
#login_by_uiautomator()
#login_by_xpath()
#get_web_wiev()

#get_toast()
#print(driver.page_source)


#driver.quit()