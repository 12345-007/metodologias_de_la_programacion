magicians = ['alice', 'david', 'carolina', 'bob', 'eve', 'frank']
print('alice'[0], 'david'[1], 'carolina'[2])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran echiso.")
    print("\n")

print("Gracias a todos, fue un gran espectaculo!")

"""
     Identacion.

     python utilica la identacion para determinar cuando una linea de codigo
     esta conectada ala linea de codigo 
     anteriror.
     basicamente, se utilizan 4 espacion en blanco
     para obligarnos a escribir codigo ordenado y estructurado.

"""
# no olvidemos identar (donde se necesita)
# ejemplo 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
#print(magician) #  Error - el for necesita al menos un elemento 
    print(magician) # Correcto

# identantion error 
# logical error - del programdor
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#print(f"great {magician}!, I can't wait to see your next trick.") error de logica
    print(f"great {magician}!, I can't wait to see your next trick.")
print("Thank you everyone, that was a great magic show!") # solucion identar ala isquierda 

# identacion innecesaria
message = "hola charly"



# error de syntaxis
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # (sytaxis error): olvidar colocar los dos puntos (:) al final de la linea del for
    print(magician)
    
    
