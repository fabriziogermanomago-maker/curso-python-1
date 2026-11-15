meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador o siniestro",
    "AGGRO": "Ponerse agresivo o enojado",
    "BRUH": "Expresión de sorpresa o decepción",
    "FLEX": "Presumir algo",
    "GHOSTING": "Dejar de responder a alguien sin explicación",
    "OMG": "Expresión de sorpresa"
}

print("¡Bienvenido al diccionario de palabras modernas!")
print("Escribe una palabra en MAYÚSCULAS para conocer su significado.")
print("Tienes 5 oportunidades para buscar palabras.")

for i in range(5):
    word = input("\nEscribe una palabra: ")

    if word in meme_dict:
        print("Significado:", meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario.")

print("\n¡Gracias por utilizar el diccionario!")
