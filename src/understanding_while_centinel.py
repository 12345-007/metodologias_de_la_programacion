"""
 vamos a realisar un programa que sume pesos mexicanos
 hasta que el usuario escriba la palabra "salir"

 el programa tambien debe decirme cuantos numeros 
 ingreso el usuario, cual fue el minimo y cual fue 
 el maximo.

"""
sum_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:
    print("ingresa la palabra 'salir' para terminar")
    user_input = input("ingresa una cantidad (MXN): ")

    #centinel
    if user_input == 'salir':
        break 

    try: 
        quantity = float(user_input)
    except ValueError:
        print("cantidad no valida, ingresa nueva mente")
        continue
    except KeyboardInterrupt:
        break

    counter +=1 # esto es una estructura contadora 
    sum_numbers += quantity #esto es una estructura acumuladora 
    
    if minimum is None or quantity < minimum:
        minimum = quantity

    if maximum is None or quantity > maximum:
        maximum = quantity

print("SUM", sum_numbers)
print("COUNTADOR", counter)
print("maximo", maximum)
print("minimo", minimum)



