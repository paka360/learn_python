import json
import os

data = {"a": 1, "b": 2,}

with open("test.json", "w") as file:
    json.dump(data, file)

with open("test.json", "r") as file:
    loaded = json.load(file)

print(loaded)

contacts = {
    'stephen':{
        'phone_number':'1',
        'email': 'st@gmail.com'
    },
    'john':{
        'phone_number': '2',
        'email': 'jh@gmail.com'
    },
    'ella':{
        'phone_number':'3',
        'email': 'el@gmail.com',
    },
}

with open("phone_book1", "w") as file:
    json.dump(contacts , file)

    

def load_contacts():  
    if os.path.exists("phone_book1.json"):   
        with open ("phone_book1.json", "r") as file:
            phone_book1 = json.load(contacts, file)

    else:
        phone_book1 = {}

load_contacts()