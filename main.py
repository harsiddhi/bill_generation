# from tkinter import *
# from functools import partial
# import mysql.connector
#
# def validateLogin(username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())
# 	username = username.get()
# 	password = password.get()
# 	logintodb(username, password)
#
# 	return
#
#
# def logintodb(user, passw):
# 	# If password is enetered by the
# 	# user
# 	if passw:
# 		db = mysql.connector.connect(host="localhost",
# 									 user='root',
# 									 password='',
# 									 db="python")
# 		cursor = db.cursor()
#
# 	# If no password is enetered by the
# 	# user
# 	else:
# 		db = mysql.connector.connect(host="localhost",
# 									 user='root',
# 									 password='',
# 									 db="python")
# 		cursor = db.cursor()
#
# 	# A Table in the database
# 	savequery = "select * from user"
#
# 	try:
# 		cursor.execute(savequery)
# 		myresult = cursor.fetchall()
#
# 		# Printing the result of the
# 		# query
# 		for x in myresult:
# 			print("user and pass value from user",user,passw)
# 			if(user == x[1] and passw == x[2]):
# 				print("Ues.. Auth")
# 				break;
# 			else:
# 				print("No Auth")
# 		print("Query Executed successfully")
#
# 	except:
# 		db.rollback()
# 		print("Error occured")
# #window
# tkWindow = Tk()
# tkWindow.geometry('400x150')
#
#
# tkWindow.title('Tkinter Login Form - pythonexamples.org')
#
# #username label and text entry box
# usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = StringVar()
# usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
#
# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
#
# validateLogin = partial(validateLogin, username, password)
#
# #login button
# loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
#
# tkWindow.mainloop()

import socket
import sys
ip = socket.gethostbyname('www.google.com')
print(ip)



try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

	# this means could not resolve the host
	print("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")


