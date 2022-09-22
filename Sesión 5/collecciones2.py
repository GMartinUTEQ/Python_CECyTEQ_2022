from collections import deque

letras = deque("dabde")

letras.insert(2, "c")

print(letras)

letras.remove("d")  # <- Elimina el elemento.

print(letras)

print(letras[1])

# Lenguaje con posición 0.

del letras[2]  # <- El elmento que está en esa posición

print(letras)
