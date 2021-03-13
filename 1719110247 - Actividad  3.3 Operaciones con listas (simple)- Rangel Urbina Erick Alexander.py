class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamaño += 1

        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    
    def iterar(self):
        actual = self.cola

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        
        return False

    def eliminar_dato(self, dato):
        actual = self.cola
        anterior = self.cola

        while actual:
            if actual.dato == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    # [2]->[3]->[5] => [2]->[5]
                    anterior.siguiente = actual.siguiente
                self.tamaño -= 1
                return
            anterior = actual
            actual = actual.siguiente


numeros = ListaEnlazada()
numeros.insertar(1719110247)
numeros.insertar(1745158420)

print('ordenes de compra dia 1: %i' % numeros.tamaño)

print()

for d in numeros.iterar():
    print(d)

print()

numeros.insertar(51651079852)
numeros.insertar(45618671874)
numeros.insertar(30541815851)

print('ordenes de compra dia 2: %i' % numeros.tamaño)

print()

for d in numeros.iterar():
    print(d)

c = 30541815851

print("\nEliminar compra: "+str(c)+" \n")

numeros.eliminar_dato(c)

for d in numeros.iterar():
    print(d)

n = 11

print('Existe la orden? '+str(n), numeros.buscar(n))