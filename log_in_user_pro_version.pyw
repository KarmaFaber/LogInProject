#python modules:---
from tkinter import *
from tkinter import messagebox
from pymysql import *

#my modules:---
from class_sql import *

#root-----------------------------------------------------------
root=Tk()
root.title("Logn In Pro Version: ")
root.geometry("400x200")
root.config(bg="#F5EEE2")

#variables-------
email=StringVar()
#password=StringVar()
#encrypt_pass=StringVar()

#labels------------
lblEmail=Label(root, text="your email: ", bg="#F5EEE2")
lblEmail.config(font=("Courier", 12))
lblEmail.grid(row=3, column=2, padx=10, pady=10)

lblPass=Label(root, text="password: " , bg="#F5EEE2")
lblPass.config(font=("Courier", 12))
lblPass.grid(row=4, column=2, padx=10, pady=10)

#entry (intup box)---------
emailBox=Entry(root, bg="#C6B895", fg="#3C303E")
emailBox.config(font=("Courier", 12))
emailBox.grid(row=3, column=3, padx=10, pady=10)
emailBox.focus()

passBox=Entry(root, bg="#C6B895",show="*", fg="#3C303E")
passBox.config(font=("Courier", 12))
passBox.grid(row=4, column=3, padx=10, pady=10)
passBox.focus()

#btn- function--------------
def logn_in():
     #variables
     email_box=emailBox.get()
     password_box=passBox.get()
     
     try: 
          
          #sql query
          db=pymysql.connect("localhost","root", "", "proyect")
          cursor=db.cursor()
          query="select * from user where email='%s'"%email_box
          cursor.execute(query)

          result=cursor.fetchall()
          for row in result:
               email=row[0]
               password=row[1]
               ("email={0}, password={1}".format(email, password))


          if password_box==password:
               messagebox.showinfo(message="log in OK", title="Log In message :)")
               emailBox.delete(0,END)
               passBox.delete(0,END)
          else:
               messagebox.showinfo(message="log in not OK", title="Log In message :)")
               emailBox.delete(0,END)
               passBox.delete(0,END)



     except TypeError:
          messagebox.showwarning(message="some kind of format error is found: please type your password again", title="Warning")
          passBox.delete(0,END)
     except OperationalError: 
           messagebox.showwarning(message="A connection cannot be established since the destination team expressly denies that connection.", title="Warning")
     except ConnectionRefusedError:
          messagebox.showwarning(message="Error connecting to the database, check your connection to the server and try again.", title="Warning")
     except InternalError:
          messagebox.showwarning(message="Check the connection data to the BD.", title="Warning")
     except IntegrityError:
          messagebox.showwarning(message="Duplicate entry email, use email for sign up or log in.", title="Warning")

#btn---------------
btn=Button(root, text="Log In", command=logn_in, bg="#FB7F64", fg="#3C303E")
btn.grid(row=6, column=2, padx=20, pady=20)
btn.config(font=("Courier", 12))

#close root----
root.mainloop()