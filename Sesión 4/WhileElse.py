# Programa que dada una lista sepamos si un valor se encuentra en la lista

x = int(input("Escriba el valor a encontrar: "))
valores = [5, 1, 8, 2, 7, 4]

indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if (valor == x):
        print(f"el elemento {x} ha sido encontrado en el indice {indice}")
        break
    else:
        indice += 1
else:
    print(f"El elemento {x} no se encuentra en la lista de valores")
