import sqlite3

connection = sqlite3.connect('contacts.db')

cursor = connection.cursor()
# Creăm tabelul
sql = '''
create table if not exists contacte (
name text,
tel text
);
'''
cursor.execute(sql)

while True:
   
    action = int(input('Introduceți acțiunea (1-adăugare, 2-afișare, 3-modificare, 4-stergere 0-ieșire): '))
      
    if action == 0:
        break

    if action == 1:
        print('ADĂUGARE')
        name = input('Introduceți numele abonatului: ')
        phone = input('Introduceți numărul de telefon: ')

        cursor.execute('''insert into contacte values ("{}","{}");'''.format(name,phone))
        # Salvăm modificările
        connection.commit()
        print('Contactul este adaugat cu succes.')
    if action == 2:
        cursor.execute('select * from contacte')
        x = cursor.fetchall()
        for i in x:
            print('{}:{}'.format(i[0],i[1]))
        print()
    if action == 3:
        print('MODIFICARE')
        name_mod_0 = input('Introduceți numele vechi abonatului: ')
        phone_mod_0 = input('Introduceți numărul vechi de telefon: ')
        name_mod_1 = input('Introduceți numele nou abonatului: ')
        phone_mod_1 = input('Introduceți numărul nou de telefon: ')

        cursor.execute('''update contacte set name='{}' where name='{}';'''.format(name_mod_1,name_mod_0))
        # Salvăm modificările
        connection.commit()
        cursor.execute('''update contacte set tel='{}' where tel='{}';'''.format(phone_mod_1,phone_mod_0))
        connection.commit()
        print('Contactul a fost modificat cu succes.')
    elif action == 4:
        print('STERGERE')
        name = input('Introduceți numele vechi abonatului: ')
        cursor.execute('''delete from contacte where name = '{}';'''.format(name))
        connection.commit()
        print('Contactul a fost sters cu succes!')
    
# Închidem conexiunea cu BD
connection.close()
print('STOP')