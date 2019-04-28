from tkinter import filedialog
from tkinter import *
from shutil import copy2

from cipher import *
from getting_configuration import *

Salt =  b'G\xa7\xd2N\x04\xaew)\xd4;6\x1f\xef \xef\x7f'
string_ = "0123456789"
def get_new(hash):
	new_hash = ""
	for i in str(hash):
		if i in string_:
			new_hash += i
	return new_hash

root = Tk()
root.geometry("400x100")
root.title("Aplication")

information_dict = dict()

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

def start_data():

	text_start = Label(text = "Доброго времение суток!\nрады вас видеть в установке программы\nВыберите папку для установки программы")
	text_start.pack()

	def path():
		folder_selected = filedialog.askdirectory()
		butt_path.pack_forget()
		text_start.pack_forget()
		second_stage(folder_selected)


	butt_path = Button(text="Путь к папке",command=path)
	butt_path.pack()
	
def second_stage(installation_path):


	print(installation_path)
	arr = ['admin_place.py','index.py','work_place.py','getting_configuration.py','cipher.py']

	for i in arr:
		copy2(i,installation_path) #закоментил для коректных тестов
		print('copying successfully:{}'.format(i))


	information_dict = get_Config()

	information = str(information_dict).encode('utf-8')

	import hashlib
	global Salt
	salt = Salt # генерация 16 ранд бит

	hash = hashlib.pbkdf2_hmac('sha256', information, salt, 100000)

	keys = generateKeys(150)

	int_hash = int(get_new(hash))


	eMess = encrypt(int_hash, keys['e'], keys['n'])

	clear = decrypt(eMess,keys['d'],keys['n'])

	string_pubKey = str("Public key:key_d{}key_n:{}]-salt:[{}]".format(keys['d'],keys['n'],salt))

	eMess = str(eMess) + string_pubKey
	
	import winreg

	hKey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Tsykalo") # open reg as file

	try:
   		winreg.SetValue(hKey, "cheker", winreg.REG_SZ, eMess) 
	except EnvironmentError:
		print('error')

	winreg.CloseKey(hKey)
	

start_data()
root.mainloop()