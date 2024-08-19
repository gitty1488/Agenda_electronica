import json
x = {'Ana' : 9, 'Alex' : 10, 'Radu' : 8}
z = [1,2,3, 'Hi']
#for cheia in x:
#    print(cheia)
#for values in x.values():
#    print(values)
#for chei, values in x.items():
#    print(chei, ':', values)
print(z)
y = json.dumps(z)
print(y)