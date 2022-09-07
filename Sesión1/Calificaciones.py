# NA No Aprobó     < 7.5
# SA Satisfactorio >= 7.5  <= 8.4
# DE Destacado     >= 8.4  <= 9.4
# AU Autónomo.     >= 9.5
# Operadores && & ||
# Obtener 3 calificaciones, obtener promedio y comparar el promedio.
calif1 = int(input("Escriba la primera calificación"))
calif2 = int(input("Escriba la primera calificación"))
calif3 = int(input("Escriba la primera calificación"))
promedio = (calif1+calif2+calif3) / 3
print(promedio)
if promedio < 7.5:
    print("Tu calificación es NA")
else:
    if promedio >= 7.5:
        if promedio <= 8.4:
            print("Tu calificación es SA")
        else:
            if promedio > 8.4:
                if promedio <= 9.4:
                    print("Tu calificación es DE")
                else:
                    print("Tu calificación es AU")
