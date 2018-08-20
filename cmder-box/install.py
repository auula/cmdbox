# -*- coding=UTF-8-*-
'''
Created on 2018年7月23日12:17:13
cmder-box安装函数
@author: coding1618@gmail.com
'''

import zipfile,os,sys,time,zip,shutil
from winreg import * 


#添加环境变量
def add_path(new_dir, scope='user'):
    assert scope in ('user', 'system')
    if scope == 'user':
        key = HKEY_CURRENT_USER
        subkey = 'Environment'
    else:
        key = HKEY_LOCAL_MACHINE
        subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    
    key_handle = OpenKey(key, subkey, 0, KEY_ALL_ACCESS)
    path, data_type = QueryValueEx(key_handle, 'path')
    if path.lower().find(new_dir.lower()) != -1:
		i = 1+1
        #print('"%s" already exists in path!' % new_dir)
    else:
        path = os.pathsep.join(path.split(os.pathsep) + [new_dir])
        SetValueEx(key_handle, 'path', 0, data_type, path)
    key_handle.Close()



#检查目录
def mkdir(path):
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
	
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        #print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        shutil.rmtree(path)
        return False

		
		
#设置环境变量
def setOSPath():
	cmder = 'C:\cmderBox\cmder'
	openssh = 'C:\cmderBox\openssh_bin'
	add_path(cmder + ";" + 	openssh,"system")


	
	
def Logo():
	l1 = '                    _                ____'
	l2 = '  ___ _ __ ___   __| | ___ _ __     | __ )  _____  __'
	l3 = ' / __| \'_ ` _ \ / _` |/ _ \ \'__|____|  _ \ / _ \ \/ /'
	l4 = '| (__| | | | | | (_| |  __/ | |_____| |_) | (_) >  <'
	l5 = ' \___|_| |_| |_|\__,_|\___|_|       |____/ \___/_/\_\\'
	print(l1)
	print(l2)
	print(l3)
	print(l4)
	print(l5)
	print '			version: 1.3'
	print '		    By:coding Q2420498526'
	print '		Abandon Cmd,Hug Cmder-Box ~'
	print ' 		Cmder-Box Please wait while installing.....'


	
class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        #print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
 
	
	
if __name__ == '__main__':
	Logo()
	TOPath = 'C:\cmderBox'
	mkdir(TOPath)
	os.rename(".\data",'.\data.zip')
	#解压资源函数
	f = zipfile.ZipFile(".\data.zip",'r')
	for file in f.namelist():
		f.extract(file,TOPath)
	if f != None:
		f.close()
	os.rename(".\data.zip",'.\data')
	setOSPath()
	bar = ProgressBar(total = 20)
	for i in range(20):
		bar.move()
		bar.log('We have arrived at: ' + str(i + 1))
		time.sleep(1)
	print ''
	# 绿色字体
	#print('\033[1;32m' + 'INFO: ' + '\033[0m'+'Cmder-Box Successful installation!')
	print('Cmder-Box Successful installation!')
	print('info: Press the win and R keys and enter cmder to start')
	
	os.system('pause')