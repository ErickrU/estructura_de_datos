from queue import Queue #usamos la libreria Queue

q = Queue(maxsize = 3) #el tamaño maximo de la cola si tambein si no quiseramosq eu tenga limite solo no le pasamos el parametro maxsize

print(q.qsize()) #el tamaña actual de la cola
print(list(q.queue))
q.put(1)# agregar elementos a la cola
q.put('b')
q.put(0.5)
print(list(q.queue)) #valores en la cola

print("\nFull: ", q.full()) #aqui imprimimos si la cola esta llena
print("\nElements dequeued from the queue") #elementos que van a ser eliminados de la cola
print(q.pop()) #nos retorna el valor y lo elimina de la cola
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty()) #booleano de si es que esta vacia la cola

q.put(1) 
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
print(list(q.queue))