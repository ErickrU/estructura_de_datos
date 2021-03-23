class stack(object): #clase pila
    
    def __init__(self):
        self.items=[] #como las pilas en python no existe pdoemos usar las listas para simular una pila

    def push(self, dato): #apilamos el valor que nos pasa el usarioe en la pila
        self.items.append(dato) #basta con un append sobre la lista

    def pop(self): 
        if self.empty(): #en caso de no haber nada pues no regresamos nada
            return None
        else:
            return self.items.pop() #pop eliminamos el ultimo valor

    def empty(self): 
        if len(self.items)==0: #si no hay nada en la longitud de la lista no hay nada
            return True
        else: #contrario tenemos algo
            return False
        
    def size(self):  #sin mas imprimimos la lista
        print(self.items)

obj = stack()
print(obj.empty())
obj.push(15)
obj.push(25)
obj.push(35)
obj.push(15)
print(obj.empty())
obj.size()
print(obj.pop())
obj.size()
print(obj.pop())
obj.size()