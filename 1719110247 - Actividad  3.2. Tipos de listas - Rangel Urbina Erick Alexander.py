##SIMPLEMENTE # ENLAZADA#

class Nodo: # esta clase creara cada nodo 
    
    def __init__(self, dato): #inicicizalizador y le pasamos el dato
        self.dato = dato #variable de instancia del dato obtenido que se llamara dato tambien
        self.siguiente = None #esta nos va decir quien es el nodo siguiente


class ListaEnlazada: 

    def __init__(self): 
        self.cabeza = None #para una lista de este tipo se requiere de cosas una cabeza y una cola por nodo
        self.cola = None 
        self.tamaño = 0 #elementos en la lista
    
    def insertar(self, dato): #agregar elementos a un nodo
        nodo = Nodo(dato) #cada que insertamos creamos un nuevo nodo con la instacia dato requeriada por la clase nodo

        if self.cabeza: #si hay elemento en la cabeza #importante recordar la cabeza y cola son nodos
            self.cabeza.siguiente = nodo #el nodo tomara el lugar en la cabeza del nodo
            self.cabeza = nodo #ahora el nodo sera la cabeza actual

        else: #si no hay nada enteonces toma el valor que le pasamos de dato en nodo
            self.cabeza = nodo 
            self.cola = nodo
    
    def iterar(self): #iterar
        actual = self.cola #la variable almacena el valor del primer elemento que se agrego en la cola del nodo  

        while actual: #mientras tengamos algo
            dato = actual.dato #actual es el objeto de tipo nodo
            actual = actual.siguiente #ahora actual se arrastra al siguiente nodo y ahora ya estariamos en el siguiente nodo 
            yield dato #usamos yield como contador ya que cada que se cree un nodo necesitaremos mas variables

'''
numeros = ListaEnlazada() #creamos un bjeto de la clase esdecir la lista

numeros.insertar(2) #valores de la lista por que la lista esta vacia hasta ahora
numeros.insertar(0)
numeros.insertar(10)
numeros.insertar(9)
numeros.insertar(7)
numeros.insertar(6)
numeros.insertar(5)
numeros.insertar(15)
numeros.insertar(3)

for d in numeros.iterar(): #vereficamos la lista 
    print(d)
'''

#DOBLEMENTE # ENLAZADA#

class Nodo(object): # hereda todo lo que definimos como object esta la podemos considerar la clase madre y esta nosla proporciona python

    def __init__(self, dato=None, siguiente=None, anterior=None): #al no tner info de los nodos los podemos definir com valores nulos
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior #ahora agregamos el backsite de un nodo para saber su predesecor ya que es una lista doblemente enlazada

class ListaDoblementeEnlazada(object): #

    def __init__(self): 
        self.cabeza = None #el ultimo elemento agregado a la lista 
        self.cola = None #primer elemento que agregamos a la lista
        self.contador = 0 #contador ya que no hay nodos en la lista al inicio
    
    def insertar(self, dato):
        nodo = Nodo(dato) #nodo va ser un objeto de la clase nodo que lo nombramos nodo

        if self.cabeza is None: #si no hay ninguno elemento en la lista 
            self.cabeza = nodo #le asiganos un valor a la cabeza 
            self.cola = self.cabeza #y este es el regreso 

        else: #si hay
            nodo.anterior = self.cola #el nodo anterior ahora apunta hacia la cola 
            self.cola.siguiente = nodo #la antigua cola sera la neuva cabeza del sig nodo
            self.cola = nodo #y ahora cola se convierte en el nodo actual
        
        self.contador += 1 #contador los nodos
    
    def iterar(self):  
        actual = self.cabeza #iteracion

        while actual: 
            dato = actual.dato #que dato hay en el nodo actual
            actual = actual.siguiente #el siguiente nodo 
            yield dato 

'''
numeros = ListaDoblementeEnlazada()
print('Cantidad después de crear la lista:', numeros.contador)
numeros.insertar(2)
print('Cantidad después de insertar un elemento en la lista:', numeros.contador)

print()

numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)

print('Cantidad actual de elementos:', numeros.contador)

print()

for d in numeros.iterar(): #iteracion
    print(d)
'''

#DOBLEMENTE # ENLAZADA#
class Node(object): #clase nodo
    def __init__(self, data):
        self.data = data
        self.next = None
 
class create_circular_linked_list(object):
    
    def __init__(self):
        self.head = None
 
    def is_empty(self):
        return self.head is None 
 
    def length(self): #longitud de la lista circular 
        cur = self.head #toma el valor de de la cabeza del nodo
        count = 0 #contador
        while cur is not None: #si no hay nada en el nodo actual sumar mas 1 
            count += 1
            if cur.next == self.head: #buscar el siguiente nodo para saber si es la cola 
                break
            else: #contrario
                cur = cur.next
        return count
 
    def add_first(self, data):
        node = Node(data) #un objeto
        if self.is_empty():  #si esta vacia then:
            self.head = node #el nodo toma el lugar de la cabeza 
            node.next = self.head #se convierte en el siguiente 
        else: # si no esta vacia
            cur = self.head
            while cur.next is not self.head: # mover el puntero a la nueva cola 
                cur = cur.next
            cur.next = node 
            node.next = self.head #cambiar puntero de cabeza
            self.head = node
 
    def insert_node(self, index, data): #insertar nodo con todo e info
        node = Node(data) #obj
        if index < 0 or index > self.length():  #error de insercion posición del índice no está dentro de la longitud de la lista vinculada
            print ("Posición de inserción incorrecta")
            return False
        elif index == 0: #insertar en la cabeza 
            self.add_first(data) 
        else: #insertar en medio
            cur = self.head #puntero en posicon de insercion
            pre = None #nodo anterior
            count = 0
            while count < index:
                pre = cur
                cur = cur.next #el nuevo nodo apunta al orginal donde se agrego el que se esta crando
                count += 1
            pre.next = node
            node.next = cur
 
    def travel(self):
        if self.is_empty(): #si esta vacia
            return
        cur = self.head
        print(cur.data) 
        while cur.next != self.head: #nodo a nodo
            cur = cur.next
            print(cur.data) #imprimir todos los nodos
 
''' 
lists = create_circular_linked_list()
lists.add_first(1)
lists.add_first(0)
lists.insert_node(2, 8)
lists.travel()
print ("Longitud de la lista:", lists.length ())
lists.travel()
'''