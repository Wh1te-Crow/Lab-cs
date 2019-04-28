from tkinter import *
from tkinter import messagebox
alphabet1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "0123456789"
alphabet3 = ",.:;"
counter_change = 0
def check(temp_str):
	flag  = [0,0,0]
	for i in temp_str:
		
		if not(i in (alphabet1+alphabet2+alphabet3)):
			return False

	for i in alphabet1:
		if i in temp_str:
			flag[0] = 1

	for i in alphabet2:
		if i in temp_str:
			flag[1] = 1

	for i in alphabet3:
		if i in temp_str:
			flag[2] = 1

	if flag == [1,1,1]:
		return True
	else:
		return False

def second_stage(data):

	text_change = Label(text="change Password")
	text_old_pswd = Label(text="Old Password")
	old_pswd = Entry(show = "*")
	text_new_pswd = Label(text="New Password")
	new_pswd = Entry()
	text_new_pswd_c = Label(text="New Password Copy")
	new_pswd_c = Entry(show = "*")

	def change():
		global counter_change 
		counter_change += 1
		if counter_change> 1:
			global information
			information.pack_forget()


		f = open('permission.txt','r')
		fData = f.read()
		f.close()

		if( str([data[0]]) in fData):
			if(    check(new_pswd.get()) == False  ):
				information = Label(text="password requirements not met")
				information.pack()
				print('Некоректный новый пароль')
				return 0



		f = open('text.txt','r')
		fData = f.read()
		f.close()

		if (old_pswd.get() == data[1]):
			print('Старый пароль верный')
			if (new_pswd.get() == new_pswd_c.get()):
				
				f = open('text.txt','w')
				print('Новые пароли совпадают')
				
				newData = [data[0],new_pswd.get()]
			
				fData = fData.replace(str(data),str(newData))
		
				f.write(fData)
				f.close()

				information = Label(text="password changed")
				information.pack()
			else:

				information = Label(text="new passwords do not match")
				information.pack()
				print('Новые пароли не совпадают')
		else:
			information = Label(text="old password do not match")
			information.pack()
			print('Новые пароли не совпадают')


	button_change = Button(text="change",command=change)



	text_change.pack()
	text_old_pswd.pack()
	old_pswd.pack()
	text_new_pswd.pack()
	new_pswd.pack()
	text_new_pswd_c.pack()
	new_pswd_c.pack()
	button_change.pack()
