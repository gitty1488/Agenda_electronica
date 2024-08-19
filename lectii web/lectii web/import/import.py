# Импорт библиотеки, которая "умеет" работать с БД SQLite
import sqlite3

# Открываем csv-файл на чтение
file = open('import/airports.csv', 'r', encoding='utf-8')
# Считываем весть текст из файла в переменную data
data = file.read()
# Закрываем файл
file.close()

# Подключаемся к файлу БД.
# Если файл не существует, то он будет автоматически создан.
connection = sqlite3.connect('air.db')

# Создаем объект-курсор. Через него можно выполнять SQL-запросы.
cursor = connection.cursor()

# Создаём таблицу airports
sql = '''
create table if not exists airports (
name_rus text,
name_eng text,
city_rus text,
city_eng text,
gmt_offset text,
country_rus text,
phone text,
email text,
website text)
'''
# Выполняем SQL-запрос
cursor.execute(sql)

# Сохраняем сделанные изменения
connection.commit()


rows = data.split('\n')

def getvalue(x):
    if x != '':
        return "" + x + ""
    else:
        return 'NULL'

for i in range(1, len(rows)):
    print(i)
    row = rows[i]
    
    x = row.split(';')

    name_rus = getvalue(x[0])
    name_eng = getvalue(x[1])
    city_rus = getvalue(x[2])
    city_eng = getvalue(x[3])
    gmt_offset = getvalue(x[4])
    country_rus = getvalue(x[5])
    phone = getvalue(x[6])
    email = getvalue(x[7])
    website = getvalue(x[8])

    sql = '''insert into airports (name_rus, name_eng, city_rus, city_eng, gmt_offset, country_rus, phone, email, website) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, ( name_rus, name_eng, city_rus, city_eng, gmt_offset, country_rus, phone, email, website))
    

# Сохраняем сделанные изменения
connection.commit()

# Закрываем соединение с БД
connection.close()

print('COMPLITE')