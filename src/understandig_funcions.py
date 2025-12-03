"""funcions
    las funciones son bloques de codigos diseñados 
    para realizaar una tarea espesifica 
    
    cuando queremos realizar la tarea que se a definido 
    en una funcion tenemos que llamar el nombre de la funcion responsable de esto.
    
    definicion de una funcion (Syntax)
    
    def  name_of_fuction(parameters):
        actions

"""

def greeting_mauro():
    print("hola mauro, que gusto verte!!!")

"""for i in range(10):
    greeting_mauro()
"""

#parametros
def greet(usename):
    print(f"Hola {usename}, que desgracia verte!!!")

#argumentos
greeting_mauro()
greet("jorge")


def greet(usename, msj):
    print(f"Hola {usename}, {msj}!!!")

#argumentos
greeting_mauro()
greet("jorge", "eres joto puto.")

"""vamos a aser un programa que genere el nombre completo de  una persona.

   vamos a pasarle el primer nombre, el segundo y el apellido

   la funcion debe generar el nombre completo y regresarlo 

   """
def create_full_name(first_name, last_name,  middle_name=""):
    """docstring - jorge this functions creates the fullname
    of a person given its three names.
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

user_first_name = input("Escribe tu primer nombre:").strip().lower()
user_middle_name = input("Escribe tu segundo nombre:").strip().lower()
user_last_name = input("Escribe tus apellidos:").strip().lower()

#esta manera de mandar llamar la funcion es Argumentos posicionales -> positional arguments
print(create_full_name(user_first_name,  
                       user_last_name,
                       user_middle_name,))

full_name = create_full_name(
    user_first_name,
    user_first_name,
    user_middle_name
)
print(full_name)

#argumentos clave -> keyword arguments
full_name_key = create_full_name(
    last_name=user_last_name,
    first_name=user_first_name,
    middle_name=user_middle_name

)
print(full_name_key)



## parametros opcionales 
profe_falso=create_full_name("carlos", "tovar")
print(profe_falso)




#temas para estudiar a futuro 
#funciones: args, kwargs
#manejo de datos: abrir archivos scv,.json,.yml,.txt,.xls,.dos,.
#argumento por linea de comandos - sys
#cli - command line interface
# generadores, interadores, yield
#testing -> 