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

params = cgi.FieldStorage()
n = int(params.getfirst('n', 0))

value = 0
for celula in range(n):
    print('<tr>')
    for cifra in range(n):
        value += 1
        print('<td>{}</td>'.format(value))
    print('</tr>')

print('''
</table>
</body>
</html>
''')