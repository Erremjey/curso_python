print("Hola mundo")
print("Nunca"+"pares"+"de"+"aprender")

# Con las comas se añaden espacios automaticamente y con los "+" no.
print("Nunca","pares","de","aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# El separador ' sep="" ' separa la cadena con el caracter indicado.
print("Nunca","pares","de","aprender",sep=", ")

# El separador ' end="" ' actua como salto de linea para PRINT, pero en la terminal se visualiza en una sola linea.
print("Nunca", end="_")
print("pares de aprender")

# visualizacion de valor de variables en PRINT
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:",frase,"Author:",author)
print("\tFrase:",frase,"\n\tAuthor:",author)