
# Ejercicio: sacar licencia de conducir desde 16 años con autorización de los padres

import sys
     

band = "s"
while band == "s":
        
 nombre = input("Ingrese su nombre: ")
 edad = int(input("Ingrese su edad: "))

 if edad >= 16 and edad <= 18: # Menor de edad
     print("Usted puede sacar su licencia de conducir con autorizacion de sus padres")
    
 
 elif edad > 18 and edad <= 60: # Mayor de edad
     print("Usted puede sacar la licencia de conducir")
     
 
 else:
    if edad < 16 or edad > 60: # No habilitados
        print("Usted no puede sacar la licencia de conducir")
band = print(input("Desea continuar? s/n: " ))
sys.stdout.flush()

 
    