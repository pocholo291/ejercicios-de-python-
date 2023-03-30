3# leer un numero entero  y mostrar todos los divisores exactos del numero  compredido  entre 1 y el numero  leido .

try:
	num = int(input("ingrese  un numero entero"))
	print("**************************************************")
	print("Los divisores de",num,"comprendidos entre 1 y",num,"son: ")
	print("**************************************************")
	
	for i in range(1, num + 1):
	    if num % i == 0:
	     print(i)


except ValueError:
   print("error")