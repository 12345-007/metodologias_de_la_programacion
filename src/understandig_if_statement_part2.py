"""
vamos a realizar un programa que pregunte al ususario 
por su edad y muestre un mensaje diferente segun el rango
de edad en que se encuentre. 
"""
"""
try:
    age = int(input("porfavor, introduce tu edad"))             # el input siempre te regresa un string numeros 

    if age >= 18:
        print("eres mayor de edad")
    elif age < 18:
        print("eres menor de edad")
except:
    print("tuviste un error al ingresar tu edad")

print("hola charly")
"""
age = 18
try:
    print("tuviste un error al ingresar la edad")

    if age > 100:
        print('tienes mas de un siglo de vida')
    elif age >=18 and age <= 100:
        print ("eres mayor de edad")
    elif age <18 and age >= 0:
        print("eres menor de edad")
    else:
       print("tuviste un error ")
except:
    print("hola charly")



"""ejercicio para casa
aser un programa que pregunte la edad de una persona y 
responde lo sigiente:
-si la edad es menor e igual a 4, entonses la entrada es 
gratuita
- si la edad es menor e igual a 18,pero mayor que 4
entonses la entrada cuesta $200
- si la edad es mayor que 18, entonses la entrada cuesta $400
"""

# multiple if
guisos = ['desebrada', 'asado', 'salsa verde', 'pozole']
if "asado" in guisos:
    print('si ay asado')
else:
    print('no hay asado')
if "tamales" in guisos:
    print('si hay tamales')
else:
    print('no ay tamales')
if "salsa verde" in guisos:
    print('si hay salsa verde')
else:
    print('no ay salsa verde')
