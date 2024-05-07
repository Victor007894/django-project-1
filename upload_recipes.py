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
    "category": "lanche",
    "description": "O hamburguer que você conhece agora com 3 carnes, bacon e molho stacker.",

    "preparation_steps": """500g de carne moída (patinho, acém, contrafilé ou sua preferência)
                            Sal e pimenta a gosto
                            1 ovo
                            1 colher de sopa de cebola picada (opcional)
                            1 colher de sopa de farinha de rosca (opcional)
                            Azeite para untar""",

    "preparation_time": "60",
    "preparation_time_unit": "Minutos",
    "servings": "1",
    "servings_unit": "Unidade",
    "url": "https://gkpb.com.br/wp-content/uploads/2023/04/BK-celebra-o-Dia-do-Churrasco-com-o-combo-Mega-StackerCheddar-2.0-pela-metade-do-preco.jpg",
}

# -------------CREATE DATA-------------
# db.child("Mega Stacker 3").set(data)

# -------------READ DATA-------------
dados = db.get_etag()
print(dados["value"])
