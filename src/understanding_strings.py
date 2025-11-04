"""
un string es de manera cencilla una serie de caracteres.
en python todo lo que se encuentre dentro de comillas simples 
o dobles comillas es considerado un string.

     "esto es un string"
    'esto tambien es un string'

    'le dije a un amigo, "¡python es mi lenguaje favorito!"'
    "el lenguaje 'python' lleva el por monty python, 
    no por la serpiente"

"""
name= "clase de programacion"
print(name)
print(name.title())
print(name)


"""
un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.

El punto . despues de una variable segida 
del metodo tilde () dise que se tiene que ejecutar 
el metodo tilde () de la variable name.

Todos los metodos van seguidos de parentesis 
por que en ocaciones nesesita informacion adicional 
para funcionar, lo cual iria dentro de los parentesis.
En esta ocacion el metodo title() no requiere informacion adicional para ejecutarse.

"""
print(name.upper())
print(name.lower())



# concatenacion de strings
print("cocatenacion de strings")
first_name= "charly"
last_name= "mercury" 
full_name= first_name + " " + last_name
print(full_name)
print("hola, " + full_name.title() + "!")

# syntax error con strings
message= "una fortalesa de python es su comunidad"
print(message)

message = "una fortalesa de 'python' es su comunidad "
print(message)


# cocantenacion con f-strings
"""
() - parentesis
{} - llaves
[] - corchetes

"""
famous_person= "Emiliano ortiz"
quote= "python is love"

# concatenacion convencional 
message= famous_person + " " + quote
print(message)

# concatenacion con f-strings
message= f"{famous_person} una ves dijo  {quote}"
print(message)

# actividad 
"""
1. elige un personaje famoso y igualalo con una variable strings.
2. elige una frase famosa del personaje e igualala con otra variable string.
3. genera un mensaje con las dos variables utilizando f-strings.
4. imprime el mensaje.

"""
famous_person2= "alfredo valenzuela"
quote2= "nada es imposible"
message2= f"{famous_person2} una ves dijo {quote2}"
print(message2) 

# whitespaces
"""
whitespace se refiere a cualquier caracter que se imprime,
es decir, un tabulador y finales de linea. los whitespaces
se utilizan comun mente para organizar las salidas (prints)
de tal manera que sea mas amigable para leer o ver para los  usuario.

"""
# Ejemplos
print("python")
print("\tpython") # tabulador
print("\t\tpython") # doble tabulador 

# ejemplos salto de linea
print("lenguajes: \npython \nc \njavascript") # salto de linea
print("emiliano")
print("ortiz")

message = """

    esta clase es de programacion
    
    mis compañeros son  buena onda 
    
                            metodologias de la programacion
                            
"""
print(message)


#eliminacion de spacios en blanco
programming_language= " python javascript"
print(programming_language)
print(programming_language.lstrip()) # elimina espacios a la izquierda
print(programming_language.rstrip()) # elimina espacios a la derecha
print(programming_language.strip())  # elimina espacios a ambos lados






 

