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

''')

""
params = cgi.FieldStorage()
x = params.getfirst('x', 0)
y = params.getfirst('y', 0)

z = int(x) + int(y)

print(z)

print('''
</body>
</html>
''')