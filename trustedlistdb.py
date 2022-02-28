import sqlite3
import pandas as pd
def connt():
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("CREATE TABLE IF NOT EXISTS trusted (ide INTEGER NOT NULL PRIMARY KEY, trustedaddress TEXT, un_list TEXT)")
    conn.commit()
    conn.close()

def insert(trustedaddress, un_list):
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("INSERT INTO trusted VALUES (NULL,?,?)", (trustedaddress, un_list))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("SELECT * FROM trusted")
    books = cus.fetchall()
    conn.commit()
    conn.close()
    return books

def remove(ide):
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("DELETE FROM trusted where ide = ?",(ide,))
    conn.commit()
    conn.close()

def edit(ide,trustedaddress, un_list):
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("UPDATE trusted SET trustedaddress = ?, un_list = ? WHERE ide = ? ",(trustedaddress,un_list, ide))
    conn.commit()
    conn.close()

def search(trustedaddress = "", un_list = ""):
    conn = sqlite3.connect("trusted_list.db")
    cus = conn.cursor()
    cus.execute("SELECT * FROM trusted WHERE trustedaddress = ?, un_list = ?" ,(trustedaddress, un_list))
    result = cus.fetchall()
    conn.commit()
    conn.close()
    return result

def remove(ide):
    conn = sqlite3.connect("trustedlist.db")
    cus = conn.cursor()
    cus.execute("DELETE FROM trusted where ide = ?",(ide,))
    conn.commit()
    conn.close()
'''
dta = sqlite3.connect('trustedlist.db')
query = dta.execute("SELECT * From trusted")
cols = [column[0] for column in query.description]
res = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
'''