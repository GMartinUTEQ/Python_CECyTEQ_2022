import random

valor = random.randint(1, 100)

terminado = 0

while terminado == 0:
    num = int(input("Escribe el número: "))
    if num == valor:
        print("Ya ganaste !!")
        terminado = 1
    else:
        if num > valor:
            print("Menor")
        else:
            print("Mayor")
