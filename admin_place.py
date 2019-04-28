from tkinter import *
from tkinter import messagebox
ch_count = 0
def admin_stage(data):

	def clean(key):
		if key == 0:
			text.pack_forget()
			change_Password.pack_forget()
			Add_User.pack_forget()
			restrictions.pack_forget()


	text = Label(text="admin menu")
	def ch_pswd():
		clean(0)
		text_change = Label(text="change Password")
		text_old_pswd = Label(text="Old Password")
		old_pswd = Entry(show = "*")
		text_new_pswd = Label(text="New Password")
		new_pswd = Entry()
		text_new_pswd_c = Label(text="New Password Copy")
		new_pswd_c = Entry(show = "*")
	
		def change():
			global ch_count
			if ch_count != 0:
				global information
				information.pack_forget()
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
					ch_count +=1
					information = Label(text="password changed")
					information.pack()
				else:
					ch_count +=1
					information = Label(text="new passwords do not match")
					information.pack()
					print('Новые пароли не совпадают')
			else:
				ch_count +=1
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

		#функция для возврата к предыдущему меню
		def back():
			text_change.pack_forget()
			text_old_pswd.pack_forget()
			old_pswd.pack_forget()
			text_new_pswd.pack_forget()
			new_pswd.pack_forget()
			text_new_pswd_c.pack_forget()
			new_pswd_c.pack_forget()
			button_change.pack_forget()
			butt_back.pack_forget()
			admin_stage(data)
		butt_back = Button(text="Back", command = back)
		butt_back.pack()


	change_Password = Button(text="change Password",command=ch_pswd)

	def add_user():
		clean(0)
		text_add = Label(text="add new user")
		name_user = Entry()
		def add():
			temp = name_user.get()
			f = open('text.txt','r')
			fData = f.read()
			f.close()
			if (temp not in fData):
				data_arr = [temp,'']	
				f = open('text.txt','a')
				f.write(str(data_arr)+'\n')
				f.close()
			else:
				print('Повтор данных')

		text_add.pack()
		name_user.pack()
		butt_add = Button(text = "add", command=add)
		butt_add.pack()
		def back():
			text_add.pack_forget()
			name_user.pack_forget()
			butt_add.pack_forget()
			butt_back.pack_forget()
			admin_stage(data)
		butt_back = Button(text="Back", command = back)
		butt_back.pack()

	Add_User = Button(text="Add_User",command=add_user)
	def limits():
		clean(0)
		text_lim = Label(text="limited password or banned users")
		text_lim.pack()
		f = open('text.txt')
		fp = open('permission.txt')
		fbanned = open('banned users.txt')
		fBd = fbanned.read()
		fpd = fp.read()
		diction = {}
		temp = []
		for line in f:
			i = line.index(',')
			temp += [line[1:i]]
		for line in temp:
			
			if (line in fpd) and (line in fBd) :
				diction[line] = 'pb'
			elif (line in fpd):
				diction[line] = 'p'
			elif (line in fBd):
				diction[line]='b'
			else:
				diction[line]=''
		f.close()
		fp.close()
		fbanned.close()
		listbox = Listbox(height=5,selectmode=EXTENDED)
		for i in diction.keys():
			listbox.insert(END,"["+i +"]"+ ":" + diction[i])
		listbox.pack()

		text_name = Label(text= "Username for actions")
		text_name.pack()

		form_username = Entry()
		form_username.pack()

		def lock_unlock():
			f = open('permission.txt' ,'r')
			fData = f.read()
			
			temp = [form_username.get()]

			if (str(temp) in fData):
				f.close()
				f = open('permission.txt','w')
				fData = fData.replace(str(temp),'')
				f.write(fData)
				f.close()
			else:
				f.close()
				f = open('permission.txt','a')
				f.write(str(temp))
				f.close()

			butt_back.pack_forget()
			butt_ban_unban.pack_forget()
			butt_lock_unlock.pack_forget()
			text_name.pack_forget()
			listbox.pack_forget()
			form_username.pack_forget()
			text_lim.pack_forget()
			limits()

		butt_lock_unlock = Button(text="lock / unlock", command = lock_unlock)
		butt_lock_unlock.pack()



		def ban_unban():
			f = open('banned users.txt' ,'r')
			fData = f.read()
			f.close()
			temp = [form_username.get()]

			if (str(temp) in fData):
				f = open('banned users.txt','w')
				fData = fData.replace(str(temp),'')
				f.write(fData)
				f.close()
			else:
				f = open('banned users.txt','a')
				f.write(str(temp))
				f.close()

			butt_back.pack_forget()
			butt_ban_unban.pack_forget()
			butt_lock_unlock.pack_forget()
			text_name.pack_forget()
			listbox.pack_forget()
			form_username.pack_forget()
			text_lim.pack_forget()
			limits()


		butt_ban_unban = Button(text="ban/unban", command = ban_unban)
		butt_ban_unban.pack()

		def back():
			butt_back.pack_forget()
			butt_ban_unban.pack_forget()
			butt_lock_unlock.pack_forget()
			text_name.pack_forget()
			listbox.pack_forget()
			form_username.pack_forget()
			text_lim.pack_forget()
			admin_stage(data)


		butt_back = Button(text="Back", command = back)
		butt_back.pack()


	restrictions = Button(text="Restrictions",command=limits)
	text.pack()
	change_Password.pack()
	Add_User.pack()
	restrictions.pack()
