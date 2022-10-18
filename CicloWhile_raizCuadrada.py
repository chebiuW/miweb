

# Ejercicio: calculo raiz cuadrada

import math

numero = float(input("Ingrese un numero: "))
intentos = 0
resultado = 0

while intentos < 2:
    if numero < 0:
        print("No se puede hallar la raiz cuadrada de un numero negativo")
        print("Ud. tiene tres intentos")
        intentos+=1
        numero = float(input("Ingrese un numero: "))
    else:
        resultado = math.sqrt(numero)
        break
        

if intentos < 2:
    print(f"La raiz cuadrada de {numero} es: {resultado}")
else:
    print("Ud. ha superado el numero de intentos permitidos")
    