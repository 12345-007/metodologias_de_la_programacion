"""
las listas tambien pueden almacenar numeros y de echo 
son ideales para almacenarlos.

 python ofrece una gran variedad de metodos para trabajar con listas de numeros.

 por ejemplo, funcion range():  para crear una lista de numeros

"""
# la funcion range() crea una lista de numeros
# en un rango especifico.
numbers = list(range(10)) # crea una lista de numeros del 0 al 9
print(numbers)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) # salida class 'list'

# podemos realizar lo mismo con un foor loop:
for number in range(10):
    print(number)
    #print(type(number))

"""\n aqui solo se imprimen del 1 al 4 por el rango espesificado.\n"""

for number in range(1, 5):
    print(number)

"""\n numeros impares:\n"""

for num in range(1, 10, 2):  # numeros impares del 1 al 9
        print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # salida: [1 2 3 4 5 6 7 8 9]


"""\n numeros pares\n"""
for num in range(2, 10, 2): #numeros pares del 2 al 9
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) # salida: [2 4 6 8]

# conclucion: podemos crear cualquier tipos de listas de numeros 
# utilizando range() y list().
print("\nprimeros 10 numeros al cuadrado:\n")
squares = []
for value in range(1, 11):
    square = value ** 2                      # si quieres cambiar al cubo solo cambia el 2 por un 3
    squares.append(square)
print(squares)


# ejemplo cubos 
squares = []
for value in range(1, 11):
    square = value ** 3                      # si quieres cambiar al cubo solo cambia el 2 por un 3
    squares.append(square)
print(squares)

# metodos built-in para listas de numeros 
print("\nmetodos built-in para listas de numeros\n")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"lista de dijitos: {digits}")





