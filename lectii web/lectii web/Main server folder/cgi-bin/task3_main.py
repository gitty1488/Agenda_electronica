import cgi
print('''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primul site pentru server!</title>
</head>
<body>
<table>
''')

for i in range(1,11):
    print('<a href="multitablev2.py?n={}">Tabelul inmultirii cu {}</a><br>'.format(i,i))

print('''
</table>
</body>
</html>
''')