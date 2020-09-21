import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def Create_database():
    cursor.execute('CREATE TABLE IF NOT EXISTS Persons(user_id INTEGER PRIMARY KEY, name VARCHAR(35))')
    conn.commit()

def Verification(user_id):
    response = cursor.execute(f'SELECT user_id FROM Persons WHERE user_id={user_id}')
    conn.commit()
    if not response:    # если в переменную не записывается id, то функция возвращает False
        return False
    else:
        return True

def Join(user_id, name):
    cursor.execute(f'INSERT OR IGNORE INTO Persons VALUES({user_id}, "{name}")')
    print(f'user start bot|| name: {name}; id: {user_id}')
    conn.commit()

def Change(user_id, name):
    print('change info about user')

#def Search(user_id):
#    if cursor.execute(f'SELECT * FROM Persons WHERE user_id = {user_id}') != None:
#        print(cursor.execute(f'SELECT * FROM Persons WHERE user_id = {user_id}'))
#        return True
#    else:
#        print(cursor.execute(f'SELECT * FROM Persons WHERE user_id = {user_id}'))
#        return False

def Ban():
    print('banbanbanban')
