import cgi

params = cgi.FieldStorage()
x = int(params.getfirst('x', 0))

print('Content-type: text/html\n')

black = True
result = '<table border="1px">'

for i in range(x):
    result += '<tr>'
    for celula in range(x):
        if black:
            bgcolor = 'black'
        else:
            bgcolor = 'white'

        result = '<td width="60px" height="60px" bgcolor={}></td>'.format(bgcolor)
        black = not black

    if x % 2 == 0:
        black = not black
    result += '</tr>'
result += '</table>'

print(result)