import os

class DosCmd:
	def excute_cmd_get_result(self,command):
		'''
		返回cmd中命令的执行结果,如cmd输入adb devices后的结果
		'''
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i =='\n':
				continue
			result_list.append(i.strip('\n'))

		return result_list

	def excute_cmd(self,command):
		os.system(command)

if __name__ == '__main__':
	print(DosCmd().excute_cmd_get_result('adb devices'))
