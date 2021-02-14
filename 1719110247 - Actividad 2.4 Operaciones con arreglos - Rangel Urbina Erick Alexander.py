import numpy as np
from numpy.lib.function_base import append

#/*************************** Tamaño del arreglo y llenado **************\
cont = 0
values = []
valuesNumpy = np.array([],dtype=object)
elements = int(input("cuantos elementos quieres en tu matriz: "))

for i in range (elements):
    cont += 1
    valR = int(input("Valor "+str(cont)+": "))
    values.append(valR)

sizeList = int(input("\nCuantas listas quieres en la matriz: "))
sizeColum = int(input("Cuantas columnas quieres en cada lista: "))

VLNP = np.array(values)
print(valuesNumpy)
valuesNumpy = np.append(valuesNumpy, VLNP)
print(valuesNumpy)
valuesNumpy = valuesNumpy.reshape((sizeList,sizeColum))
print(valuesNumpy)

#/*************************** Eliminar columna **************\
deleteColum = int(input("\nposicion de la columna que sera eliminada: "))
valuesNumpy = np.delete(valuesNumpy, deleteColum, axis=1)
print(valuesNumpy)

#/*************************** Agregar elementio en posicion **************\
axis = int(input("\nEje en el que se va agregar los lementos: "))
elementsAppend = int(input("cuantos elementos vas agregar: "))
eA = []
cont2 = 0

for i in range (elementsAppend):
    cont2 += 1
    valE = int(input("\nValor "+str(cont2)+": "))
    eA.append(valE)

eANumPy = np.array(eA)
valuesNumpy = np.append(valuesNumpy, [eANumPy], axis=axis)
print(valuesNumpy)

#/*************************** suma de dos matrices **************\
print("\nSuma de matrices")
valuesNumpySum1 = valuesNumpy
valuesNumpySum2 = valuesNumpy
valuesNumpySumResult = np.sum([valuesNumpySum1, valuesNumpySum2], axis=0)
print(valuesNumpySumResult)

#/*************************** Multiplicación de dos matrices **************\
valuesNumpyDot1 = valuesNumpy.reshape(6,2)
valuesNumpyDot2 = valuesNumpy.reshape(2,6)
valuesNumpyDotResult = np.dot(valuesNumpyDot1, valuesNumpyDot2)
print("matrices de 6*2 y 2*6")
print(valuesNumpyDot1)
print()
print(valuesNumpyDot2)
print("\nMultiplicación de matrices")
print(valuesNumpyDotResult)

#/*************************** Invertir  matriz **************\
response = str(input("\ndeseas invertir la matriz (y/n): "))
if response == 'y':
    valuesNumpyVert = valuesNumpy
    valuesNumpyVert = np.flip(valuesNumpy)
    print(valuesNumpyVert)
else:
    print("Ok...")
#/*************************** Invertir  matriz **************\
responsev2 = str(input("\ndeseas generaruna diagonal con tu matriz (y/n): "))
diagflatArray = valuesNumpy
diagflatArray = np.diagflat(diagflatArray)
if responsev2 == 'y':
    print(diagflatArray)
else:
    print("ok...")

#/*************************** modificar arreglos **************\
responsev3 = str(input("\ndeseas modificar algun valor de un arreglo (y/n): "))
while responsev3 == 'y':
    print("\n",valuesNumpy)
    arrowPos = int(input("\nposicion del elemento en la lista que quieres modificar: "))
    columPos = int(input("posicion del elemento en de la columna que quieres modificar: "))
    newValue = int(input("Valor que quieres agregar: "))
    valuesNumpy[arrowPos,columPos] = newValue
    print(valuesNumpy)    
    responsev3 = str(input("\ndeseas modificar otro valor de un arreglo (y/n): "))