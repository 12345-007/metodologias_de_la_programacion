message = "This is my frient python variable" 
another_message = "I am really, really, really happy"

# print() -> use to show messages in terminal 
# print() -> se utilisa para mostrar mensajes en la terminal 
print(message)
print(another_message)
print(message, another_message, message)

message = "I love python"
print(message)

"""
los nombres de variables en python deben nombrarse solo con:

   -letras, numeros y gion bajo (espacios)
   - deben comenzar con una letra o un gion bajo, pero NO con numero:
      ejemplo correcto: messaje_1 (:) )
      ejemplo incorrecto: 1_messaje (x)
   - no utilizar espacios para separar palabras en los nombres de las variables 
   - no utilizar palabras reservadas de python para nombrar variables o archivos
   - deben ser cortos, pero descriptivos
   - deben ser en ingles 
   nombre de las variables en minusculas 
   """
charly_message = " hola soy charly y estoy aprendiendo python"
print(charly_message)
print(charly_message) 

"""
traceback: Es un r4egistro donde le interprete tuvo problemas para ejecutar el codigo 

Traceback (most recent call last):
  File "C:\Users\emili\projects\metodologias_de_la_programacion\src\understanding_variables.py", line 28, in <module>
    print(charly_mesage)
          ^^^^^^^^^^^^^
NameError: name 'charly_mesage' is not defined. Did you mean: 'charly_message'?


NameError: significa que olvidamos obedeser el valor de una variable antes de utilizar o cometimos un error 
al ingresar el nombre de la variable 
"""