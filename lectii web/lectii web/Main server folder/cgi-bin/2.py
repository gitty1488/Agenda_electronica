import cgi
print('''
<!DOCTYPE HTML>
<html>
<head>
 <meta charset="utf-8">
 <title>Sarcina nr.2</title>
</head>
<body>
''')
# Solicitarea obiectului care conține parametrii de intrare
params = cgi.FieldStorage()
# Obținerea valorii parametrului x. Dacă nu există, funcția va returna valoarea transmisă ca al 2-lea parametru de intrare.
x = params.getfirst('x', '')
count_last_zero = 0
for i in range(len(x) - 1, -1, -1):
 if x[i] == '0':
  count_last_zero += 1
 else:
  break
if count_last_zero > 0:
 x = x[0:len(x) - count_last_zero]
print(x)
print('''
</body>
</html>
''')