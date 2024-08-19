# Импорт библиотеки, которая "умеет" работать с БД SQLite
import sqlite3
# Импорт библиотеки, которая "умеет" открывать сайты в браузере
import webbrowser

# Создаём объект-подключение к БД
connection = sqlite3.connect('air3.db')

# Создаём объект-курсор, через который можно выполнять SQL-запросы
cursor = connection.cursor()

# Пример выполнения SQL-запроса
#cursor.execute('select * from airports')
# Закачиваем все записи в виде двумерного массива и сохраняем его в x
#x = cursor.fetchall()

# ТУТ НУЖНО НАПИСАТЬ СВОЙ АЛГОРИТМ

            
# Закрываем соединение с БД
connection.close()