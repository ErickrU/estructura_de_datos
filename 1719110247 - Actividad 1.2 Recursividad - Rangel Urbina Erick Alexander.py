'''Py 3.x Elaborar un programa aplicando recursividad explicando en que parte del desarrollo están aplicando el concepto. '''
def main(x):
    if x>0:
        print(x)
        main(x-1)#aqui sucede la recursividad ya que mandamos a llamar a la funcion main dentro de la funcion main
    elif x == 0:
        print("Fin programa")
    else:
        print("Es cuenta regresiva no ascendente")

main(int(input("valor para cuenta regresiva ")))