meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso", 
            "CREEPY" : "Algo que puede ser aterrador", 
            "XD" : "Expresion de causar mucha risa", 
            "BRUH" : "Puede expresar algo que ha sido decepcionante",
            "VIBE" : "Algo que puede definir la vibra del ambiente"
            }

word = input("Escribe una palabra que no entiendas:").upper()
if word in meme_dict.keys():
   print(word, ":",meme_dict[word])

else:
    print("Error 404, route to value was not found")
