# Ejercicio 7: Promedio de 5 notas
# Pseudocódigo:
# INICIO
#   suma_notas = 0
#   PARA i DESDE 1 HASTA 5 HACER
#       LEER nota
#       suma_notas = suma_notas + nota
#   FIN PARA
#   promedio = suma_notas / 5
#   MOSTRAR "El promedio es: " + promedio
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

suma_notas = 0
for i in range(1, 6):
    nota = float(input(f"Ingresa la nota {i}: "))
    suma_notas += nota
promedio = suma_notas / 5
print(f"El promedio de las 5 notas es: {promedio:.2f}")