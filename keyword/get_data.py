import sys
sys.path.append("..")
from util.opera_excel import OperaExcel
class GetData:
	def __init__(self):
		self.opera_excel = OperaExcel()

	def get_case_lines(self):
		'''
		获取case.xlsx行数
		'''
		lines = self.opera_excel.get_lines()
		return lines

	def get_handle_step(self,row):
		'''
		获取case.xlsx的步骤列，即操作方法名称
		'''
		method_name = self.opera_excel.get_cell(row,3)
		return method_name

	def get_element_key(self,row):
		'''
		获取case.xlsx的元素列，即元素的key
		'''
		element_key = self.opera_excel.get_cell(row,4)
		if element_key =='':
			return None
		else:
			return element_key

	def get_handle_value(self,row):
		'''
		获取case.xlsx的操作值列，即输入的数据
		'''
		handle_value = self.opera_excel.get_cell(row,5)
		if handle_value =='':
			return None
		else:
			return handle_value

	def get_expect_element(self,row):
		'''
		获取case.xlsx的预期元素列
		'''
		expect_element = self.opera_excel.get_cell(row,6)
		if expect_element =='':
			return None
		else:
			return expect_element

	def get_is_run(self,row):
		'''
		获取case.xlsx的是否运行列
		'''
		is_run = self.opera_excel.get_cell(row,9)
		if is_run == 'yes':
			return True
		else:
			return False

	def get_expect_handle(self,row):
		'''
		获取case.xlsx的是否运行列
		'''
		expect_handle = self.opera_excel.get_cell(row,7)
		if expect_handle =='':
			return None
		else:
			return expect_handle

	def get_expect_value(self,row):
		'''
		获取case.xlsx的是否运行列
		'''
		expect_value = self.opera_excel.get_cell(row,8)
		if expect_value =='':
			return None
		else:
			return expect_value

	def write_value(self,row,value):
		self.opera_excel.write_value(row,value)

if __name__ == '__main__':
	print(GetData().get_case_lines())
	print(GetData().get_expect_handle(3))

