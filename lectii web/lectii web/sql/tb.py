import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
sql = '''
create table users(login text, psw text)
'''
cursor.execute(sql)
cursor.execute('insert into users values("admin", "123")')
cursor.execute('insert into users values("user", "111")')
connection.commit()
cursor.execute('select * from users')
x = cursor.fetchall()
print(x)
connection.close()