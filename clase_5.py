name_1 = 'raul'
name_2 = 'jesus'
last_name_1 = 'montero'
last_name_2 = 'justiniano'
name = name_1 +' '+ name_2 +' '+ last_name_1 +' '+ last_name_2
edad = 32
space = '_______________'

# CONCATENAR_________añadir espacios__________________
print(space*3)
print(name_1 + ' ' + last_name_1)
print(name_1 + name_2 +' '+ last_name_1 + last_name_2)
print(name_1 +' '+ name_2 +' '+ last_name_1 +' '+ last_name_2)
print(name)
print(space*5)

# ACCEDER A POCISION_____acceder a los caracteres mediante el indice
print(name[5])
print(name.capitalize())
print(space*5)

# FUNCIONES___________acciones sobre los objetos, no manipulan
print(len(name_1))
print(f"La longitud de Raul es: {len(name_1)}")
print(type(name_1))
print(len(name))
print(space*5)

# METODOS______________acciones que manipulan las cadenas
print(name_1.upper()+" "+name_2.upper())
print(name.count("a"))
print(f""" Su nombre es {name.capitalize()} y tiene {edad} años.
      \nEn su nombre aparece {name.count("a")} veces la letra 'a' y {name.count("o")} veces la letra 'o'
      \n \t Su nombre contiene {len(name)} carácteres.
      \nEsto es mayuscula total: {name.upper()}
      \ny esto es mayuscula solo primera letra: {name.capitalize()} """)
#______________prueba de metodos
print(name.title()) # Pone mayusculas todas las primeras letras
print(name.swapcase()) # pone en mayuscula toda la frase
print(name.replace("raul","Raúl")) # Reemplaza un texto por otro, no modifica el original
print(name_1.split()) #separa o divide cadenas de texto
print(name_1.strip()) # Elimina espacios al principio y final de un texto
print(name_1.lstrip()) 
print(name_1.find("l")) # Busca y devuelve el indice de la letra o palabra, si no hay lanza "-1"
print(name_1.index("a")) # Busca y devuelve el indice de la letra o palabra, si no hay lanza Error. (try/except)