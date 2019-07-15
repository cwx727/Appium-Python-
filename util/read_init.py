import configparser
'''

read_ini = configparser.ConfigParser()
read_ini.read('../config/LocalElement.ini')
print(read_ini.get('login_element','username'))
'''

class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '../config/LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		#read_ini.read('file_path')
		read_ini.read(self.file_path)
		return read_ini

	def get_value(self, key, section = 'login_element'):
		'''
		获取ini文件中的key值
		'''
		try: 
			value = self.data.get(section,key)
		except:
			value = None
		return value



if __name__ == '__main__':
	read_ini = ReadIni()
	print(read_ini.get_value('username','login_element'))