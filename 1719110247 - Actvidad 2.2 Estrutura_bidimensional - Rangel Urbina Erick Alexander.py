import numpy 

#arreglo a lista
'''a = numpy.array([1, 2, 3, 4, 5])
print("Array to list = ", a.tolist())#uso de la palabra resevada nombrematriz.tolist() de la libreria numpy'''

#lista a arreglo
'''l = [1, 2, 3, 4, 5]
a = numpy.array(l)#uso de la librerianumpy con numpy.array(nombre de la lista)'''

#eliminar una fila
'''a = numpy.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])
newArray = numpy.delete(a, 1, axis = 0)#especificamos con delete(matriz, numero de la fila,eje)
print(newArray)'''

#eliminar elemntos
'''a = numpy.array([1, 2, 3])
newArray = numpy.delete(a, 1, axis = 0)#eliminamos un elemento de un lista por su posicion
print(newArray)'''

#agregar una lista a un conjunto de listas 
'''a = numpy.array([[1, 2, 3], [4, 5, 6]])
newArray = numpy.append(a, [[50, 60, 70]], axis = 0)#en esta matriz agregamos una lista al eje 0 nota: si qusiera ser para el eje 2 los elementos deben ser los mismos ese decir 1x1 2x2 3x3
print(newArray)'''

#insertar
'''a = numpy.array([1, 2, 3])
newArray = numpy.insert(a, 1, 90)#agregar un lemento a una lista mediante posicion
print(newArray)'''

#agregar a una lista de una nuevos elementos
'''a = numpy.array([1, 2, 3])
newArray = numpy.append (a, [10, 11, 12])#funcion append elementos de una lista a otra R una sola lista
print(newArray)'''

#agregar a la columna(mismas dimensiones ej 3x3)
'''a = numpy.array([[1, 2, 3], [4, 5, 6],[0,2,52]])#una matriz con 3 ejes y una fila de 3 elementos
b = numpy.array([[400], [800], [0]])#una matriz de 3 ejes y una fila con 1 elemnto
newArray = numpy.append(a, b, axis = 1)#funcion append de un elemento a la fila de todos los ejes
print(newArray)'''

#de dos listas hacerlas una misma
'''a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([10, 20, 30, 40, 50])#dos matrices de un eje y una filla con 5 elementos convertidas en una sola con la funcion append
newArray = numpy.append(a, b)
print("The new array = ", newArray)'''