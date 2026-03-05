# Ejercicio 4: Tabla de multiplicar
# Pseudocódigo:
# INICIO
#   LEER numero
#   PARA i DESDE 1 HASTA 10 HACER
#       resultado = numero * i
#       MOSTRAR numero + " x " + i + " = " + resultado
#   FIN PARA
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")