
from Tkinter import *
from tkMessageBox import *
from random import *
#import splashscreen
import sqlite3
root1=Tk()
root1.geometry("1100x500")

root1.title("BSF DATABASE SYSTEM")
root1.configure(background="black")
photo=PhotoImage(file="1.gif")
Label(root1,image=photo).grid()
def fun():
    root1.destroy()
    fun1()
def login():
    new=Tk()
    new.title("Login Window")
    Label(new,text="Enter Username").grid(row=0,column=0,padx=5,pady=5)
    Label(new,text="Enter Password").grid(row=1,column=0,padx=5,pady=5)
    username=Entry(new)
    username.grid(row=0,column=1)
    password=Entry(new,show="*")
    password.grid(row=1,column=1)
    def check():
        if(str(username.get())=="rohan" and str(password.get())=="1234"):
            fun()
            new.destroy()
        else:
            showerror("Login Failed","Invalid Credentials")
    Button(new,text="Login",fg="red",bd=6,font="times 10 bold italic",command=check).grid(columnspan=2)
Button(root1,text="Login Window",fg="red",bd=6,font="times 15 bold italic",command=login).grid(pady=20,sticky=S,row=0,column=0)

def fun1():
    root=Tk()
    conn=sqlite3.connect("Information")
    cur=conn.cursor()
    cur.execute("create table if not exists info(ID varchar,FIRST_NAME varchar(10),LAST_NAME varchar(20),PHONE number(10),EMAIL_ID varchar(10),AGE number(3),ADDRESS varchar(40),RANK varchar(10))")
    fields=["ID","First Name","Last Name","Phone","Email Id","Age","Address","Rank"]
    cur.fetchall()

    entries={}
    global IDEntry
    IDEntry=StringVar()
    IDEntry.set( "" )

    
    for i in range(len(fields)):
        Label(root,text=fields[i]+":").grid(row=i+1,column=0)
        entry=Entry(root,name=fields[i].lower(),font="Courier 12",width=14)
        entry.grid(row=i+1,column=1,padx=5,sticky=N+W+E+S)
        if fields[i]=="ID":
            entry.config(state=NORMAL,textvariable=IDEntry,bg="Yellow")
            entry.insert(0,IDEntry)
            entry.config(state=DISABLED)
        key=fields[i].replace(" ","_")
        key=key.upper()
        entries[key]=entry
        


    def aboutbsf():
        root4=Toplevel()
        root4.title("About BSF")
        root4.geometry("750x500")
        root4.configure(background="White")
        Label(root4,text="The Border Security Force (BSF) is the primary border guarding force of India.It is one of the five Central Armed Police Forces").pack()
        Label(root4,text=" of the Union of India,it was raised in the wake of the 1965 War on 1 December 1965,for ensuring the security of the borders").pack()
        Label(root4,text="of India and for matters connected there with It is a Central Armed Police Force charged with guarding India's land border").pack()
        Label(root4,text="during peacetime and preventing transnational crime It is a Union Government Agency under the administrative control of Ministry").pack()
        Label(root4,text="of Home Affairs.The BSF has its own cadre of officers but its head,designated as a Director-General (DG),since its raising has been").pack()
        Label(root4,text="an officer from the Indian Police Service. It is an Armed Force of the Union of India tasked with various assignments from time to").pack()
        Label(root4,text="time. The BSF has grown exponentially from a few battalions in 1965, to 186 battalions with a sanctioned strength of 257,363 personnel").pack()
        Label(root4,text="including an expanding air wing marine wing, artillery regiments, and commando units.It currently stands as the world's largest ").pack()
        Label(root4,text="border guarding force. BSF has been termed as the First Line of Defence of Indian Territories.").pack()
        

    def add():
        k=entries["FIRST_NAME"].get()
        s=entries["LAST_NAME"].get()
        k1=entries["AGE"].get()
        k2=entries["ADDRESS"].get()
        k3=entries["RANK"].get()
        
        if k!="" and s!="" and k3!="":
            
            query="Insert into info(FIRST_NAME,LAST_NAME,PHONE,EMAIL_ID,AGE,ADDERSS,RANK) values (entries['ID'].get(),entries['FIRST_NAME'].get(),entries['LAST_NAME'].get(),entries['PHONE'].get(),entries['EMAIL_ID'].get(),entries['AGE'].get(),entries['ADDRESS'].get(),entries['RANK'].get())"
            #query=query[:-2]+")"
            
            try:
                conn=sqlite3.connect("Information")
                cur=conn.cursor()
                v=entries["ID"].get()
                
                
                t=entries["FIRST_NAME"].get()
                p=entries["LAST_NAME"].get()
                f=entries["PHONE"].get()
                z=entries["EMAIL_ID"].get()
                u=entries["AGE"].get()
                g=entries["ADDRESS"].get()
                w=entries["RANK"].get()
                a=(v,t,p,f,z,u,g,w)
                cur.execute("Insert into info (ID,FIRST_NAME,LAST_NAME,PHONE,EMAIL_ID,AGE,ADDRESS,RANK) values (?,?,?,?,?,?,?,?)",a)
                conn.commit()
                showinfo(title="Done",message="Information Added")
            except sqlite3.Error as message:
                errorMessage=message.args[0]
                showerror("error",errorMessage)
                
            else:
                cur.close()
                conn.close()
                clearContents()
        else:
            showwarning("Missing fields","Please enter all information")

    def showAll():
        try:
            root2=Toplevel()
            root2.title("All Information")
            connection=sqlite3.connect("Information")
            connection.text_factory=str
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM info")
            #for row in cursor.execute("SELECT * FROM info"):
            a=cursor.fetchall()
            
            def showInfo():
                root1=Toplevel()
                root1.title("Contact Details")
                j = 1
                for j in range (8):
                    Label(root1,text=str(fields[j])+":  "+str(a[(int)(v.get())][j])).pack(anchor=W)
            v=StringVar()
            v.set("l")
            for i in range (len(a)):
                j=a[i][1]
                Label(root2,text=str(i+1)+". ").grid(row=i,column=0)
                b=Radiobutton(root2,text=j,padx=20,variable=v,value=i,command=showInfo,indicatoron=0).grid(row=i,column=2,columnspan=20,padx=10,sticky=N+S+W+E,pady=10)
                
            
        except sqlite3.OperationalError as message:
                errorMessage=message.args[0]
                showerror("error",errorMessage)
                    
    def find():
        if entries["FIRST_NAME"].get()!="":
            #query="SELECT * FROM info WHERE FIRST_NAME = '"+entries["FIRST_NAME"].get()+"'"
            
            try:
                connection=sqlite3.connect("Information")
                cursor=connection.cursor()
                t=(entries["FIRST_NAME"].get(),)
                cursor.execute("SELECT * FROM info WHERE FIRST_NAME = ? ",t)
            except sqlite3.OperationalError as message:
                errorMessage=message.args[0]
                showerror("error",errorMessage)
            else:
                results=cursor.fetchall()
                fields=cursor.description
                if not results:
                    showinfo("Not found","Nonexistent record")
                else:
                    clearContents()
                    for i in range(len(fields)):
                        
                        if fields[i][0]=="ID":
                            IDEntry.set(str(results[0][i]))
                        else:
                            entries[fields[i][0]].insert(INSERT,str(results[0][i]))
                cur.close()
                conn.close()
        else:
            showwarning("Missing fields","please enter first name")

    def update():
        
        if entries["FIRST_NAME"].get():
            entryItems=entries.items()
            
            query="UPDATE info SET "
            for key,value in entryItems:
                if key!="ID":
                    query+="%s='%s'," %(key,value.get())
            query=query[:-1]+" WHERE ID='%s'"%(IDEntry.get())
            
            try:
                conn=sqlite3.connect("Information")
                conn.text_factory=str
                cur=conn.cursor()
                cur.execute(query)
                conn.commit()
            except sqlite3.OperationalError as message:
                errorMessage=message.args[0]
                showerror("error",errorMessage)
                clearContents()
            else:
                showinfo("database updated","Database Updated.")
                cur.close()
                conn.close()
        else:
            showwarning("No ID specified","""you may only update\nan existing record\nuse Find to locate the record,\nthen modify the information and press Update.""")
    def clearContents():
        global  IDEntry
        for entry in entries.values():
            entry.delete(0,END)
        IDEntry.set("")
        for i in range(len(fields)):
            if fields[i]=="ID":
                IDEntry=StringVar()
                IDEntry.set("")
                entry.config(state=NORMAL,textvariable=IDEntry,bg="gray")
                entry.insert(0,IDEntry)
                entry.config(state=DISABLED)
    def reset():
        try:
                connection=sqlite3.connect("Information")
                cursor=connection.cursor()
                askquestion("Delete", "Are You Sure?", icon='warning')
                if 'yes':
                    cursor.execute("DELETE FROM info")
                else:
                    showinfo(title="Warning",message="info. not deleted")
                connection.commit()
        except sqlite3.OperationalError as message:
                errorMessage=message.args[0]
                showerror("error",errorMessage)
                clearContents()
   

    def HelpMe():
        showinfo("HELP","""     CLICK Find To locate a record
            Click ADD to insert a new record.
            Click Update to update the information in a record.
            Click Clear to empty the Entry fields. \n""")
    

    root.title("Soldiers Information")
    Button(root,text="About B.S.F     ",command=aboutbsf,bg='#A9A9A9',font='times 15 bold italic',bd=5).grid(row=0,column=0,sticky=N+E+W+S,padx=0,columnspan=3)
    Button(root,text="Add Info. ",command=add,bg='#DAA520',bd=5).grid(row=0,column=2,sticky=N+E+W+S,padx=0,columnspan=1)
    Button(root,text="Find",command=find,bg='#DAA520',bd=5).grid(row=1,column=2,sticky=N+E+W,padx=0)
    Button(root,text="Show Info.",command=showAll,bg='#DAA520',bd=5).grid(row=2,column=2,sticky=N+E+W,padx=0)
    Button(root,text="Update",command=update,bg='#DAA520',bd=5).grid(row=3,column=2,sticky=N+E+W+S,padx=0,columnspan=1)
    Button(root,text="Clear",command=clearContents,bg='#DAA520',bd=5).grid(row=4,column=2,sticky=N+E+W+S,padx=0,columnspan=1)
    Button(root,text="Help",command=HelpMe,bg='#DAA520',bd=5).grid(row=5,column=2,sticky=N+E+W+S,padx=0,columnspan=1)
    Button(root,text="Delete All Record",command=reset,bg='#DAA520',bd=5).grid(row=6,column=2,sticky=N+W+E+S,padx=0,columnspan=1)
    
    
                        
                        



mainloop()
