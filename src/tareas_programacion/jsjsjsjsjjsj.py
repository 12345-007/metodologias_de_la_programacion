# ================================
# MÉTODOS Y FUNCIONES DE STRING
# ================================
# - len(): devuelve la longitud del texto.
# - indexación text[i]: permite acceder a un carácter específico.
# - slicing text[a:b]: permite obtener subcadenas.
# - lower(): convierte el texto a minúsculas.
# - upper(): convierte el texto a mayúsculas.
# - title(): coloca en mayúscula la primera letra de cada palabra.
# - strip(): elimina espacios al inicio y al final.
# - replace(): sustituye partes del texto por otras.
# - split(): divide el texto en una lista de palabras.
# - join(): une elementos de una lista en un solo string.
# - startswith(): verifica si el texto inicia con un patrón.
# - endswith(): verifica si el texto termina con un patrón.
# - find(): busca la posición de un texto dentro de otro.
# - f-strings f"": permite crear textos formateados fácilmente.
# - operador +: concatena textos.
# - operador *: repite un texto un número de veces.
# - in / not in: verifica si una subcadena está presente.
# - operador ==: compara igualdad de textos.

# ================================
# OPERADORES Y FUNCIONES ARITMÉTICAS
# ================================
# - +: suma valores.
# - -: resta valores.
# - *: multiplica valores.
# - /: divide dejando resultado flotante.
# - //: división entera.
# - %: módulo (residuo).
# - **: potencia.

# ================================
# OPERADORES RELACIONALES
# ================================
# - <: menor que.
# - >: mayor que.
# - <=: menor o igual que.
# - >=: mayor o igual que.
# - ==: igualdad.
# - !=: desigualdad.

# ================================
# OPERADORES LÓGICOS
# ================================
# - and: ambas condiciones deben ser verdaderas.
# - or: al menos una condición debe ser verdadera.
# - not: invierte un valor booleano.

# ================================
# FUNCIONES DE CONVERSIÓN
# ================================
# - int(): convierte a entero.
# - float(): convierte a flotante.
# - bool(): convierte a booleano.

# ================================
# FUNCIONES GENERALES
# ================================
# - round(): redondea valores numéricos.
# - abs(): valor absoluto.
# - min(): devuelve el menor valor.
# - max(): devuelve el mayor valor.
# - sum(): suma elementos.
# - sorted(): devuelve una lista ordenada.
# - range(start, stop, step): genera secuencias numéricas.

# ================================
# LISTAS (list)
# ================================
# - len(): tamaño de la lista.
# - indexación my_list[i]: acceso a un elemento.
# - slicing my_list[a:b]: sublista.
# - append(): agrega elemento al final.
# - insert(): inserta en una posición específica.
# - remove(): elimina un elemento.
# - pop(): extrae un elemento.
# - sort(): ordena la lista.
# - reverse(): invierte el orden.
# - in / not in: verifica existencia de un elemento.

# ================================
# TUPLAS (tuple)
# ================================
# - len(): tamaño de la tupla.
# - indexación my_tuple[i]: acceso a un elemento.
# - Uso principal: almacenar datos que no deben modificarse.

# ================================
# DICCIONARIOS (dict)
# ================================
# - acceso my_dict[key]: obtiene valor asociado a una clave.
# - keys(): retorna las claves.
# - values(): retorna los valores.
# - items(): retorna pares clave-valor.
# - get(): devuelve el valor de una clave o un valor por defecto.
# - pop(): elimina una clave y retorna su valor.
# - in: verifica si una clave existe.

# ================================
# TEXTO EN MENÚS Y SENTINELAS
# ================================
# - lower(): útil para normalizar opciones del usuario.
# - strip(): elimina espacios indeseados en entradas del usuario.




# Métodos más usados en listas:

# append(x): Agrega un elemento al final de la lista.
# insert(i, x): Inserta un elemento en una posición específica.
# extend(lista2): Agrega todos los elementos de otra lista.
# pop(i): Elimina y devuelve el elemento en la posición i (si no pones i, quita el último).
# remove(x): Elimina la primera aparición del valor x.
# clear(): Vacía toda la lista.
# sort(): Ordena la lista de menor a mayor.
# reverse(): Invierte el orden de los elementos.
# count(x): Cuenta cuántas veces aparece x.
# index(x): Devuelve la posición donde aparece x por primera vez.
# copy(): Crea una copia de la lista.






# Nesting dictionaries: cuando un diccionario contiene otros diccionarios para organizar datos en 
# niveles.
# Listas de diccionario: una lista que guarda varios diccionarios, útil para manejar muchos registros similares.
# Listas en diccionarios: un diccionario que tiene listas como valores para representar varios elementos de
#  un mismo dato.
# Diccionarios en diccionarios: estructura donde varios diccionarios están dentro de otro diccionario para datos 
# más complejos.
# Método get(): sirve para obtener el valor de una clave sin generar error y permite colocar un valor por defecto 
# si la clave no existe.



#subir archivos al repo
# git add -A
# git commit -m "feat: actualizacion"
#git push origin main 



# ================================
# STRINGS
# ================================

"""nombre_completo = input("Ingresa tu nombre completo: ")
nombre_limpio = " ".join(nombre_completo.strip().split())
PARTES_MINIMAS = 2

if len(nombre_limpio) == 0:
    print("Error: entrada inválida (cadena vacía)")
elif len(nombre_limpio.split()) < PARTES_MINIMAS:
    print("Error: entrada inválida (ingresa al menos dos palabras)")
else:
    nombre_formateado = nombre_limpio.title()
    partes_nombre = nombre_limpio.split()
    iniciales = ".".join([parte[0].upper() for parte in partes_nombre]) + "."
    print(f"Nombre formateado: {nombre_formateado}")
    print(f"Iniciales: {iniciales}")
"""


# ================================
# BOOLEANOS
# ================================

'''
CERO_ABSOLUTO_C = 273.15
temperatura_c_entrada = input("Ingresa la temperatura en grados Celsius: ")

try:
    temperatura_c = float(temperatura_c_entrada)
except ValueError:
    print("Error: entrada inválida")
    exit()

temperatura_k = temperatura_c + 273.15
if temperatura_k < 0.0:
    print("Error: temperatura por debajo del límite físico")
    exit()

temperatura_f = temperatura_c * 9 / 5 + 32
temperatura_k = temperatura_c + 273.15
es_temperatura_alta = (temperatura_c >= 30.0)

print("Fahrenheit:", temperatura_f)
print("Kelvin:", temperatura_k)
print("¿Es temperatura alta?:", es_temperatura_alta)
'''


# ================================
# LISTAS
# ================================

"""
def procesar_lista_compras(texto_items_iniciales, nuevo_item, item_buscar):
    SEPARADOR = ","

    if texto_items_iniciales.strip() == "":
        print("Error: entrada inválida")
        return

    if nuevo_item.strip() == "":
        print("Error: entrada inválida")
        return

    if item_buscar.strip() == "":
        print("Error: entrada inválida")
        return

    items_crudos = texto_items_iniciales.split(SEPARADOR)
    lista_items = [item.strip() for item in items_crudos if item.strip() != ""]

    lista_items.append(nuevo_item.strip())

    total_items = len(lista_items)
    esta_en_lista = item_buscar.strip() in lista_items

    print("Lista de artículos:", lista_items)
    print("Total de artículos:", total_items)
    print("Artículo encontrado:", esta_en_lista)
"""


# ================================
# BUCLES
# ================================

"""
VALOR_SENTINELA = -1.0

conteo = 0
suma_total = 0.0

while True:
    entrada_numero = input("Ingresa un número: ").strip()
    try:
        numero = float(entrada_numero)
    except:
        print("Error: entrada inválida")
        continue

    if numero == VALOR_SENTINELA:
        break

    conteo = conteo + 1
    suma_total = suma_total + numero

if conteo == 0:
    print("Error: no hay datos")
else:
    valor_promedio = suma_total / conteo
    print("Cantidad:", conteo)
    print("Promedio:", valor_promedio)
"""
