from util.read_init import ReadIni

class GetByLocal:

	def __init__(self, driver):
		self.driver = driver


	def get_element(self, key):
		'''
		分解ini文件，取到元素方法、属性，并返回driver.find_element_by_XXX（元素属性）
		'''
		read_ini = ReadIni()
		local = read_ini.get_value(key)

		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			try:
				if by =='id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				print('-------------------------------------111-------------')
				self.driver.save_screenshot('../jpg/test01.png')
				return None
		else:
			None


if __name__ == '__main__':
	get_by_local = GetByLocal()
	print(get_by_local.get_element('username'))
