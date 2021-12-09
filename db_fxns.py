from os import name
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Patientstable(name TEXT,id TEXT,diabetis TEXT,heart TEXT,parkinsons TEXT,Hospital TEXT,date DATE)')

def add_data(name,id,diabetis,heart,parkinsons,Hospital,date):
    c.execute('INSERT INTO Patientstable(name,id,diabetis,heart,parkinsons,Hospital,date) VALUES(?,?,?,?,?,?,?)',(name,id,diabetis,heart,parkinsons,Hospital,date))
    conn.commit()
    

def view_all_data():
    c.execute('SELECT * FROM Patientstable')
    data = c.fetchall()
    return data

def view_unique_name():
    c.execute('SELECT DISTINCT name FROM Patientstable')
    data = c.fetchall()
    return data

def get_name(name):
    c.execute('SELECT * FROM Patientstable WHERE name="{}"'.format(name))
    data = c.fetchall()
    return data



def edit_patient_data(new_name,new_id,new_diabetis,new_heart,new_parkinsons,new_Hospital,new_date,name,id,diabetis,heart,parkinsons,Hospital,date):
    c.execute("UPDATE Patientstable SET name = ?,id=?,diabetis=?,heart=?,parkinsons=?,Hospital=?,date=? WHERE name = ? and id=? and diabetis=? and heart=? and parkinsons=? and Hospital=? and date=?",(new_name,new_id,new_diabetis,new_heart,new_parkinsons,new_Hospital,new_date,name,id,diabetis,heart,parkinsons,Hospital,date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(name):
	c.execute('DELETE FROM Patientstable WHERE name="{}"'.format(name))
	conn.commit()
