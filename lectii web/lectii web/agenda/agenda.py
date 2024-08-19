# Biblioteca cu ajutorul căreia putem lucra cu baza de date SQLite
import sqlite3
# Ne conectăm la baza de date. Dacă fișierul lipsește, acesta va fi creat automat.
connection = sqlite3.connect('agenda/diary.db')
# Creăm un cursor. Prin acesta putem executa comenzi SQL.
cursor = connection.cursor()
# Așa se execută toate comenzile SQL
#cursor.execute(Aici se introduce comanda SQL)
# Dacă comanda returnează ceva, rezultatul se citește astfel:
#y = cursor.fetchall()
# Dacă comanda SQL modifică conținutul bazei de date, trebuie să salvăm modificările cu
# apelul funcției .commit()
#connection.commit()
# Închidem conexiunea cu baza de date
sql = '''
create table if not exists progress
(
id integer primary key autoincrement,
subject text,
grade integer
);
'''
cursor.execute(sql)
connection.commit()
print('Salut de la Castor!')
print('Ce vreți să faceți?')

while True:
    x = input('fetbet>')
    if x == 'exit':
        break
    if x == 'help':
        print("help – lista de comenzi")
        print("show - arată lista de note")
        print("add [cod materie] [nota] - adaugă înregistrare")
        print("Codurile materiilor:")
        print("m - Matematică")
        print("g - Geometrie")
        print("i - Informatică")
        print("update [id] [nota nouă] - actualizează nota")
        print("del [id] - șterge înregistrare")
        print("exit - ieșire")
        print("show avg")
        print("show group")
    elif x[:4] == 'show':
        if len(x) == 4:

            cursor.execute ('Select * from progress')
            y = cursor.fetchall()

            if len(y) == 0:
                print('Datele inca nu au fost adaugate')
            else:
                for i in y:
                    print('id = {} {} - {}'.format(i[0],i[1],i[2]))

        elif x[5:8] =='avg':

            cursor.execute('select avg(grade) from progress')
            avgnote = cursor.fetchall()
            print('Nota medie eeste: \n', avgnote[0][0])

        elif x[5:10] == 'group':

            cursor.execute('select subject, avg(grade) from progress group by subject')
            avggroup = cursor.fetchall()
            for i in avggroup:
                print('Disciplina:',i[0], '    Nota:',i[1])


    elif x[:3] == 'add':
        scode = x[4]
        subject = None
        if scode == 'g':
            subject = 'Geometria'
        elif scode == 'a':
            subject = 'Algebra'
        elif scode == 'i':
            subject = 'Istoria'
        else:
            print('Disciplina nu a fost adaugata')
            continue
        if len(x) == 8:
            grade = x[6] + x[7]
        else:
            grade = x[6]
    
        cursor.execute('insert into progress(subject,grade) values (?,?)',(subject,grade))
        connection.commit()
        print('ok')
    
    elif x[:6] == 'update':
        z = int(input('Introduceti idul:'))
        y = int(input('Introduceti nota:'))
        cursor.execute('update progress set grade=? where id=? ', (y,z))
        connection.commit()
        print('ok')
    
    elif x[:3] == 'del':
        id_note = x[4:]
        cursor.execute('delete from progress where id=?',(id_note,))
        connection.commit()
        print('ok')
    else:
        print('Comanda nu este in lista!')

    
connection.close()
