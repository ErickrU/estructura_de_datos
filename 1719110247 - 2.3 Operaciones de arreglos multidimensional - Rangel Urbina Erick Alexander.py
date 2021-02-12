#python 3
import numpy as np

'''arrayOnes  = np.ones((10,10))#esta es  la estructura de un arreglo multidimensional ya que contamos con 10 listas de una fila y con 10 columna y con la funcionones de la libreria numpy hacemos que la tabla que generamos todos sus valores sean igual a uno
print(arrayOnes)'''

'''arrayR = np.arange(90)#con la funcion arange generamos una lista con n numero de elementos en este caso 90
arrayR = arrayR.reshape(9,10)#con la funcion reshape le diremos que restruture todo la matriz con los valores que le pasemos es decir en este caso le solicitamos 9 listas con 10 columnas   
print(arrayR)'''

'''arrayR2 = np.arange(90)
arrayR2 = arrayR2.reshape(9,2,5)#ahora lo que pedimos con la funcion reshape es que nos de 9 listas con 2 filas de 5 clumnas 
print(arrayR2)
print(arrayR2[4][0][2])#ahora supongamos que queremos buscar el elemento 42 de la matriz arrayR2 bien para ello le diremos que vaya a la cuarta lista a la fila uno y me pase la columna 2
'''

'''a = np.arange(30)
b = a.reshape((2, -1, 3))  # -1 nos indica que sean las filas necesarias
print(b.shape)#por cierto con la funcion shape vemos la estructura de la matriz
print(b)'''