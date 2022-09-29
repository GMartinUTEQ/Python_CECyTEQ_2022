
# FileName: hola_mundo <- Sneak Case.
# Class: HolaMundo <- Camel Case.


class Cafepoo:
    # Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # función o Método
    def revisar_presupuesto(self, presupuesto):
        if not isinstance(presupuesto, (int, float)):
            print("Escriba un número entero o un número con decimales")
            exit()

        if presupuesto < 35:
            print("Lo siento, no te alcanza para un café")
            exit()

    # función o Método
    def obtener_cambio(self, presupuesto):
        return presupuesto - self.precio

    def vender(self, presupuesto):
        self.revisar_presupuesto(presupuesto)
        if (presupuesto >= self.precio):
            print(f"Puedes comprar el café {self.nombre}")
            if presupuesto == self.precio:
                print("Importe exacto.")
            else:
                print("Tu cambio es: $", self.obtener_cambio(presupuesto))
            return presupuesto - self.precio
            #exit("Gracias por su compra.")


mediano = Cafepoo("Mediano", 50)
grande = Cafepoo("Grande", 60)
chico = Cafepoo("Chico", 35)

#a = [mediano, chico, grande]

try:
    presupuesto = float(input("Cual es tu presupuesto ?: "))
except:
    exit("El sistema solo recibe números")

for cafe in [mediano, chico, grande]:
    presupuesto = cafe.vender(presupuesto)

    print(presupuesto)
