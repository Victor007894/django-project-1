from random import randint
from faker import Faker
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyASJYt_bkOZlQyPWUCO0497LFGEgq8EIGI",
    "authDomain": "arquivos-mercadib.firebaseapp.com",
    "databaseURL": "https://arquivos-mercadib-default-rtdb.firebaseio.com",
    "projectId": "arquivos-mercadib",
    "storageBucket": "arquivos-mercadib.appspot.com",
    "messagingSenderId": "983873992370",
    "appId": "1:983873992370:web:f221648b4ec2778633bbab",
    "measurementId": "G-S9M4FLS6FE"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data = {
    "title": "Combo Mega Stacker 3.0",
    "description": "O hamburguer que você conhece agora com 3 carnes, bacon e molho stacker.",
    "preparation_time": "60",
    "preparation_time_unit": "Minutos",
    "servings": "1",
    "servings_unit": "Unidade",
}

dados = db.child("Mega Stacker 3").get().val()

fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'title': dados["title"],
        'description': dados["description"],
        'preparation_time': dados["preparation_time"],
        'preparation_time_unit': dados["preparation_time_unit"],
        'servings': dados["servings"],
        'servings_unit': dados["servings_unit"],
        'preparation_steps': dados["preparation_steps"],
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': dados["category"]
        },
        'cover': {
            'url': dados["url"]
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
