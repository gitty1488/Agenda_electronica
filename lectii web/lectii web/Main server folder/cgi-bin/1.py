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
inv = params.getfirst('inv', '')
result = ''
for i in inv :
    if i.lower()== i :
        result += i.upper() 
    else:
        result += i.lower()
print (result)

print('''
</table>
</body>
</html>
''')