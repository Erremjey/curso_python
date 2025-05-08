# DOMINIO DE LA FUNCION "PRINT"
line = "____________________________"
####BLOQUE 1___Funcion "PRINT"
print ("BLOQUE_1",line)
print("Hola mundo")
print("Nunca"+"pares"+"de"+"aprender")

####BLOQUE 2___Con las comas se añaden espacios automaticamente y con los "+" no.
print ("BLOQUE_2",line)
print("Nunca","pares","de","aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

print("\n")
####BLOQUE 3___El separador ' sep="" ' separa la cadena con el caracter indicado.
print ("BLOQUE_3",line)
print("Nunca","pares","de","aprender",sep=", ")

print("\n")
#####BLOQUE 4___ El separador ' end="" ' actua como salto de linea para PRINT,
#                      pero en la terminal se visualiza en una sola linea.
print ("BLOQUE_4",line)
print("Nunca", end="_")
print("pares de aprender")

print("\n")
####BLOQUE 5___# visualizacion de valor de variables en PRINT
print ("BLOQUE_5",line)
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:",frase,"Author:",author)
print("\tFrase:",frase,"\n\tAuthor:",author)

print("\n")
####BLOQUE 6___# Uso de formato con "format", insertar valores en cadenas de textos 
print ("BLOQUE_6",line)
frase = "Nunca pares de aprender"
author_2 = "Team Platzi"
print("Frase: {}, Autor: {}".format(frase,author_2))

print("\n")
####BLOQUE 7___# Impresión con formato específico, 
#                dar el numero específico de caracteres a imprimir.
print ("BLOQUE_7",line)
valor = 3.14159
print("Valor: {:.2f}".format(valor))

print("\n")
####BLOQUE 8___# Usar barra invertida "\"para especificar texto con comillas,
#                sin que Python interprete como sintaxis,
#                lo mismo con barras invertidas como parte del texto.
print ("BLOQUE_8",line)
print("Mi nombre es 'Raul'")
print("Mi nombre es \'Raul\'")
print("La ruta de acceso es: c:\\User\\raulmj")