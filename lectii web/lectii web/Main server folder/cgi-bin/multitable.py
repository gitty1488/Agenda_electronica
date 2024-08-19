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

for cifra in range(1, 11):
    for coef in range(1, 11):

        print('{} * {} = {}'.format(cifra, coef, cifra*coef))
        print('<br>')
    print('<br>')
print('''
</body>
</html>
''')