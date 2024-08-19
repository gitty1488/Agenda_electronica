# Importarea bibliotecii pentru a afla ora curentă
from datetime import datetime
import time
import requests
import json

# Funcția va returna orele, minutele și secundele curente ca șir de caractere
def get_current_time():
    current_time = datetime.now().time()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return '{}h {}min {}sec'.format(hour, minute, second)

token = input('Introducti tokenul botului:')
api_url = 'https://api.telegram.org/bot{}'.format(token)

# Cerem să citim mesajele neprocesate începând cu update_id specificat
offset = -1

# Variabilă steag. Dacă utilizatorul introduce cuvântul "stop", terminăm algoritmul
stop = False
print('START')

while True:
    # Dormim timp de 5 secunde
    #time.sleep(5)
    if stop == True:
        break

    # Citim mesajele noi
    x = requests.get('{}/getUpdates?offset={}'.format(api_url, offset))
    # Răspunsul se află în proprietatea .text
    response = x.text
    # Deserializăm răspunsul din șir de caractere
    response = json.loads(response)
    # Mesajele sunt stocate în cheia result
    result = response['result']

    if len(result) == 0:
        continue

    # Iterăm prin mesaje
    for message in result:
        # Pentru a nu citi același mesaj data viitoare, setăm offset-ul
        # ca update_id al mesajului + 1
        offset = message['update_id'] + 1

        # Citim valorile cheii message
        message_value = message['message']
        # Citim mesajul introdus de utilizator
        text = message_value['text']

        if text == 'stop':
            stop = True
            break

        # Dacă utilizatorul a introdus mesajul "time", îi trimitem ora curentă
        if text == 'time':
            # Extragem id-ul chatului
            chat = message_value['chat']
            id_chat = chat['id']

            # Citim id-ul mesajului pentru a trimite
            # mesajul ca răspuns
            message_id = message_value['message_id']

            # Trimitem mesajul cu ora curentă
            requests.post('{}/sendMessage'.format(api_url), data={
                'chat_id': id_chat,
                'text': get_current_time(),
                'reply_to_message_id': message_id
            })

print('STOP')