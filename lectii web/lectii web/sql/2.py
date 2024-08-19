import sqlite3
import webbrowser
connection = sqlite3.connect('sql/air3.db')
cursor = connection.cursor()
locations =  {}
cursor.execute('select country_rus from airports')
x = cursor.fetchall()
for i in x:
    country = i[0]
    if country in locations:
        locations[country] += 1
    else:
        locations[country] = 1
#print(x)
print(locations)
connection.close()