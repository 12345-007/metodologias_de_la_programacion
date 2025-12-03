#problem_1_pasword_classifer

CORRECT_PASSWORD = 

 = 0

while  < :
    password_input= input("ingresa tu contraseña:")
    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    attempts = attempts + 1

if  == :
    print("Account locked")

    print("pasword strengt:, weak")
    print("pasword strengt:, medium")
    print("pasword strengt:, strong")












#problem 2


def shopping_list_processor(initial_items_text, new_item, search_item):
    SEPARATOR = ","

    if initial_items_text.strip() == "":
        print("Error: invalid input")
        return

    if new_item.strip() == "":
        print("Error: invalid input")
        return

    if search_item.strip() == "":
        print("Error: invalid input")
        return

    raw_items = initial_items_text.split(SEPARATOR)
    items_list = [item.strip() for item in raw_items if item.strip() != ""]

    items_list.append(new_item.strip())

    total_items = len(items_list)
    is_in_list = search_item.strip() in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", is_in_list)







#pregunta de rescate 1: 
#las tuplas tienen 
#
#
#
#

#pregunta de recate 2 explica la diferencia entre un siclo for y un ciclo whitle en python:
#el siclo while es un bucle infinito que que solo se puede usar usando un break al final 
#tambien se utilisa el siclo four para implementar o mas vien un requerimiento para que no se
#trave la compu si no lo usas la computadora sete puede travar por eso es bueno usarlo 
#

#menciona al menos dos diferencias entre listas y tuplas y explica cuando conviene usar cada una?
"""
Listas son modificables puedes cambiar, agregar o borrar elementos
Tuplas son inmutables no se pueden modificar después de crearse
Cuando se deve usar cada una de ella
Lista cuando los datos van a cambiarTupla cuando los datos deben permanecer fijos y seguros.
"""

#explica la diferencia entre un siclo for y un siclo while en python y da un ejemplo de situacion donde sea mas natural usar for y otra donde sea mas natural usar ehitle 
"""
for recorre una secuencia con un número conocido de repeticiones
while repite mientras una condición sea verdadera
Ejemplo para for: recorrer una lista de nombres.
Ejemplo para while: repetir hasta que el usuario escriba una contraseña correcta.
"""

# que ventajas tiene usar funciones en un programa ? menciona al menos tres beneficios (legitibilidad reutilizacion y pruevas:)
"""
Legibilidad el código se entiende mejor
Reutilización  puedes usar la función varias veces sin reescribir código.
Pruebas es más fácil probar y detectar errores en partes pequeñas del programa.
"""























