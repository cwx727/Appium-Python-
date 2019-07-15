import sys
sys.path.append("..") 
from util.dos_cmd import DosCmd

class Port:
	def port_is_used(self,port_num):
		'''
		判断端口是否被占用
		'''
		command = 'netstat -ano | findstr ' + str(port_num)
		result = DosCmd().excute_cmd_get_result(command)
		if len(result)>0:
			flag = True
		else:
			flag = False
		return flag

	def create_port_list(self,start_port,device_list):
		'''
		返回可用的端口列表
		'''
		port_list = []
		if device_list != None:
			while len(port_list) != len(device_list):
				if self.port_is_used(start_port) != True:
					port_list.append(start_port)
				start_port = start_port +1
			return port_list
		else:
			print("生成可用端口失败")
			return None


if __name__ == '__main__':
	device_list=[1,2,3,4,5]
	print(Port().create_port_list(8079,device_list))


