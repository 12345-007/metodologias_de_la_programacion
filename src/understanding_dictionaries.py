# simple diccionario 
alien_0 = {'color': 'green', 'points': 5}

#the simpiest dictionary
alien_1= {'color': 'yellow'}

#accesing values in a diccionary
print(alien_1['color'])
print(alien_0['points'])

# empty dictionary
alien_2 = {}

#modifying values in a dictionary
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

#adding new key-value pairs
alien_2['x_position'] =0
alien_2['y_position'] =25

print(alien_2)

## dictionary to store similar objects
favorite_lenguages = {
    'jen': 'python',
    'sarah': 'c',
    'eduard': 'ruby',
    'gael': 'python',
}
#print(f"sarah favorite language is {favorite_lenguajes['sara']}")


#looping through all key-value pairs
for key, value in favorite_lenguages.items():
    print(f"{key.title()}'s favorite\
lenguage is {value.title()}.")
    
    for key in favorite_lenguages.items():
        print(key)

    for value in favorite_lenguages.values():
        print(value)




"tarea investigar "
"nesting dictionaries"
"listas de diccionario"
"listas en diccionarios"
"diccionarios en diccionarios"
"""metodo get()"""


