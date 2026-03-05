# Ejercicio 5: Sumar del 1 al N
# Pseudocódigo:
# INICIO
#   LEER N
#   suma = 0
#   PARA i DESDE 1 HASTA N HACER
#       suma = suma + i
#   FIN PARA
#   MOSTRAR "La suma es: " + suma
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2025]

N = int(input("Ingresa un número N: "))
suma = 0
for i in range(1, N + 1):
    suma += i
print(f"La suma de 1 hasta {N} es: {suma}")