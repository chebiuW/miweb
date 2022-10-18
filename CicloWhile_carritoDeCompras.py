
# Ejercicio: carrito de compras


from calendar import c


productos = {}
codigoArticulo  = ""
producto = ""
precioProducto = 0
compraTotal = 0
band = "s"

while band == "s":
    
    codigoArticulo = input("Ingrese código de Articulo: ")
    producto = input("Ingrese el nombre del producto: ")
    precioProducto = int(input("Ingrese el precio: $"))
    
    productos[codigoArticulo] = []
    productos[codigoArticulo]
    compraTotal+= precioProducto
    
    band = (input("Desea continuar? s/n")).lower()

print("Compra:")
print(f"Lista de productos: {productos}")
print(f"Compra total: ${compraTotal}")
    



""" print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor "))
intentos=0
while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	print("")
	print("Ingrese un numero positivo ")
	print("Tiene tres intentos  ")
if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizando")
		break;
	numero=int(input("Introduce un numero por favor: "))	
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de "+str(numero)+" es "+ str(solucion))
 """