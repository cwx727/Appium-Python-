import xlrd
from xlutils.copy import copy
import time

class OperaExcel:
	def __init__(self,file_path=None,i=0):
		if file_path == None:
			self.file_path = '../config/case.xls'
		else:
			self.file_path = file_path
		self.excel = self.get_excel()
		self.data = self.get_sheets(i)

	def get_excel(self):
		'''
		获取excel
		'''
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheets(self,i):
		'''
		获取sheet内容,参数i为第几个sheet
		'''
		tables = self.excel.sheets()[i]
		return tables

	def get_lines(self):
		'''
		获取excel行数
		'''
		lines = self.data.nrows
		return lines

	def get_cell(self,row,cell):
		'''
		获取单元格内容
		'''
		data = self.data.cell(row,cell).value
		return data

	def write_value(self,row,value):
		read_value = self.excel
		write_data = copy(read_value)
		write_save = write_data.get_sheet(0)
		write_save.write(row,9,value)
		write_data.save(self.file_path)


if __name__ == '__main__':
	opera = OperaExcel()
	opera.write_value(6,'pass222')
	opera.write_value(7,'pass111')
