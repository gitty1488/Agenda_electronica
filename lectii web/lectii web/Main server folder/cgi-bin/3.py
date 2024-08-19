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
x = params.getfirst('x', '')
y = [int(num.strip()) for num in x.split(',')]

minim = y[0]
maxim = y[1]

for i in y:
    if i < minim:
        minim = i
    if i > maxim:
        maxim = i
print('Lista numerelor eeste: {} \n<br> Numarul maxim: {} \n<br> Numarul minim: {}'.format(x, minim, maxim))


print('''
</table>
</body>
</html>
''')