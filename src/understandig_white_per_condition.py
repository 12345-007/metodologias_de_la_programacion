"""vamos a relizar un programa que
   defina un PIN como contraseña.
   
   despues bamos a darle tres intentos al ususario 
   para escribir el pin 
   
   si el ususario escribe correctamente el 
   pin, el programa debe mostrar un mensaje de acceso permitido 
   
   si el ususario se equivoca el programa debe desirle cuantos intentos 
   le quedadan
   """

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3 
intents = 0

while intents < MAX_ATTEMPTS:

    user_pin = input("escribe tu PIN:")

    if user_pin == CORRECT_PIN:
        print("Acceso permitido.")
        break
    else:
        intents+=1
        remainings_attemps = MAX_ATTEMPTS-intents
        if remainings_attemps>0:
            print(f"PIN INCORRECTO TE QUEDAN ")
    

