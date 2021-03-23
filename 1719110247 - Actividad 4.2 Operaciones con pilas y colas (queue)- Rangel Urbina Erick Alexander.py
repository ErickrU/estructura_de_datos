from collections import deque
import collections

MyQueue = collections.deque([])
print('bienvenido al agendador de citas del dia CONSULTORIO 0')

def citasDelDia ():
    try:
        cdd = int(input('\ncitas del dia: '))
        return cdd
    except:
        print('\nesperaba un numero mayore o igual a 1')
        

def iniciador():
    try:
        xqc = int(citasDelDia())
        if xqc >= 1:
            c = 0
            for i in range (xqc):
                value = int(input('cita '+str(c+1)+': '))
                MyQueue.append(value)
    except:
        print('\nnumeros no letras')

def siguiente():
    try:
        MyQueue.popleft()
    except:
        print('\nnada que borrar')

def descartarId():
    try: 
        if MyQueue[0] != 0:
            id = int(input('\nid que deseas eliminar: '))
            MyQueue.remove(id)
    except:
        print('\ncreo que ese valor no existe :~)')

def verAgenda():
    print('\n',MyQueue)

iniciador()
verAgenda()
siguiente()
verAgenda()
descartarId()
verAgenda()