PO模型、关键字模型
# #	定义# #
		Page Object Model的核心是分离测试对象和测试数据
# 	config #
		配置测试数据等
		case.xls，关键字模型的测试步骤及数据
		LocalElement.ini，页面元素的属性等
		userconfig.yaml，多进程，程序自动存储的设备号，端口信息
# 	util #
		读取config文件中的元素属性信息key，value
		定义查找元素是按照id或者classname等方式，返回driver.find_element_by_key('value')
		dos_cmd.py，python调用执行cmd命令
		get_by_local.py，分解ini文件，取到元素方法、属性，并返回driver.find_element_by_XXX（元素属性）
		opera_excel.py，关键字模型，处理excel
		port.py，判断端口是否被占用，生成可用的端口
		read_init.py，读取ini文件等号后面的值
		server.py，多线程启动多台设备的appium
		write_user_command.py，定义处理yaml文件的方式
# 	base #
		定义driver
# 	page #
		调取util，整合util中的文件，定义被测页面全部元素信息；调用driver，定义driver
# 	handle #
		调用page，定义被测页面全部元素的操作方式，如send_keys或click
# 	business #
		业务：调用handle，传入输入框数据等参数等，定义测试案例的操作步骤
# 	case #
		调用business，执行测试案例、报告输出定义等
# 	report #
		存储测试报告
# 	keyword #
		aciton_method.py，关键字模型，定义操作，获取元素属性等操作
		get_data.py，从调用util-opera_excel.py,从config-case.xls中，获取关键字模型的数据
		run_main.py，关键字模型运行程序的入口，执行excel测试案例，并填写测试结果
# 	log #
		appium的允许日志存储的地方
