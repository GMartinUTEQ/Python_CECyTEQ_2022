# Ejercicio que dado los ejes X y Y nos indique en que cuadrante se encuentra.
#

continuar = 1

while continuar == 1:
    x = int(input("Escriba el valor de la coordenada X: "))
    y = int(input("Escriba el valor de la coordenada Y: "))

    if x == 0 and y == 0:
        print("Se encuentra en el Origen.")
    else:
        if x > 0 and y > 0:
            print("Se encuentra en el cuadrante 1.")
        else:
            if x < 0 and y > 0:
                print("Se encuentra en el cuadrante 2.")
            else:
                if x < 0 and y < 0:
                    print("Se encuentra en el cuadrante 3.")
                else:
                    print("Se encuentra en el cuadrante 4.")
    continuar = int(input("Si desea continuar presione 1, si no, presione 0"))

print("Gracias por usar nuestro sistema")
