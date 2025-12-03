#ROBERTO EMILIANO ORTIZ CUMPIAN 
#MATRICULA: 2530167
#GRUPO: A:104


#RESUMEN EJECUTIVO 
"""- ¿Qué es un string en Python (tipo de dato, inmutabilidad)?Un string en Python es un tipo de dato que representa 
una secuencia de caracteres, almacenados entre comillas simples (') o dobles ("), y es de tipo inmutable, lo que 
significa que su contenido no puede ser modificado una vez creado. En lugar de alterar un string existente, cualquier 
operación que parezca modificarlo en realidad crea un nuevo string en una nueva dirección de memoria. 

- ¿Qué operaciones básicas se pueden realizar: concatenar, obtener longitud, extraer sub-cadenas, 
   buscar patrones, reemplazar texto?Sí, todas las operaciones mencionadas son operaciones básicas y fundamentales que se 
   pueden realizar con cadenas de texto en la gran mayoría de los lenguajes de programación, sistemas de bases de datos y
   herramientas de manipulación de texto como hojas de cálculo. 

- ¿Por qué es importante validar y normalizar texto de entrada 
  (por ejemplo, correos, nombres, contraseñas)?Validar y normalizar cualquier dato que ingresa un usuario (correos, nombres, 
  contraseñas, direcciones, etc.) es esencial para que un sistema sea seguro, funcional y confiable.

"""
#Problem 1:Full name formatter (name + initials)
#Description: 2–4 lines explaining what the program does.
"""el codigo trata de que el usuario ingrese su nombre asi como se
muestra a continuacion pero lo piede ingresar con todas las letras 
minusculas o mayusculas y el programa lo va a imprimir con la primer 
letra de cada palabra mayuscula y el resto de letras minusculas y 
tambien imprimira las primeras letras de cada palabra en mayusculas 
imprimiendo solo las iniciales en la pantalla seria un formateador de nombre
completo."""

"""
Inputs:- full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).
- ...

Outputs:- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"
- ...

Validations: full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.
- ...

Test cases:
1) Normal: enter your full name: roberto emiliano ortiz cumpian
formatted name: Roberto Emiliano Ortiz Cumpian
initials: R.E.O.C.
2) Border: ...
3) Error:enter your full name: rrrrrroooobeeeerrrtoooo
Error: invalid input (enter at least two words)
"""
#PROBLEM_1 
"""full_name = input("enter your full name: ")
clean_name= " ".join(full_name.strip().split())
MIN_PARTS=2
if len(clean_name) == 0:
    print("error: invalid imput (empty tring)")
elif len(clean_name.split()) < MIN_PARTS:
    print("Error: invalid input (enter at least two words)")
else:

    formatted_name = clean_name.title()
    name_parts = clean_name.split()
    initials = ".".join([part[0].upper() for part in name_parts]) + "."
    print(f"formatted name: {formatted_name}")
    print(f"initials: {initials}")
"""

#Problem 2: Simple email validator (structure + domain)
#Description: 2–4 lines explaining what the program does.
"""Este codigo o algoritmo nos ayuda verificar o saber si nustro
correo electronico es apto para usarlo si tiene las suficientes 
requisitos para usarse si es valido el programa nos arroja  verdadero 
si no es valido el programa nos arroja falso que no se puede usar.
"""

"""
Inputs:- email_text (string).
- ...

Outputs:- - "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validations: - email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Test cases:
1) Normal:enter your email address: emiliano.or270@gmail.com
valied email: true
domain: gmail.com
2) Border:enter your email address: emiliano@@.com123
valid email: falce
3) Error:
"""
#problema_2
"""
# Constantes
MIN_AT_COUNT = 1
MAX_AT_COUNT = 1

# Entrada del usuario
email_text = input("enter your email address: ")

# Paso 1: Normalizar entrada (quitar espacios al inicio y final)
clean_email = email_text.strip()
# Paso 2: Validaciones básicas
# Verificar si está vacío después de strip()
if len(clean_email) == 0:
    print("valid email: false")
# Verificar si contiene espacios internos
elif " " in clean_email:
    print("valid email: falce")
# Verificar que exista exactamente un '@'
elif clean_email.count("@") !=1:
    print("valid email: falce")
    # Encontrar la posición del '@'
else:
    at_index = clean_email.find("@")
# Verificar que después del '@' exista al menos un '.'
    if "." not in clean_email[at_index:]:
        print("valid email: false")
# Email válido – extraer el dominio
    else:
        domain = clean_email[at_index + 1:]
        print("valied email: true")
        print(f"domain: {domain}")
"""
#Problem 3: Palindrome checker (ignoring spaces and case)
#Description: 2–4 lines explaining what the program does.
"""este codigo me sirve para identificar si una 
palabra se lee igual de derecha a isquierda y
de isquierda a derecha."""
"""
Inputs:phrase (string).
- ...

Outputs:"Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.
- ...

Validations:- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios 
(por ejemplo, al menos 3 caracteres).
- ...

Test cases:
1) Normal: ingresa la frase:Anita lava la tina
is palindrome: True
normalized phrase: anitalavalatina
2) Border:ingresa la frase:Hola mundo
is palindrome: False
normalized phrase: holamundo
3) Error: ingresa la frase:w
error: phrase too short to check palindrome.
"""
#probrema_3
"""phrace = input("ingresa la frase:")
if phrace.strip() == "":
    print("error: the phrase cannot be empty.")
else:
    normaliczed = phrace.lower().replace(" ","")
    if len(normaliczed) < 3:
        print("error: phrase too short to check palindrome.")
    else:
        reversed_text = normaliczed[::-1]
        is_palindrome = (normaliczed == reversed_text)
        print("is palindrome:", is_palindrome)
        print("normalized phrase:", normaliczed)"""

#Problem_4: Sentence word stats (lengths and first/last word)
##Description: 2–4 lines explaining what the program does.

"""
Inputs:sentence (string).

Outputs:- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validations:- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().


Test cases:
1) Normal: ...Enter a sentence:  la vaca lola tiene cabeza y tiene cola
Word count: 8
First word: la
Last word: cola
Shortest word: y
Longest word: cabeza
2) Border: ...Enter a sentence: qwertyujm
Word count: 1
First word: qwertyujm
Last word: qwertyujm
Shortest word: qwertyujm
Longest word: qwertyujm
3) Error: ...Enter a sentence:
Error: empty sentence
"""
"""
#problema_4

MIN_WORDS = 1  # mínimo de palabras válidas

# Entrada del usuario
sentence = input("Enter a sentence: ")

# Paso 1: Normalizar espacios externos
clean_sentence = sentence.strip()

# Validación: verificar si está vacía
if len(clean_sentence) == 0:
    print("Error: empty sentence")
else:
    # Paso 2: Separar palabras por espacios
    words = clean_sentence.split()

    # Validación: verificar que haya palabras válidas
    if len(words) < MIN_WORDS:
        print("Error: no valid words found")
    else:
        # Paso 3: Obtener datos básicos
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        # Paso 4: Encontrar palabra más corta y más larga
        shortest_word = words[0]
        longest_word = words[0]

        for w in words:
            if len(w) < len(shortest_word):
                shortest_word = w
            if len(w) > len(longest_word):
                longest_word = w

        # Salidas
        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")
"""

#Problem 5: Password strength classifier
##Description: 2–4 lines explaining what the program does.
"""
Inputs:- password_input (string).
- ...

Outputs:- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"
- ...

Validations:- No aceptar contraseña vacía.
- Verificar longitud con len().
- ...

Test cases:
1) Normal: ...Enter the password: Emiliano(@)26
Password strength: medium
2) Border: ...
3) Error: ...Enter the password: 1
Password strength: weak
#referencias 
"""
"""
#problem_5:
MIN_LENGTH = 8 
password_input = input("Enter the password: ").strip()
if len(password_input) == 0:
    print("password strength: weak")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for ch in password_input:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_isdigit = True
        elif not ch.isalnum(): 
            has_symbol = True   

    is_long_enough = len(password_input) >= MIN_LENGTH

    
    if not is_long_enough:
        password_strength = "weak"
    else:
        
        if has_upper and has_lower and has_digit and has_symbol:
            password_strength = "strong"
        else:
            
            types_count = sum([has_upper, has_lower, has_digit, has_symbol])

            if types_count >= 2:
                password_strength = "medium"
            else:
                password_strength = "weak"

    print(f"Password strength: {password_strength}")


"""


#Problem 6: Product label formatter (fixed-width text)
##Description: 2–4 lines explaining what the program does.
"""
Inputs:- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).
- ...

Outputs:- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)
- ...

Validations:- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.
- ...

Test cases:
1) Normal: ...Enter product name: bread
Enter price: 25
Label: "Product: bread | Price: $25.00"
apple juice 
2) Border: ...Enter product name: apple juice 
Enter price: 12
Label: "Product: apple juice | Price: "
3) Error: ...Enter product name: 
Enter price: 10
Error: invalid product name
"""
#problem_6
LABEL_LENGTH = 30
MIN_PRICE = 0.0

# Leer entradas
product_name = input("Enter product name: ")
price_value = input("Enter price: ")

# Validar nombre del producto

clean_name = product_name.strip()   # quitar espacios al inicio y final

if len(clean_name) == 0:
    print("Error: invalid product name")
    exit()

# Validar y convertir precio

try:
    price_number = float(price_value)
except ValueError:
    print("Error: invalid price")
    exit()

if price_number <= MIN_PRICE:
    print("Error: invalid price")
    exit()

# Convertir precio a texto con dos decimales
price_text = f"{price_number:.2f}"

# Construir la etiqueta base

label = f"Product: {clean_name} | Price: ${price_text}"

# Medir longitud actual
label_length = len(label)

# Ajustar a exactamente 30 caracteres

if label_length == LABEL_LENGTH:
    final_label = label

elif label_length < LABEL_LENGTH:
    # Rellenar con espacios
    padding = LABEL_LENGTH - label_length
    final_label = label + (" " * padding)

else:
    # Recortar a 30 caracteres
    final_label = label[:LABEL_LENGTH]

# Mostrar resultado final

print(f'Label: "{final_label}"')

# El manejo de strings es esencial en cualquier programa que trabaje con entrada y salida de datos,
# porque casi toda la información del usuario llega como texto y debe procesarse correctamente.
# Métodos como lower(), strip() y split() son útiles para normalizar, limpiar y dividir datos,
# mientras que join() permite reconstruir cadenas de forma controlada. Normalizar el texto antes
# de compararlo evita errores por mayúsculas, espacios extra o formatos inconsistentes. Además,
# diseñar validaciones apropiadas previene que datos incorrectos entren al sistema y causen fallos.
# Aprendí también que los strings son inmutables, por lo que cada transformación genera una nueva
# cadena, y que los slices permiten obtener partes específicas del texto de manera segura y precisa.



#referencias 
"""https://www.youtube.com/shorts/yjcHXxnS-P8#:~:text=En%20Programaci%C3%B3n%20las%20variables%20del%20tipo%20String,
por%20qu%C3%A9%20pasa%20esto.%20%23shorts%20%23programming%20%23dev.
https://www.youtube.com/watch?v=tb6EYiHtcXU1
https://www.youtube.com/watch?v=tb6EYiHtcXU2
https://www.youtube.com/watch?v=tb6EYiHtcXU3
https://www.youtube.com/watch?v=tb6EYiHtcXU4
"""