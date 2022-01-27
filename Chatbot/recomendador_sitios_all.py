import requests
import random

key = "23611330-7b74-11ec-ac78-3d4d8310fc4dccb74286-c7a7-46a0-83b0-2f28d9dbbb9c"
url = "https://machinelearningforkids.co.uk/api/scratch/"

def classify(text):
    url_c = url + key + "/classify"

    response = requests.get(url_c, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
def storeTraining(text, label):
    url_c = url + key + "/train"

    response = requests.post(url_c, json={ "data" : text, "label" : label })

    if response.ok == False:
        print (response.json())

def trainModel():
    url_c = url + key + "/models"

    response = requests.post(url_c)

    if response.ok == False:
        print (response.json())

def gustos():
    usuario_entrada = input("> ")
    usuario_clasificar = classify(usuario_entrada)
    usuario_clasificado = usuario_clasificar["class_name"]
    fiabilidad = usuario_clasificar["confidence"]
    respuesta_bot = ""
    bot_chat = "<bot_recomendador> "
    error = 0
    contador=1
    if fiabilidad < 80:
        respuesta_bot = "no te he entendido, ¿a que te refieres, teatro, fiesta, monumentos, gastronomia, saludo, presentacion, comedia, drama, musical, pop, rock, regueton, gotico, barroco, romano, desenlace, carne, pescado o postres?"
        error = 1
        if error == 1:
            print("<bot_recomendador> " + respuesta_bot)
        while contador == 1:
            etiqueta = input(" >")
            storeTraining(usuario_entrada, etiqueta)
            print("Estoy aprendiendo de nuevo...")
            trainModel()
            print("leccion aprendida!!")
            respuesta_bot = "Vale, acabo de aprender que cuando me dices '" + usuario_entrada + "' te refieres a " + etiqueta
            contador-=1
    else:
        print (chatbot.ask_question(usuario_clasificado))
    
    # print(bot_chat + respuesta_bot)
    

print("Hola, soy bot_recomendador, ¿que te gustaria hacer?")


try:
    while True:
        gustos()
except:
    pass  