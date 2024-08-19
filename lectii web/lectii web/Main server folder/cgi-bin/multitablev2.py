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

for lol in range(1, 11):
    print('{} * {} = {}'.format(n, lol, n*lol))
    print('<br>')

print('''
</table>
</body>
</html>
''')