from win32api import * 
import wmi
import platform
from ctypes import windll
import os

def get_Config():
	def serial_number():
		c = wmi.WMI()
		for item in c.Win32_PhysicalMedia():
			item = str(item)
			temp = item.split('\n')
			for i in temp:
				#print(i)
				if 'SerialNumber' in i:
					i = i.replace('SerialNumber = "','')
					i = i.replace('";','')
					return i.strip()

	information_dict = {}
	information_dict['Тип и подтип клавиатуры'] = [windll.user32.GetKeyboardType(0),windll.user32.GetKeyboardType(1)]
	information_dict['Разрешение экрана']=[GetSystemMetrics(0),GetSystemMetrics(1)]
	information_dict['Дисковые устройства']=GetLogicalDriveStrings().split('\000')[:-1]
	information_dict['Серийный номер']=[serial_number()]
	information_dict['Имя пользователя']=[GetUserName()]
	information_dict['Имя пк']=[platform.node()]

	return information_dict

