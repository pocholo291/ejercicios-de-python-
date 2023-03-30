# 15 leer 10 numero enteros alamacenarlo en una rylista y determinar cuantos datos almacenados son multiplos de 3

try:
	lista = []
	cont = 0

	for i in range(10):
	    numero = int (input("ingrese un numero entero:"))
	    lista.append(numero)
	print("La lista es:",lista)

	for j in range (len(lista)):
	    if lista[j] % 3 == 0:
	       cont += 1
	print(" la cantidad de numeros que son multplos de 3 son:",cont)


except ValueError:
   print("Error...") 
 
