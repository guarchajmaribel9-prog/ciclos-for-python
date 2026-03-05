# Ejercicio 9: Contar positivos, negativos y ceros
# Pseudocódigo:
# INICIO
#   positivos = 0
#   negativos = 0
#   ceros = 0
#   PARA i DESDE 1 HASTA 10 HACER
#       LEER numero
#       SI numero > 0 ENTONCES
#           positivos = positivos + 1
#       SINO SI numero < 0 ENTONCES
#           negativos = negativos + 1
#       SINO
#           ceros = ceros + 1
#       FIN SI
#   FIN PARA
#   MOSTRAR "Positivos: " + positivos
#   MOSTRAR "Negativos: " + negativos
#   MOSTRAR "Ceros: " + ceros
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

positivos = 0
negativos = 0
ceros = 0
for i in range(1, 11):
    numero = int(input(f"Ingresa el número {i}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")