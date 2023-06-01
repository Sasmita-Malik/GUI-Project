from tkinter import *
#print (dir () )#dir is used to get all attribute avail inside tkinter module.
import  pymysql
def Exit () :
	win.destroy ()




def Login():
	


	x = user.get()
	y = password.get ()
	#print("Admin login user name =",x)
	#print("Admin login password=",y)
	
	conobj = pymysql.connect (host = 'localhost' , user = "root" , password = "")

	curobj = conobj.cursor ()
	
	curobj.execute ('use marchpro;')
	curobj.execute ("Select Auser, Apassword from admin;")
	Adata = curobj.fetchall ()
	 
	for i, j in Adata :
		if i == x and j == y:
			print("Welcome to admin home page")
			def Uadd ():
				def NewUser():
					conobj = pymysql.connect (host = 'localhost' , user = "root" , password = "")
					curobj = conobj.cursor ()
					curobj.execute ('use marchpro;')
					print ('insert into USER values ("' +Uuser.get ()+ '" , "' +Uphno.get ()+ '" , "' +Uvar.get ()+   '");')
		

					curobj.execute ('insert into USER values ("' +Uuser.get ()+ '" ,"' +Uphno.get ()+ '" ,"' +Uvar.get ()+  '");')
		
					conobj.commit ()
					curobj.close ()
					conobj.close ()
					win3.destroy()
				def Exit1 ():
					win3.destroy()
				win3 = Tk ()
				win3.title("User Registration Page")
				win3.geometry("500x500")
				win3.maxsize(height=400,width=500)
				win3.minsize(height=400,width=500)

				Label  (win3 , text= "Enter  User ID" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 20,y= 20)
				Uuser = Entry (win3 , font = ("Bell MT" , 13), bg ="yellow" , fg ="red" )
				Uuser.place (x= 250,y= 20)

				Label  (win3 , text= "Enter Phone Number" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 20,y= 50)

				Uphno = Entry (win3 , font = ("Bell MT" , 13), bg ="yellow" , fg ="red" )
				Uphno.place (x= 250,y= 50)


				Label  (win3 , text= "Select Gender" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 20,y= 80)
				Uvar = Entry (win3 , font = ("Bell MT" , 13), bg ="yellow" , fg ="red" )
				Uvar.place (x= 250,y= 80)

				Button (win3 , text = "Add User" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10" ,command = NewUser).place (x= 130,y= 130)
	
				Button (win3 , text = "Exit" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10",command = Exit1).place (x= 230,y= 130)



				win3.mainloop()




			def Usearch () :
				conobj = pymysql.connect (host = 'localhost' , user = "root" , password = "")
				curobj = conobj.cursor()
				
				curobj.execute ('use marchpro;')
				curobj.execute ('select * from USER  ;')
				userrecord = curobj.fetchall ()
				print(userrecord)

				curobj.close ()
				conobj.close ()
			def Udisplay ():
				
				conobj = pymysql.connect (host = 'localhost' , user = "root" , password = "")
				curobj = conobj.cursor ()
				curobj.execute ('use marchpro;')
				curobj.execute ('select * from USER  ;')
				userrecord = curobj.fetchall ()
				print(userrecord)

				curobj.close ()
				conobj.close ()
				
			def Uexit ():
				win1.destroy()
			win1 = Tk ()
			win1.title("Admin Home Page")
			#win1.geometry("500x500")
			win1.maxsize(height=400,width=500)
			win1.minsize(height=400,width=500)


			Button (win1, text = "Add New User" ,font = ("Bell MT",10),bg = "alice blue" ,fg ="black", height = "2", width = "20" , command = Uadd).place (x= 150,y= 20)

			Button (win1, text = "Search User" ,font = ("Bell MT",10),bg = "alice blue" ,fg ="black", height = "2", width = "20" , command = Usearch).place (x= 150,y= 50)

			Button (win1, text = "Show All Record" , font = ("Bell MT",10),bg = "alice blue" ,fg ="black", height = "2", width = "20" , command = Udisplay).place (x=150,y= 80)

			Button (win1, text = "Exit" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10" , command = Uexit).place (x= 200,y= 180)


			win1.mainloop()



	curobj.close()
	conobj.close()
	
	




def NewAdmin():
	def Submit () :
		'''
		a = Auser.get ()
		b = phno.get ()
		c = Apassword.get ()
		print ("Admin register user name = ",a)
		print ("Admin reg phno = ",b)
		print ("Admin reg password = ",c)
		'''

		conobj = pymysql.connect (host = 'localhost' , user = "root" , password = "")
		curobj = conobj.cursor ()
		curobj.execute ('use marchpro;')
		print ('insert into ADMIN values ("' +Auser.get ()+ '" , "' +phno.get ()+ '" , "' +var.get ()+  '" , "' +Apassword.get ()+ '");')
		

		curobj.execute ('insert into ADMIN values ("' +Auser.get ()+ '" ,"' +phno.get ()+ '" ,"' +var.get ()+ '" , "' +Apassword.get ()+ '");')
		
		conobj.commit ()
		curobj.close ()
		conobj.close ()

	def Reset () :
		pass
	win2 = Tk ()
	win2.title("AdminRegister Page")
	win2.geometry("500x500")

	Label  (win2 , text= "Enter Admin User Name" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 10,y= 20)


	Auser = Entry (win2 , font = ("Bell MT" , 13), bg ="yellow" , fg ="red" )
	Auser.place (x= 250,y= 20)



	Label  (win2 , text= "Enter Phone Number" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 10,y= 50)


	phno = Entry (win2 , font = ("Bell MT" , 13), bg ="alice blue" , fg ="black" )
	phno.place (x= 250,y= 50)


	Label  (win2 , text= "Select Gender" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 10,y= 80)

	var = Entry (win2 , font = ("Bell MT" , 13), bg ="alice blue" , fg ="black" )
	var.place (x=250,y=80)

	'''
	var = StringVar ()
	r1 = Radiobutton (win2 , text = "Male" ,font = ("bold" , 12),bg = "yellow" , fg = "red",value = "male",variable = v)
	r1.grid(row = 10 ,column = 1)
	r2 = Radiobutton (win2 , text = "FeMale" , font = ("bold" , 12),bg = "yellow" , fg = "red", value = "female" ,variable  = v)
	r2.grid(row = 10 ,column = 2)
	'''
	Label  (win2 , text= "Enter Password" , font = ("Bell MT" , 13) ,bg = "blue" , fg = "white" , width = "20" ,height = "1").place (x= 10,y= 110)


	Apassword = Entry (win2 , font = ("Bell MT" , 13), bg ="alice blue" , fg ="black" ,show = "*" )
	Apassword.place (x= 250,y= 110)


	Button (win2 , text = "Submit" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10" ,command = Submit).place (x= 130,y= 160)

	
	Button (win2 , text = "Reset" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10",command = Reset).place (x= 240,y= 160)




	win2 = mainloop()






win = Tk () #Tk () is class and win is object of Tk () class
win.title ("Admin Login Page")
win.geometry ("700x500")
win.maxsize(height=600,width=700)
win.minsize(height=600,width=700)

'''
#win = Tk()
x = Canvas(win, width=40, height=60)
x.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
x.create_line(0, y, canvas_width, y )
'''


Label (win , text = "Admin Login Page" , font = ("Bell MT", 20),width = "30" , height = "2").place (x= 10,y= 10)

Label (win , text = "Enter User ID" , font = ("Bell MT", 13), fg = "black", bg = "alice blue" , width = "20" , height = "1").place (x= 10,y= 100)

user = Entry (win,  font = ("Bell MT", 13) )
user.place (x= 250,y= 100)

Label (win , text = "Enter password" , font = ("Bell MT", 13), fg = "black", bg = "alice blue" , width = "20" , height = "1").place (x= 10,y= 130)

password = Entry (win,  font = ("Bell MT", 13),show = "*")
password.place (x= 250,y= 130)

Button (win , text = "Login" , font = ("Bell MT",10),bg = "deep sky blue" ,fg ="white", height = "2", width = "15" ,command = Login).place (x= 280,y= 170)
Button (win , text = "Exit" , font = ("Bell MT",10),bg = "red" ,fg ="black", height = "2", width = "10",command = Exit).place (x= 180,y= 290)



Button (win , text = "Admin Register" , font = ("Bell MT",10),bg = "blue violet" ,fg ="black", height = "2", width = "25" , command = NewAdmin).place (x= 125,y= 240)








win.mainloop()#mainloop is used to make a framework
