# Ejercicio 8: Dibujar una escalera de asteriscos
# Pseudocódigo:
# INICIO
#   LEER N
#   PARA i DESDE 1 HASTA N HACER
#       MOSTRAR "*" repetido i veces
#   FIN PARA
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

N = int(input("Ingresa un número N: "))
for i in range(1, N + 1):
    print("*" * i)