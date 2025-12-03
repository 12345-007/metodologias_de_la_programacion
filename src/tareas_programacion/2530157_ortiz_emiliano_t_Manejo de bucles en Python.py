#ROBERTO EMILIANO ORTIZ CUMPIAN 
#MATRICULA: 2530167
#GRUPO: A:104

 #RESUMEN EJECUTIVO
"""
 ¿Qué es un bucle for y para qué se usa típicamente?
 Un bucle for es una construcción de programación que permite ejecutar un bloque de código un número
 predeterminado de veces. Se usa típicamente para iterar sobre elementos de una secuencia, como listas,
 diccionarios o cadenas de texto, y es ideal cuando se sabe de antemano cuántas repeticiones se necesitan. 
- ¿Qué es un bucle while y cuándo es más natural usarlo?
Un bucle while ejecuta un bloque de código repetidamente mientras una condición booleana sea verdadera.
Es más natural usarlo cuando no sabes de antemano cuántas veces se necesitará iterar, como por ejemplo,
esperar a que el usuario introduzca un dato correcto o procesar datos hasta que se cumpla una condición 
específica, en lugar de para un número predeterminado de veces. 
- ¿Qué son un contador y un acumulador?
Un contador es una variable que se utiliza para contar el número de veces que ocurre un evento, incrementándose
típicamente en 1 en cada ocurrencia. Un acumulador es una variable que suma o almacena valores continuos de una operación,
como la suma de una lista, donde su valor cambia según el resultado de una operación. Ambos se usan frecuentemente en ciclos 
(bucles) para mantener un estado durante la ejecución. 
- ¿Por qué es importante definir bien la condición de salida y evitar ciclos infinitos?
es importante  por que si no lo defines sete va partir el programa 
y  a tronar la pc ya sea que se trave y ya no ejecute nada 
por eso ay que definir vien eso 
- ¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas,
validaciones, y uso de for/while en diferentes situaciones (recorridos, menús, lectura repetida).
"""
#Problem 1: 1: Sum of range with for
#Description: 2–4 lines explaining what the program does.
"""
Inputs:
- ...

Outputs:
- ...

Validations:
- ...

Test cases:
1) Normal: ...
Input:
n = 10
Output:
Sum 1..n: 55
Even sum 1..n: 30
2) Border: ...
Input:
n = 1
Output:
Sum 1..n: 1
Even sum 1..n: 0
3) Error: ...
Input:
n = -5 → o 0 → o "abc"
Output:
Error: invalid input
"""
user_input = input("Enter n: ").strip()

if not user_input.isdigit():
    print("Error: invalid input")
else:
    n = int(user_input)

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for number in range(1, n + 1):
            total_sum += number
            if number % 2 == 0:
                even_sum += number

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)



#Problem  2: Multiplication table with for
#Description: 2–4 lines explaining what the program does.
"""Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
Inputs:
 base (int)
- m (int; límite de la tabla)
- ...

Outputs:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.
- ...

Validations:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

- ...

Test cases:
1) Normal: ...
Input:
base = 5
m = 4

Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
2) Border: ...
Input:
base = 7
m = 1

Output:
7 x 1 = 7
3) Error: ...
base = "abc"
m = 5
Output:
Error: invalid input
"""
base_input = input("Enter base: ").strip()
m_input = input("Enter limit: ").strip()

if not base_input.lstrip("-").isdigit() or not m_input.isdigit():
    print("Error: invalid input")
else:
    base = int(base_input)
    m = int(m_input)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")



#Problem 3: Average of numbers with while and sentinel
#Description: 2–4 lines explaining what the program does.
"""Lee números uno por uno hasta que el usuario ingrese un valor sentinela 
(por ejemplo, -1). Calcula el promedio de los números válidos ingresados y la cantidad 
de números leídos. Si el usuario sólo ingresa el sentinela sin números válidos, muestra 
un mensaje de error.

Inputs: 
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).
- ...

Outputs:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"
- ...

Validations:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.
- ...

Test cases:
1) Normal: ...
User inputs:

10
20
30
-1
Output:

Count: 3
Average: 20.0
2) Border: ...
Input:

50
-1
Output:

Count: 1
Average: 50.0
3) Error: ...
Input:

-1
Output:

Error: no data
"""
SENTINEL_VALUE = -1.0

count = 0
total_sum = 0.0

while True:
    number_input = input("Enter number: ").strip()
    try:
        number = float(number_input)
    except:
        print("Error: invalid input")
        continue

    if number == SENTINEL_VALUE:
        break

    count = count + 1
    total_sum = total_sum + number

if count == 0:
    print("Error: no data")
else:
    average_value = total_sum / count
    print("Count:", count)
    print("Average:", average_value)



#Problem 4: Password attempts with while
#Description: 2–4 lines explaining what the program does.
"""Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los intentos, 
mostrar un mensaje de bloqueo.
"""
"""
Inputs:- user_password (string; se lee en cada intento).
- ...

Outputs:- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"
- ...

Validations:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

- ...

Test cases:
1) Normal: ...
Input sequence:

1234
admin123
Output:

Login success
2) Border: ...
Input sequence:

aaa
bbb
admin123
Output:

Login success
3) Error: ...
Input:

111
222
333
Output:

Account locked
"""
MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "admin123"

attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ").strip()
    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    attempts = attempts + 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")

#Problem 5: Simple menu with while
#Description: 2–4 lines explaining what the program does.
"""Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit

Inputs:- option (string o int; elección del usuario).
- ...

Outputs:- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

- ...

Validations:- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
- ...

Test cases:
1) Normal: ...
User sequence:

1
2
3
2
0
Output:

Hello!
Counter: 0
Counter incremented
Counter: 1
Bye!

2) Border: ...
Input:

0
Output:

Bye!
3) Error: ...
Input:

abc
9
1
0
Output:

Error: invalid option
Error: invalid option
Hello!
Bye!

"""
counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Option: ").strip()
    try:
        option = int(option_input)
    except:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter = counter + 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

#Problem 6: Pattern printing with nested loops
#Description: 2–4 lines explaining what the program does.
"""Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).

Inputs:- n (int; número de filas del patrón).
- ...

Outputs:- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- ...

Validations:- n convertible a int.
- n >= 1; si no, "Error: invalid input".

- ...

Test cases:
1) Normal: ...
Input:

4
Output:

*
**
***
****
****
***
**
*
2) Border: ...
Input:

1
Output:

*
*
3) Error: ...
abc
Output:

Error: invalid input

"""
n_input = input("Enter number of rows: ").strip()

try:
    n = int(n_input)
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

for i in range(1, n + 1):
    print("*" * i)

for i in range(n, 0, -1):
    print("*" * i)


    
# concluciones 

# - Diferencias prácticas entre usar for y while:
#   - El bucle for es útil cuando se conoce o se define claramente la cantidad de iteraciones.
#   - El bucle while es útil cuando la repetición depende de una condición que puede cambiar durante la ejecución.

# - Cómo ayudaron los contadores y acumuladores dentro de los bucles:
#   - Los contadores permitieron llevar el registro de cuántas iteraciones o entradas válidas se procesaron.
#   - Los acumuladores permitieron ir sumando valores o construyendo resultados de forma progresiva.

# - Riesgos al programar un while:
#   - Condiciones incorrectas o mal planteadas pueden generar ciclos infinitos.
#   - Errores al actualizar la condición pueden impedir que el bucle termine.

# - Cómo los menús y los intentos de contraseña son ejemplos típicos de while:
#   - Los menús requieren repetirse hasta que el usuario elija salir.
#   - Los sistemas de contraseña repiten intentos hasta que haya éxito o se alcancen los intentos máximos.

# - Qué se aprendió sobre bucles anidados y generación de patrones:
#   - Los bucles anidados permiten repetir estructuras dentro de otras repeticiones.
#   - Hacen posible construir patrones visuales o numéricos creando filas o niveles paso a paso.



# referencias 
"""
https://plataforma.josedomingo.org/pledin/cursos/programacion/curso/u23/#:~:text=Un%20contador%20es%20una%20variable,contado%20se%20le%20suma%201.
https://es.scribd.com/document/508901823/Contadores-y-Acumuladores#:~:text=Contadores%20y%20Acumuladores-,Este%20documento%20explica%20la%20diferencia%20entre%20contadores%20y%20acumuladores.,sus%20valores%20de%20forma%20sucesiva.
https://study.com/academy/lesson/while-loop-definition-example-results.html#:~:text=n%C3%BAmero%20de%20iteraciones-,Resumen%20de%20la%20lecci%C3%B3n,no%20se%20cumple%20una%20condici%C3%B3n.
apuntes de calses de programacion
chatgpt.com

"""

