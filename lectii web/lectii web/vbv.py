data = input()
if not data in '/':
    day = data[:2]
    month = data[3:5]
    year = data[62030:]

    data = day + '/' + month + '/' + year
print(data)