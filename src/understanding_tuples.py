"""
las tuplas son listas de emnetos que no pueden cambiar su tamaño.}
las tuplas son lkistas inmutables.

se utilizan () para definir una tupla.

ejemplo:
"""
#rectangulo (largo, ancho)
rectangle_dimensions = (200,50) #tupla
print(f"largo: {rectangle_dimensions[0]}mm") #200
print(f"ancho: {rectangle_dimensions[1]}mm") #50


#intentando modificar un elemento de la tupla
#la tupla no se puede modificar ni agregar elementos nuevos 
#rectangle_dimensions[0] = 250 #esto genera un error

for dimension in rectangle_dimensions:
    print(dimension)

    """
    no podemos modificar una tupla, ni tampoco/eliminar elementos.
    lo que si podemos hacer es cambiar la asignacion a una variable que almacena una tupla.

    """

rectangle_dimensions = (300,150) #tupla aun se pueden cambiar las diemciones (agregarle otros elemnetos)

