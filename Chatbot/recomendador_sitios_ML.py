import requests
import random

def classify(text):
    key = "c15dd690-749e-11ec-b689-8174d92278c0b85eb195-6619-4480-a5d2-450c8e865da2"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
def storeTraining(text, label):
    key = "c15dd690-749e-11ec-b689-8174d92278c0b85eb195-6619-4480-a5d2-450c8e865da2"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())

        #
# This function will train a new ML model using the current 
# training examples in your project
#
# key - API key - the secret code for your ML project 
#
def trainModel():
    key = "c15dd690-749e-11ec-b689-8174d92278c0b85eb195-6619-4480-a5d2-450c8e865da2"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/models"

    response = requests.post(url)

    if response.ok == False:
        # if something went wrong, display the error
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
        #respuesta_bot = "no te he entendido, ¿podrias ser mas concreto?"
        respuesta_bot = "no te he entendido, ¿a que te refieres, teatro, fiesta, monumentos o gastronomia?"
        error = 1
        if error == 1:
            print("<bot_recomendador> " + respuesta_bot)
        while contador == 1:
            etiqueta = input(" >")
            #respuesta_bot = "el texto que va aprender es " + usuario_entrada + " y la etiqueta donde lo va a meter es " + etiqueta
            storeTraining(usuario_entrada, etiqueta)
            print("Estoy aprendiendo de nuevo...")
            trainModel()
            print("leccion aprendida!!")
            respuesta_bot = "Vale, acabo de aprender que cuando me dices '" + usuario_entrada + "' te refieres a " + etiqueta
            contador-=1
        
    elif usuario_clasificado == "teatro":
        respuesta_bot = "creo que te gustaria ir al teatro" + " con una probabilidad de " + str(fiabilidad) + "%"
    elif usuario_clasificado == "fiesta":
        respuesta_bot = "creo que te gustaria ir de fiesta" + " con una probabilidad de " + str(fiabilidad) + "%"
    elif usuario_clasificado == "monumentos":
        respuesta_bot = "creo que te gustaria ver monumentos" + " con una probabilidad de " + str(fiabilidad) + "%"
    elif usuario_clasificado == "gastronomia":
        respuesta_bot = "creo que te gustaria disfrutar de la gastronomia" + " con una probabilidad de " + str(fiabilidad) + "%"
        
    
    print(bot_chat + respuesta_bot)
    

print("Hola, soy bot_recomendador, ¿que te gustaria hacer?")


#storeText(key, texto, etiqueta)



while True:
    gustos()