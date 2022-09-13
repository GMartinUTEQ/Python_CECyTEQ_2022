# Programa de nómina e impuestos.
# Obtener las horas trabajadas a la semana y el sueldo por hora
# Si sueldo <= 500 Impuesto será del 10%
# Si el sueldo > 500 Empuesto será 10% Hasta los 500 y el 5% por el excedente
# Mostrar el total a pagar que es equivalente al sueldo menos impuestos

HorasT = int(
    input("Ingrese el número de horas trabajadas en la semana (Entero): "))
SueldoXH = int(input("Escriba el sueldo por hora (Entero): "))
Sueldo = (HorasT * SueldoXH)
if Sueldo <= 500:
    Impuesto = Sueldo * .10
    Sueldo = Sueldo - Impuesto
    print(Sueldo)
else:
    if Sueldo > 500:
        Impuesto = (Sueldo - 500) * .05
        Sueldo = Sueldo - (500 * .10)
        Sueldo = Sueldo - Impuesto
        print(Sueldo)
