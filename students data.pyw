from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import mysql.connector


f=tkinter.Tk()
f.geometry('1300x1000')
bg="blue"
fo=('Arail ','25')

fg=('white')
f.title('My Data')
f.config(bg='purple')
fra=Frame(f).grid(row=0,column=0)
Label(fra,text='Student data',font=(fo),bg=bg,fg=fg).grid(row=0,column=1)

svid=IntVar()
svna=StringVar()
svadd=StringVar()


L1=Label(fra,text='Enter Student ID:',font=('arail','20'),fg='red')
L1.grid(row=1,column=1,pady=20)
E1=Entry(fra,bd=5,width=50,textvariable=svid)
E1.grid(row=1,column=2)
         

Label(fra,text='Enter Student Name:',font=('arail','20'),fg='red').grid(row=2,column=1,pady=20)
Ena=Entry(fra,bd=5,width=50,textvariable=svna)
Ena.grid(row=2,column=2)


Label(fra,text='Enter Student Address:',font=('arail','20'),fg='red').grid(row=3,column=1,pady=20)
Ead=Entry(fra,bd=5,width=50,textvariable=svadd)
Ead.grid(row=3,column=2)

def mybuton(selection):
    print("Student id is :", E1.get())
    print("Student name is :" ,Ena.get())
    print("Student address is :", Ead.get())
    
    try:
        con=mysql.connector.connect(
            host='localhost',
            user='Student Data',
            passwd='123456',
            database='  Student Data'
            )
        cur=con.cursor()
        #cur.execute('select version()')
        #data=cur.fetchone()
        #print('Mysql Database version ',data)
        query= (""" CREATE TABLE  Student_Data ( Student_id  int primary key , Student_name   varchar(99) ,Student_address    varchar(180) ) """ )
        cur.execute(query)
        con.commit()
        con.close()
        con.rollback()

    except mysql.connector.Error as e:
        print(e)
        
        





    
Button(fra,text='Insert:',font=('arail','20'),fg='red',command= lambda :mybuton('insert')).grid(row=5,column=1)

Button(fra,text='Update:',font=('arail','20'),fg='red').grid(row=5,column=2)

Button(fra,text='Exit:',font=('arail','20'),fg='red').grid(row=7,column=2,pady=20)

Button(fra,text='Select:',font=('arail','20'),fg='red').grid(row=6,column=1)

Button(fra,text='Delete:',font=('arail','20'),fg='red').grid(row=6,column=2,pady=20)



f.mainloop()


















input('press enter to exit....')
