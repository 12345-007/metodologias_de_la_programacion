# LISTAS 
# una lista es una coleccion ordenada y mutable de elementos.
# se pueden crear listas utilizando los corchetes [] y separando los elementos con comas.
# Ejemplo de creacion de una lista
frutas = ['manzanas','banana','cereza','naranja'] 
print(frutas)  # Salida: ['manzanas', 'banana', 'cereza', 'naranja'] 

print(frutas[0].upper())  # Salida: manzanas
print(frutas[1].title())  # Salida: Banana
print(frutas[2])    # Salida: cereza         
print(frutas[3]) # Salida: naranja     
 
"""
el orden de los elementos al empesar a de isquierda a derecha y el indice empieza en 0.
y al empesar de derecha a izquierda el indice empieza en -1.

 """

# Acceso a los elementos de la lista utilizando indices negativos
print(frutas[-1].capitalize()) # Salida: naranja
print(frutas[-2]) # Salida: cereza
print(frutas[-3]) # Salida: banana  
print(frutas[-4]) # Salida: manzanas  

message = f'Mi fruta favorita es {frutas[0].title()}'
print(message)  # Salida: Mi fruta favorita es Manzanas


"""
f sirve para combinar variables con texto string que esta dentro de las comillas triples o una sola comilla.
"""
my_favorite_frut = frutas[1]
message = f'Mi fruta favorita es {my_favorite_frut.title()}'
print(message)  # Salida: Mi fruta favorita es Banana

"""
 agregar elementos a una lista
 - append(): agrega un elemento al final de la lista.
 append(): agrega un elemnto al final de la lista.
El metodo append modifica la lista original.


"""
print("\nAgregar elementos a una lista con append()\n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles.append("emiliano bike")
print(motorcycles)
 
print(motorcycles[0].title())  # Salida: Honda
print(motorcycles[-1])  # Salida: Emiliano Bike

"""
agrega elementos auna lista en una posicion especifica.
- insert(): permite agregar un elemento en una posicion especifica de la lista donde yo quera.
 

"""

print("\nAgregar elementos a una lista con insert()\n")
motorcycles = ['honda','yamaha','suzuki']       
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)  # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']
motorcycles.insert(2,'emiliano bike')   
print(motorcycles)  # Salida: ['ducati', 'honda', 'emiliano bike', 'yamaha', 'suzuki'] 
print(motorcycles[-1]) 


"""
el metodo append es para listas 
y el metodo upper es para cadenas de texto strings.

"""

"""
    Eliminar elemtos de una lista.
- del : elimina un elemento de la lista en una posicion especifica de la lista.
 la declaracion del index elimina el elemento en la posicion especifica de la lista.
 """
print("\nEliminar elementos de una lista con del\n")
motorcycles = ['honda','yamaha','suzuki']               
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)  # Salida: ['yamaha', 'suzuki']
print(motorcycles[-1])

"""
eliminar elementos de una lista utilizando el metodo pop().
- pop(): elimina el ultimo elemento de la lista y lo devuelve.
el metodo pop() no toma argumentos y elimina el ultimo elemento de la lista y lo devuelve.

"""
print("\nEliminar elementos de una lista con pop()\n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
last_motorcycle = motorcycles.pop()
print(motorcycles)  # Salida: ['honda', 'yamaha']
print("La ultima motocicleta que tuve fue una " + last_motorcycle.title() + ".")


"""
eliminar elementos de una lista.
- pop index: elimina un elemento de la lista en una posicion especifica y lo devuelve.
el metodo pop (index) toma un argumento, que es el indice del elemento que desea eliminar y devolver.

"""
print("\nEliminar elementos de una lista con pop index\n")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)   
print(motorcycles)  # Salida: ['yamaha', 'suzuki']
print("La primera motocicleta que tuve fue una " + first_motorcycle.title() + ".")
"""
eliminar elementos de una lista por valor
- remove(): elimina la primera aparicion de un elemento con un valor especifico.
el metodo remove(value) toma un argumento, que es el valor del elemento que desea eliminar.

"""


# ejemplo practico del metodo remove()

print("\nEliminar elementos de una lista con remove\n")
motorcycles = ['honda','yamaha','suzuki','ducati']      
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)  # Salida: ['honda', 'yamaha', 'suzuki']

names = ['emiliano','juan','pedro','maria','ana']
print(names)
delated_name = input("\n \n ingresa el nombre que deseas eliminar:")
names.remove(delated_name.strip().lower())
print(names)


