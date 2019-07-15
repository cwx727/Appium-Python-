import unittest
import HtmlTestRunner 
import threading
import multiprocessing
import time
from appium import webdriver
import sys
sys.path.append("..") 
from business.login_business import LoginBusiness
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
	'''
	unittest能传入参数，编写父类
	'''
	def __init__(self, methodName='runTest',parame=None):
		super(ParameTestCase,self).__init__(methodName)
		global parames #为了能在setUpClass(cls)中使用parame，定义全局变量
		parames = parame


class CaseTest(ParameTestCase):
	'''
	继承ParameTestCase类
	'''
	@classmethod
	def setUpClass(cls):
		print('setUpClass',parames)
		cls.login_business = LoginBusiness(parames)

	def setUp(self):
		
		print("this is setup")

	def test_01(self):
		print("para:"+str(parames))
		self.login_business.login_pass()

	#@unittest.skip("CaseTest") #跳过下面的test_02,CaseTest为类名
	def test_02(self):
		print("para:"+str(parames))
		self.login_business.login_user_error()

	def tearDown(self):
		print("this is teardown")


def appium_init():
	server = Server()
	server.main()


def get_suite(i):
	suite = unittest.TestSuite()
	suite.addTest(CaseTest("test_02",parame=i))
	suite.addTest(CaseTest("test_01",parame=i))
	#unittest.TextTestRunner().run(suite)
	file_name = 'report'+str(i+1)
	HtmlTestRunner.HTMLTestRunner(output="../report",report_name=file_name).run(suite)
def get_count():
	writer_user_file = WriteUserCommand()
	count = writer_user_file.get_file_lines()
	return count

if __name__ == '__main__':
	appium_init()
	threads = []
	for i in range(get_count()):
		print('threads',i)
		#t = threading.Thread(target=get_suite,args=(i,)) #多线程
		t = multiprocessing.Process(target=get_suite,args=(i,))
		threads.append(t)
	for j in threads:
		j.start()




