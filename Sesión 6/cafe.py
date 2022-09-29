chico = 35
mediano = 50
grande = 65

presupuesto = input("Cuanto es tu presupuesto ?: ")

try:
    presupuesto = int(presupuesto)
except:
    print("Lo lamento, el sistema solo usa numeros enteros")
    exit()

if presupuesto >= 35:
    if presupuesto >= grande:
        print("Puedes comprar un café grande")
        if presupuesto == grande:
            print("Importe exacto")
        else:
            print("Tu cambio es de: ", presupuesto - grande)
    elif presupuesto >= mediano:
        print("Puedes comprar un café mediano")
        if presupuesto == mediano:
            print("Importe exacto")
        else:
            print("Tu cambio es de: ", presupuesto - mediano)
    elif presupuesto >= chico:
        print("Puedes comprar un café chico")
        if presupuesto == chico:
            print("Importe exacto")
        else:
            print("Tu cambio es de: ", presupuesto - chico)
else:
    print("Lo siento, no te alcanza.")
