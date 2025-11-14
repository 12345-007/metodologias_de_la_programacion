cars=['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':         #car == 'bmw': "esto es una condicion"
        print(car.upper())
    else:
        print(car)

# el condicional es el corazon de un if
# condicional 
car = "bmw"
print(car=='bmw') #true
# condicional false
car = 'audi'
print(car=='Audi') #false
# mayusculas y minusculas importan

# posible solucion a entradas de ususario 
car = 'Audi'
print(car.lower()=='audi') #true

# operador relacional != para determinar desigualdad
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': #true 
    print("Hold the anchovies!")


# comparaciones numericas 
age=18
print(age==18) #true

answer=17
if answer!=42: #true
    print("esta no es la respuesta correcta. intentalo otra ves.")

age = 17 
print(age<21) #true
print(age<=21) #true
print(age>21) #false
print(age>=21) #false

# multiples condiciones 
age_0 = 22
age_1 = 18

#operacion and
print(age_0 >= 21 and age_1 >= 21) #falce 
print(age_0 >= 21 and age_1 >= 18) #true

#operacion or
print(age_0 >= 21 or age_1 >= 21) #true
print(age_0 >= 21 or age_1 >= 21) #falce


"""
para preguntarnos si un valor especifico 
esta en una lista, podemos utilizar el siguiente comparador:

value not in list 'al agregar el not  ejem:2
"""
motorcycles=['mortalica', 'honda', 'vento', 'yamaha']
moto_charly_wants = 'italica'
print(moto_charly_wants in motorcycles) #falce
print('honda' in motorcycles) 

#ejem:2
banned_students=['jorge','carlos','moyra','gus', 'hots']
user= "mauro"
print(user not in banned_students) # true
print('jorge' not in banned_students) #false

## variables del tipo booleano
game_activate = True
can_edit= False 

#examen el 28 de este mes 


"""if statement

sintax:

    if condition:
        do something

    if condition:
        do something
    else:
        do something
"""

age = int(input("\n ¿dime cual es tu edad? "))
print (age)

if age>=18:
    print("tu tienes la edad para votar")
else:
    print("eres menor de edad puto")







