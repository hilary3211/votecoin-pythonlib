import sqlite3
import pandas as pd
def conn():
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("CREATE TABLE IF NOT EXISTS storage(ide INTEGER NOT NULL PRIMARY KEY, escrow_address TEXT , title TEXT ,question TEXT ,category TEXT)")
    conn.commit()
    conn.close()

def insert(escrow_address, title, question, category):
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("INSERT INTO storage VALUES(NULL,?,?,?,?)", (escrow_address,title,question,category))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("SELECT * FROM storage")
    books = cus.fetchall()
    conn.commit()
    conn.close()
    return books

def remove(ide):
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("DELETE FROM storage where ide = ?",(ide,))
    conn.commit()
    conn.close()

def edit(ide,title,question,category):
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("UPDATE storage SET title = ?, question=?,category=?  WHERE ide = ? ",(title,question,category,ide))
    conn.commit()
    conn.close()

def search(title="",category = ""):
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("SELECT * FROM storage WHERE title= ? OR category = ?" ,(title,category))
    result = cus.fetchall()
    conn.commit()
    conn.close()
    return result

def remove(ide):
    conn = sqlite3.connect("vote.db")
    cus = conn.cursor()
    cus.execute("DELETE FROM storage where ide = ?",(ide,))
    conn.commit()
    conn.close()


conn()
#insert('TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA','something', 'what is something oo', 'community')
'''
dta = sqlite3.connect('vote.db')
query = dta.execute("SELECT * From storage")
cols = [column[0] for column in query.description]
res = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
'''