import yaml

class WriteUserCommand:
	def read_data(self):
		'''
		读取yaml文件数据，返回字段
		'''
		with open('../config/userconfig.yaml') as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
		return data

	def get_value(self,key,port):
		'''
		获取yaml文件字典中某个参数值
		'''
		data = self.read_data()
		value = data[key][port]
		return value

	def write_data(self,i,device,bp,port,systemport):
		'''
		数据写入yaml文件
		'''
		data = self.join_data(i,device,bp,port,systemport)
		with open("../config/userconfig.yaml","a") as f:
			yaml.dump(data,f)

	def join_data(self,i,device,bp,port,systemport):
		data = {
		'user_info_'+str(i):{
		'daviceName':device,
		'bp':bp,
		'port':port,
		'systemport':systemport
		}}
		return data

	def clear_data(self):
		'''
		删除yaml文件内容
		'''
		with open("../config/userconfig.yaml","w") as f:
			f.truncate()

	def get_file_lines(self):
		data = self.read_data()
		return len(data)




if __name__ == '__main__':
	WriteUserCommand().write_data(1,'127.0.0.1:21503','4900','4700',5100)
	print(WriteUserCommand().get_value('user_info_1','bp'))
	#print(write_file)