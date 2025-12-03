#ROBERTO EMILIANO ORTIZ CUMPIAN 
#MATRICULA: 2530167
#GRUPO: A:104


#RESUMEN EJECUTIVO
"""- ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
Una lista es una colección ordenada y modificable de elementos; una tupla es una colección 
ordenada e inmutable (no modificable); y un diccionario es una colección desordenada de pares
clave-valor. La principal diferencia es la mutabilidad (las listas se pueden cambiar, las tuplas no), 
mientras que los diccionarios usan claves únicas en lugar de un índice numérico para acceder a sus valores. 
- ¿Qué significa que una lista sea mutable y una tupla inmutable?
Que una lista sea mutable significa que se pueden añadir, eliminar o modificar sus elementos después 
de crearla. Que una tupla sea inmutable significa que su contenido y tamaño son fijos y no se pueden cambiar 
una vez creadas. 
- ¿Cómo se usan los diccionarios para asociar claves con valores?
Los diccionarios asocian claves con valores mediante la notación de corchetes [ ]. Se crea un nuevo par clave-valor 
asignando un valor a una clave entre corchetes, por ejemplo, mi_diccionario[clave] = valor. Para acceder a un valor, 
se utiliza la clave entre corchetes: valor = mi_diccionario[clave]. Los diccionarios son mutables, lo que significa 
que puedes añadir, modificar o eliminar pares clave-valor. 
- ¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas,
validaciones aplicadas y uso de listas, tuplas y diccionarios en contextos prácticos
(por ejemplo, catálogos, registros, estadísticas).
"""

#Problem 1: Shopping list basics (list operations)
#Description: 2–4 lines explaining what the program does.
"""
Inputs:- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).
- ...

Outputs:- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false
- ...

Validations:- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

- ...

Test cases:
1) Normal: ...initial_items_text = "apple,banana,orange"
new_item = "grapes"
search_item = "banana"
Items list: ['apple', 'banana', 'orange', 'grapes']
Total items: 4
Found item: True

2) Border: ...initial_items_text = " apple ,  , pear ,  mango "
new_item = "kiwi"
search_item = "orange"
Items list: ['apple', 'pear', 'mango', 'kiwi']
Total items: 4
Found item: False
3) Error: ...initial_items_text = "   "
new_item = "apple"
search_item = "banana"
Error: invalid input
"""

def shopping_list_processor(initial_items_text, new_item, search_item):
    SEPARATOR = ","

    if initial_items_text.strip() == "":
        print("Error: invalid input")
        return

    if new_item.strip() == "":
        print("Error: invalid input")
        return

    if search_item.strip() == "":
        print("Error: invalid input")
        return

    raw_items = initial_items_text.split(SEPARATOR)
    items_list = [item.strip() for item in raw_items if item.strip() != ""]

    items_list.append(new_item.strip())

    total_items = len(items_list)
    is_in_list = search_item.strip() in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", is_in_list)

#Problem  2: Points and distances with tuples
#Description: 2–4 lines explaining what the program does.
"""
Inputs:- x1, y1, x2, y2 (float; coordenadas de los puntos).
- ...

Outputs:- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

- ...

Validations:- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.

- ...

Test cases:
1) Normal: ...x1 = 1
y1 = 2
x2 = 4
y2 = 6
Point A: (1.0, 2.0)
Point B: (4.0, 6.0)
Distance: 5.0
Midpoint: (2.5, 4.0)
2) Border: ...x1 = 3
y1 = 3
x2 = 3
y2 = 3
Point A: (3.0, 3.0)
Point B: (3.0, 3.0)
Distance: 0.0
Midpoint: (3.0, 3.0)

3) Error: ...x1 = "abc"
y1 = 2
x2 = 4
y2 = 6
Error: invalid input

"""
x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
except ValueError:
    print("Error: invalid input")
    exit()

point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)




#Problem 3: Product catalog with dictionary
#Description: 2–4 lines explaining what the program does.
"""
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
"""
"""
Inputs:- product_name (string).
- quantity (int; cantidad a comprar).

- ...

Outputs:- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"
- ...

Validations:- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).
- ...

Test cases:
1) Normal: ...
product_name = "apple"
quantity = 3
Salida esperada:

Unit price: 10.0

Quantity: 3

Total: 30.0


2) Border: ...
product_name = "banana"

quantity = 1

Salida esperada:

Unit price: 8.5

Quantity: 1

Total: 8.5
3) Error: ...
product_name = "orange"

quantity = 0

Salida esperada:

Error: invalid quantity
"""

product_prices = {
    "apple": 10.0,
    "banana": 6.5,
    "orange": 8.0
}

product_name = input("Enter product name: ").strip().lower()

if product_name == "":
    print("Error: product name cannot be empty")
else:
    quantity_input = input("Enter quantity: ")

    if not quantity_input.isdigit():
        print("Error: quantity must be a positive integer")
    else:
        quantity = int(quantity_input)

        if quantity <= 0:
            print("Error: invalid quantity")
        else:
            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")

#Problem  4: Student grades with dict and list
#Description: 2–4 lines explaining what the program does.
"""
Inputs: student_name (string).
- ...

Outputs:Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

- ...

Validations: student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

- ...

Test cases:
1) Normal: ...
Entrada:
Alice
Salida esperada:

Grades: [90.0, 85.5, 88.0]
Average: 87.83333333333333
Passed: true
2) Border: ...Entrada:

Bob
Salida esperada:

Grades: [70.0, 72.5, 68.0]
Average: 70.16666666666667
Passed: true

3) Error: ...
Entrada:

Daniel
Salida esperada:

Error: student not found
"""
student_grades = {
    "Alice": [90.0, 85.5, 88.0],
    "Bob": [70.0, 72.5, 68.0],
    "Carol": [95.0, 92.0, 94.0]
}

student_name = input().strip()

if student_name == "":
    print("Error: invalid input")
elif student_name not in student_grades:
    print("Error: student not found")
else:
    grades_list = student_grades[student_name]
    if len(grades_list) == 0:
        print("Error: empty grades list")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", str(is_passed).lower())



#Problem X: <short title>
#Description: 2–4 lines explaining what the program does.
"""
Inputs:- sentence (string).
- ...

Outputs:- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)
- ...

Validations:- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía
- ...

Test cases:
1) Normal: ...Entrada:

Hello hello world hello
Salida esperada:

Words list: ['hello', 'hello', 'world', 'hello']
Frequencies: {'hello': 3, 'world': 1}
Most common word: hello

2) Border: ...
Entrada:

red blue green yellow


Salida:

Words list: ['red', 'blue', 'green', 'yellow']
Frequencies: {'red': 1, 'blue': 1, 'green': 1, 'yellow': 1}
Most common word: red

3) Error: ...
Entrada:

    


(solo espacios)

Salida:

Error: invalid input
"""

sentence = input().strip()

if sentence == "":
    print("Error: invalid input")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        max_freq = 0

        for word, freq in freq_dict.items():
            if freq > max_freq:
                max_freq = freq
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

#Problem 6: Simple contact book (dictionary CRUD)
#Description: 2–4 lines explaining what the program does.
"""Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)

Inputs:- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").
- ...

Outputs:- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"
- ...

Validations:- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
- ...

Test cases:
1) Normal: ...Entrada:

SEARCH
Alice
Salida esperada:

Phone: 1111111111

2) Border: ...
Entrada:

ADD
Bob
9999999999
Salida:

Contact saved: Bob 9999999999
3) Error: ...
Entrada:

UPDATE
Alice
Salida:

Error: invalid input
"""
contacts = {
    "Alice": "1111111111",
    "Bob": "2222222222",
    "Charlie": "3333333333"
}

action_text = input().strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
else:
    name = input().strip()
    if name == "":
        print("Error: invalid input")
    else:
        if action_text == "ADD":
            phone = input().strip()
            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)
        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")
        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")

# Cuándo conviene usar listas, tuplas o diccionarios:
# Las listas convienen cuando necesitas una estructura flexible donde los datos puedan
# cambiar de tamaño, ya que permiten agregar, eliminar o modificar elementos fácilmente.

# Las tuplas convienen cuando la información no debe cambiar, ya que son estructuras
# inmutables. Son útiles para mantener datos fijos y asegurar que no se modifiquen
# accidentalmente durante la ejecución del programa.

# Los diccionarios convienen cuando necesitas buscar información rápidamente mediante
# una clave, ya que permiten acceder a los valores de forma directa sin recorrer toda
# la estructura. Son ideales para datos organizados por categorías, propiedades o nombres.

# Patrones comunes al combinar estas estructuras:
# Un patrón muy usado es el diccionario que contiene listas, lo cual permite agrupar
# elementos relacionados bajo una clave específica. También es común usar diccionarios
# que contienen tuplas cuando se quiere almacenar valores múltiples que no deben cambiar.



#referencias
"""
https://www.pontia.tech/python-listas-tuplas-diccionario/#:~:text=%C2%BFCu%C3%A1l%20es%20la%20diferencia%20entre,agregar%2C%20eliminar%20o%20cambiar%20elementos.
https://www.udacity.com/blog/2025/02/python-lists-vs-tuples-understanding-their-differences-and-best-uses.html#:~:text=una%20decisi%C3%B3n%20informada.-,%C2%BFQu%C3%A9%20son%20las%20listas%20de%20Python?,incluso%20otras%20listas%20y%20tuplas.
https://www.dataquest.io/blog/python-dictionaries/#:~:text=%C2%BFC%C3%B3mo%20crear%20un%20diccionario?&text=Podemos%20ver%20que%20ambos%20diccionarios,corchetes:%20dictionary%5Bkey%5D%20.&text=Los%20enteros%2C%20los%20n%C3%BAmeros%20de,los%20valores%20de%20un%20diccionario.&text=Solo%20se%20devuelve%20el%20valor,un%20diccionario;%20podr%C3%ADa%20resultar%20confuso.
Tutoriales de Python sobre estructuras de datos básicas.
Libros o apuntes de algoritmos y programación básica.


"""