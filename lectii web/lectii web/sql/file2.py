# Importarea bibliotecii care "știe" să lucreze cu BD SQLite
import sqlite3
# Conectarea la BD. Referința la obiectul de conexiune este atribuită unei variabile.
# Dacă BD nu există, aceasta va fi creată automat.
connection = sqlite3.connect('data2.db')
# Creăm un obiect-cursor. Acesta știe să execute interogări SQL.
cursor = connection.cursor()
# Creăm tabelul
sql = '''
create table if not exists users4 (
fio text,
age integer
);
'''
cursor.execute(sql)
# Adăugăm înregistrări
cursor.execute('insert into users4 values("alex", 14)')
cursor.execute('insert into users4 values("bob", 16)')
# Salvăm modificările
connection.commit()
# Afișăm setul de date (nu încarcă întreaga tabelă în memoria operativă, deoarece
# aceasta poate fi foarte mare)
cursor.execute('select * from users4')
# Încărcăm întreaga tabelă și o atribuim unei variabile
x = cursor.fetchall()
print(x)
# Închidem conexiunea cu BD
connection.close()
