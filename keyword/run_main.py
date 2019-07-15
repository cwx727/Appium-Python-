import sys
sys.path.append("..")
from get_data import GetData
from aciton_method import ActionMethod
from util.server import Server


class RunMain:
	def run_method(self):
		Server().main()
		data = GetData()

		aciton_method = ActionMethod()
		lines = data.get_case_lines()
		for i in range(1,lines):
			handle_step = data.get_handle_step(i)   #获得excel中步骤值
			element_key = data.get_element_key(i)   #获得excel中元素值
			handle_value = data.get_handle_value(i)   #获得excel中操作值
			expect_key = data.get_expect_element(i)   #获得excel中预期步骤值
			expect_step = data.get_expect_handle(i)   #获得excel中预期结果值
			expect_value = data.get_expect_value(i)
			print("-------第几行------:",i+1)
			#getattr--获取aciton_method中名为handle_step的值的方法或属性，返回如input_key()
			excute_method = getattr(aciton_method,handle_step)  #获得ActionMethod中的方法名，如ActionMethod().input_key

			if element_key != None:#如果操作值不为空
				excute_method(element_key,handle_value)  #传入参数，执行相应方法，返回如driver.find_element_by_XX(XXXX).send_keys(handle_value)
			else:
				excute_method(handle_value)#返回如driver.find_element_by_XX(XXXX).click()

			if expect_step != None:
				'''
				expect_result = getattr(aciton_method,expect_step)#获得ActionMethod().get_element
				print('------------expect_result-----------',expect_result)
				result = expect_result(expect_key)#返回如driver.find_element_by_XX(expect_key)
				print('-------result-----------',result)
				if result:
					data.write_value(i,'pass')
				else:
					data.write_value(i,'fail')
				'''
				expect_result = getattr(aciton_method,expect_step)#获得ActionMethod().get_element
				#print('------------expect_result-----------',expect_result)
				if expect_key:
					result = expect_result(expect_key)#返回如driver.find_element_by_XX(expect_key)
					#print('-------expect_key:result-----------',result)
					if result:
						data.write_value(i,'pass')
						#print('-------expect_key:result-----------pass')
					else:
						data.write_value(i,'fail')	
						#print('-------expect_key:result-----------fail')
				else:
					result = expect_result(expect_value)
					#print('-------expect_value:result-----------',result)
					if result:
						data.write_value(i,'pass')
						#print('-------expect_value:result-----------pass')
					else:
						data.write_value(i,'fail')	
						#print('-------expect_value:result-----------fail')	



if __name__ == '__main__':
	RunMain().run_method()