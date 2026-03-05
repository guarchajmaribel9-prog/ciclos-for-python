# Ejercicio 6: Contar vocales en una palabra
# Pseudocódigo:
# INICIO
#   LEER palabra
#   contador = 0
#   vocales = ["a", "e", "i", "o", "u"]
#   PARA cada letra EN palabra HACER
#       SI letra ESTÁ EN vocales ENTONCES
#           contador = contador + 1
#       FIN SI
#   FIN PARA
#   MOSTRAR "La palabra tiene " + contador + " vocales"
# FIN
# Nombre: [Karla Catalina Maribel Guarchaj Ixquiactap]
# Fecha: [06/03/2026]

palabra = input("Ingresa una palabra: ").lower()
contador = 0
vocales = ["a", "e", "i", "o", "u"]
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"La palabra tiene {contador} vocales")