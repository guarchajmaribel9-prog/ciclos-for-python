# Ejercicio 10: Lista y suma de compras
# Pseudocódigo:
# INICIO
#   LEER N
#   total = 0
#   PARA i DESDE 1 HASTA N HACER
#       LEER precio
#       total = total + precio
#   FIN PARA
#   MOSTRAR "El total a pagar es: " + total
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

N = int(input("¿Cuántos productos vas a ingresar? "))
total = 0
for i in range(1, N + 1):
    precio = float(input(f"Ingresa el precio del producto {i}: "))
    total += precio
print(f"El total a pagar es: ${total:.2f}")