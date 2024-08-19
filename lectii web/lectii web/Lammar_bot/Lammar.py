import requests
import json

x = requests.get('https://api.telegram.org/bot7427794164:AAHWVHeH7k2Tvwo6fUp8yEkQ6DniOcx90u0/getUpdates')

response = x.text

response = json.loads(response)
result = response['result']

first_message = result[0]
message = first_message['message']
id_message = message['message_id']
first_message1 = first_message['message']
text = first_message1['text']
chat = first_message1['chat']
id_chat = chat['id']
#print(result[0])

id_message_request = int(input('Introduceti idul mesajului care toriti sa fie afisat:'))
for mesaj in result:
    message = mesaj['message']
    text = message['text']
    chat = message['chat']
    id_message = message['message_id']
    if id_message == id_message_request:
        print('Mesajul:', text)
        print('Id-ul mesajului:', id_message)
        print('Id-ul chatului:', id_chat)
    

# print('Mesajul:', text)
# print('Id-ul mesajului:', id_message)
# print('Id-ul chatului:', id_chat)
# result['message'] = 'hello'
# print(result['message'])