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
