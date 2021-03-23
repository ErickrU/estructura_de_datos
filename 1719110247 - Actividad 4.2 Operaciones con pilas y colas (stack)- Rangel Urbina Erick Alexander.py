from queue import LifoQueue

print('Bienvenido a capas.py\n')
x = int(input("cuantas capas quiere en su programa: "))
stack = LifoQueue(maxsize = x)
c = 0

for i in range (x):
    data = str(input('capa '+str(c+1)+': '))
    stack.put(data)


print('\nlos valores en la cola son: \n',stack.queue)

print("\npila llena: ", stack.full()) 
print("capas: ", stack.qsize()) 

d = str(input('\ndesea eliminar una capa y/n: '))
if d == 'y':
    try:
        df = int(input('cuantas capas quiere eliminar: '))
        if df > stack.qsize() or df >= -1:
            print('no puedes borrar mas capas de las que tienes o restar capas negativas')
        else:    
            for i in range (df):
                stack.get()
    except:
        print('algo salio mal :P')
else:
    pass

print('\nelementos actuales en la pila',stack.queue)