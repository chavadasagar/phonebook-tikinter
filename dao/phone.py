import sqlite3

con = sqlite3.connect("phone.db")


def createTable():
    con.execute("create table if not exists phone(pid INTEGER PRIMARY KEY AUTOINCREMENT,name text,phno text)")
    con.commit()
    
def savephno(name,phno):
    data = (name,phno)
    con.execute("insert into phone(name,phno) values(?,?)",data)
    con.commit()
    
def updatephno(name,phno):
    data = (name,phno,name,phno)
    con.execute("update phone set name=? ,phno=? where name=? and phno=?",data)
    con.commit()
    
# def deletephno(pid):
#     data = (pid)
#     con.execute("delete from phone where pid='"+pid+"'")
#     con.commit()
def deletephno(phno,name):
    data = (phno,name)
    con.execute("delete from phone where phno=? and name=?",data)
    con.commit()    

def getallphno():
    cur = con.execute("select * from phone")
    data = cur.fetchall()
    return data

def getphno(pid):
    cur = con.execute("select * from std where pid='"+pid+"'")
    data = cur.fetchall()
    return data

def search(search):
    cur = con.execute("select * from phone where pid like '%"+search+"%' or name like '%"+search+"%' or phno like '%"+search+"%'")
    data = cur.fetchall()
    return data
    
def clear():
    con.execute("delete from phone where 1=1")
    con.commit()

createTable()

 