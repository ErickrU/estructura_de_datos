class Nodo(object):
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1
    
    def iterar(self):
        actual = self.cabeza

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    def insertar_inicio(self, dato):
        if self.cabeza is not None:
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

            self.contador += 1
    
    def buscar(self, dato):
        for d in self.iterar():
            if dato == d:
                return True
        
        return False
    
    def eliminar(self, dato):
        actual = self.cabeza
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            eliminado = True
        elif self.cola.dato == dato:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        
        if eliminado:
            self.contador -= 1

numeros = ListaDoblementeEnlazada()
print('contador registros: ', numeros.contador)


print()

numeros.insertar(2)
numeros.insertar(3)
numeros.insertar(5)
numeros.insertar(7)
numeros.insertar(11)

print('registros actuales:', numeros.contador)

print()

for d in numeros.iterar():
    print(d)

print()

numeros.insertar_inicio(0)
numeros.insertar_inicio(1)

print('nuemro de registros despues de la insercion al inicio:', numeros.contador)

print()

for d in numeros.iterar():
    print(d)

print()

numero = 10
print(str(numero)+' esta en la lista: ', numeros.buscar(numero))

print()

numero2 = 11
numero = 1
numeros.eliminar(numero)
print('el elemento de la lista con el valor de '+str(numero)+' fue eliminado\nnumero actual de registros: ', numeros.contador)
print()
print('existe un registro con el valor '+str(numero)+': ', numeros.buscar(numero))
print('existe un registro con el valor '+str(numero2)+': ', numeros.buscar(numero2), '\n')
