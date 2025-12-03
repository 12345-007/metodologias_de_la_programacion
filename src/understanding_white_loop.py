"""
    doc for understandig_white_loop_1004
    utilizamos el whitle loop para ejecutar un bloque
    de codigo mientras una condicion sea verdadera.

    estructura basica de whitle loop en python:
    whitle loop en python:

        whitle condicion:
        #bloque de codigo a ejecutar 


"""

#ejemplo basico de whitle loop
#verificar si en numero esta en un
#rango espesifico(10 y entre 20)

while True: #whitle loop infinito 
    try:
        number = int(input("ingresa un numero entre 10 y 20: "))
        if number < 20 and number > 10:
          print("numero dentro del rango, felicidades!")
        else:
          print("numero fuera de rango, intentalo de nuevo")
    except:
       print("entrada invalida, ingresa un numero entero:")
       