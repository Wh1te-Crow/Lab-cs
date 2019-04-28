from tkinter import *
from tkinter import messagebox
from work_place import *
from admin_place import *
from getting_configuration import *

from cipher import *


root = Tk()
root.geometry("400x200")
root.title("Aplication")
counter = 0
ban_counter = 0
c_help = 0
eror_ = Label()

Salt =  b'G\xa7\xd2N\x04\xaew)\xd4;6\x1f\xef \xef\x7f'

def check_configuration():

	information_dict = get_Config()

	import winreg
	our_TrueDict = {}
	hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Tsykalo")
	regValue = winreg.QueryValue(hKey,"cheker")
	winreg.CloseKey(hKey)
	tempIndex = regValue.find("Public key")
	TrueHash = regValue[:tempIndex]
	regValue=regValue[tempIndex:]

	our_TrueDict['TrueHash'] = int(TrueHash)
	tempIndex = regValue.find('key_n')
	tempKey_ = regValue[16:tempIndex]
	regValue=regValue[tempIndex:]
	our_TrueDict['d'] = tempKey_
	tempIndex = regValue.find('-salt')
	tempKey_=regValue[6:tempIndex-1]
	regValue = regValue[tempIndex+7:-1]
	our_TrueDict['n'] = tempKey_
	

	import hashlib
	information = str(information_dict).encode('utf-8')
	global Salt
	our_TrueDict['salt'] = Salt
	hash = hashlib.pbkdf2_hmac('sha256', information, Salt, 100000)



	New = get_new(hash)

	clear = decrypt(our_TrueDict['TrueHash'],int(our_TrueDict['d']),int(our_TrueDict['n']))

	if int(clear) == int(New):
		return True
	else:
		return False


string_ = "0123456789"
def get_new(hash):
	new_hash = ""
	for i in str(hash):
		if i in string_:
			new_hash += i
	return new_hash


def start_data():

	file_list = ['text.txt','permission.txt','banned users.txt']
	for i in file_list:
		try:
			f=open(i,'r')
		except FileNotFoundError:
			f=open(i,'w')
			if(i == 'text.txt'):
				f.write(str(['admin',''])+'\n')
		f.close()

	text_log = Label(text="Enter Login")
	reg_log = Entry()
	text_password = Label(text="Enter password")
	reg_password = Entry(show = "*")

	def clear(key):
		if ( key ==  0 ):
			text_log.pack_forget()
			reg_log.pack_forget()
			text_password.pack_forget()
			reg_password.pack_forget()
			button_login.pack_forget()
			button_registration.pack_forget()
			butt_help.pack_forget()
			try:
				eror_log.pack_forget()
			except NameError:
				pass
			try:
				help_log.pack_forget()
			except NameError:
				pass
			global ban_counter
			if ban_counter != 0:
				global eror_
				eror_.pack_forget()
	


	def registration():


		data_arr = [(reg_log.get()),(reg_password.get())]
		print(data_arr)
		print('---')
		f = open('text.txt','r')
		data = f.read()

		if (',' not in data_arr[0]) and (not (str(data_arr[0]) in data )):

			print('Зарегистрирован')
			f.close()

			f = open('text.txt','a')
			f.write(str(data_arr)+'\n')
			f.close()

			clear(0)
			second_stage(data_arr)

		else:
			print('Повтор данных при регистрации')

	button_registration = Button(text="registration",command=registration)

	def login():
		data_arr = [(reg_log.get()),(reg_password.get())]
		f = open('banned users.txt','r')
		data = f.read()

		if(str([data_arr[0]]) in data and data_arr[0]!='admin'):
			global ban_counter
			if (ban_counter == 0):
				global eror_
				eror_ = Label(text="the user is blocked")
				eror_.pack()
				ban_counter +=1


			
				
			f.close()
			return 0

		f.close()
		f = open('text.txt','r')
		data = f.read()
		if (data_arr[0]) == 'admin':
			if ((str(data_arr) in data )):
				f.close()
				print('Вход админа')
				clear(0)
				admin_stage(data_arr)
			else:
				global counter
				counter += 1
				if (counter >= 3):
					clear(0)
					global eror_log
					eror_log.pack_forget()
					eror_log = Label(text="multiple wrong password and login combination")
					eror_log.pack()
					

				else:
					if (counter == 1):
						eror_log = Label(text="wrong password and login combination")
						eror_log.pack()
		else:

			if (str(data_arr) in data ):
				f.close()
				print('Данные правильные')
				clear(0)
				second_stage(data_arr)
			else:


				counter += 1
				if (counter >= 3):
					clear(0)

					eror_log.pack_forget()
					eror_log = Label(text="multiple wrong password and login combination")
					eror_log.pack()
					

				else:
					if (counter == 1):
						eror_log = Label(text="wrong password and login combination")
						eror_log.pack()

		f.close()

	button_login = Button(text="login",command=login)


	def help():
		global c_help
		if c_help == 0:
			help_log = Label(text= "Tsykalo fb63, variant 23")
			help_log.pack()
			c_help = 1


	butt_help = Button(text="help",command=help)
	

# отображение окон
	text_log.pack()
	reg_log.pack()
	text_password.pack()
	reg_password.pack()
	button_login.pack()
	button_registration.pack()
	butt_help.pack()

	if not check_configuration():
		clear(0)
		text_log = Label(text="configuration mismatch")
		text_log.pack()

start_data()
root.mainloop()