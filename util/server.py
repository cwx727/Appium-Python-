import sys
sys.path.append("..") 
from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand
import time


class Server:
	def __init__(self):
		self.dos = DosCmd()
		self.devices_list = self.get_devices()
		self.write_file = WriteUserCommand()

	def get_devices(self):  
		'''
		获取设备信息
		返回信息格式['127.0.0.1:21503', '127.0.0.1:21523']
		'''
		devices_list = []
		#self.dos = DosCmd()
		result_list = self.dos.excute_cmd_get_result('adb devices')
		if len(result_list) >=2:
			for i in result_list:
				if i[-6:] == 'device':
					devices_list.append(i[:-7])
			return devices_list

		else:
			return none

	def create_port_list(self,start_port):
		'''
		按照adb devices的设备台数，以及端口是否被专用，生成可用的端口号
		'''
		port = Port()
		port_list = port.create_port_list(start_port, self.devices_list)
		return port_list

	def create_command_list(self,i):
		'''
		根据设备名，台数以及端口信息，返回启动appium的命令
		'''
		command_list = []
		appium_port_list = self.create_port_list(4700)
		bootstrap_port_list = self.create_port_list(4900)
		system_port_list = self.create_port_list(5100)
		device_list = self.devices_list
		command = 'appium -p ' +str(appium_port_list[i])+ ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + device_list[i] + ' --no-reset --session-override --log ../log/test'+str(i+1)+'.log'
		command_list.append(command)
		self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]),system_port_list[i])

		return command_list

	def start_server(self,i):
		'''
		被线程调用，通过程序，自动启动appium多台设备
		'''
		self.start_list = self.create_command_list(i)
		print(self.start_list)
		self.dos.excute_cmd(self.start_list[0])

	def kill_server(self):
		'''
		判断node是否允许，允许的话，杀掉进程
		'''
		server_list = self.dos.excute_cmd_get_result('tasklist | findstr "node.exe"')
		if len(server_list) > 0:
			self.dos.excute_cmd('taskkill -F -PID node.exe')


	def main(self):
		'''
		调用start_server，多线程启动多台设备的appium
		'''
		self.write_file.clear_data()
		self.kill_server()
		for i in range(len(self.devices_list)):
			appium_start = threading.Thread(target=self.start_server,args=(i,))
			appium_start.start()

		time.sleep(20)

if __name__ == '__main__':
	Server().main()



