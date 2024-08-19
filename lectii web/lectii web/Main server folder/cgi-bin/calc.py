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
x = int(params.getfirst('x', 0))
y = int(params.getfirst('y', 0))

t = params.getfirst('type_operation', '')

if t == '+':
    print('{} {} {} = {}'.format(x, t, y, x+y))
elif t == '-':
    print('{} {} {} = {}'.format(x, t, y, x-y))
elif t == '*':
    print('{} {} {} = {}'.format(x, t, y, x*y))
elif t == '/':
    print('{} {} {} = {}'.format(x, t, y, x/y))
else:
    print('Ati introdus operatie inexistenta')

print('''
</body>
</html>
''')