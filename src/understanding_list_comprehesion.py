# list comprehensions
"""una lista de comprehensions combina el for loop
y la creacion de nuevos elementos y tambien, automaticamente agrega el nuevo elemento 
ala lista, es decir, sin utilizar el append
"""

squares=[value**2 for value in range(1, 11)]
print(squares)

even_num_0_100_range = list(range(0,101,2))
print(even_num_0_100_range)

# numeros pares utilizando list comprehencions
even_list_compre = [value for value in range(0,101) if value%2 == 0] # si pongo en 1 enves del sero me dara los numeros impares
print(even_list_compre)



