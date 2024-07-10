texto = "Hola Mundo"
print (texto.upper())
print (texto.lower())
print (texto.find("M")) #indice desde 0
print (texto.find("mun")) #case sensitive = -1
nuevoTexto = texto.replace("Mun", "chanchito feliz") #reemplazar
print (texto, nuevoTexto)
print ("Mundo"in texto)



