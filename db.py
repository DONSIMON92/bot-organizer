import os
import sqlite3

conn = sqlite3.connect('multitask.db')
cursor = conn.cursor()

#def create_database():
#    cursor.execute('CREATE TABLE IF NOT EXISTS Persons(user_id INTEGER PRIMARY KEY, name VARCHAR(35))')
#    conn.commit()
def Create_database():                                                                            
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()

def Join(user_id, name):
    cursor.execute(f'INSERT OR IGNORE INTO Users VALUES({user_id}, "{name}")')
    print(f'user start bot|| name: {name}; id: {user_id}')
    conn.commit()

def Verification(user_id):
    cursor.execute(f'SELECT user_id FROM Users WHERE user_id={user_id}')
    response = cursor.fetchall()
    conn.commit()
    if not response:    # если в переменную не записывается id, то функция возвращает False
        return False
    else:
        return True

#def Change(user_id):
#    print('change info about user')

#def Ban(user_id):
#    print('banbanbanban')
