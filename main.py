from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Treeview
from matplotlib.pyplot import title
import dao.phone as phone


def home():
    global ph,name,phoneno
    
    
    
    ph = Tk()
    ph.title("phone book")
    ph.geometry("500x500")
    ph.minsize(500,500)
    ph.maxsize(500,500)
    
    name = StringVar(ph)
    phoneno = StringVar(ph)
    
    Label(ph,text="PHONE BOOK",font="arial 40",bg="gray",width=13).place(x=1)
    
    Label(ph,text="Name :",font="arial 10").place(x=50,y=100)
    Entry(ph,relief="solid",bd=1,textvariable=name).place(x=110,y=100)
    
    Label(ph,text="Phone :",font="arial 10").place(x=50,y=130)
    Entry(ph,relief="solid",bd=1,textvariable=phoneno).place(x=110,y=130)
    
    def add():
        phone.savephno(name.get(),phoneno.get())
        for i in t.get_children():
            t.delete(i)
        
        phnoinfodata = []
        
        for data in phone.getallphno():
            phnoinfodata.append((data[1],data[2]))

        for d in phnoinfodata:
            t.insert('',END,values=d)

        messagebox.showinfo(ph,"add successfuly!!!")
        
    def fetch():
        for itm in t.selection():
            i = t.item(itm)
            data = i['values']
            name.set(data[0])
            phoneno.set(data[1])
        
        # last stop

    def update():
        if messagebox.showwarning("confirm","confirm update this contect no"):
            phone.updatephno(name.get(),phoneno.get())
            messagebox.showinfo("successfuly!!!","contect update success")
        else:
            messagebox.showinfo("cancal","update cancal")

    def delete():
        if messagebox.showwarning("confirm","confirm delete this contect ?"):
            phone.deletephno(phoneno.get(),name.get())
            messagebox.showinfo("deleted","delete success!!")
        else:
            messagebox.showinfo("cancal","delete cancal")
    

    # show data inside trree view 
    phnoinfodata = []
    
    for data in phone.getallphno():
        phnoinfodata.append((data[1],data[2]))
    
    # messagebox.showinfo(ph,phnoinfodata)        
    

    col =("name","phone no")
    global t
    t = Treeview(ph,columns=col,show="headings")
    t.heading("name",text="Name ")
    t.heading("phone no",text="Phone No")
    t.place(x=45,y=220)  
    
    for d in phnoinfodata:
        t.insert('',END,values=d)
    
    
    Button(ph,text="add",relief="solid",bd=1,command=add).place(x=60,y=170)
    Button(ph,text="Update",relief="solid",bd=1,command=update).place(x=110,y=170)
    Button(ph,text="Delete",relief="solid",bd=1,command=delete).place(x=170,y=170)
    Button(ph,text="fetch",relief="solid",bd=1,command=fetch).place(x=225,y=170)

    
    ph.mainloop()

home()
    