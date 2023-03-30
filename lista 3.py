"""3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
el mayor número primo leído."""

try:
	lista = []
	numero = 0
	pos = 0
	mayor = 0

	for i in range(10):
		num = int(input("Ingrese un numero entero: "))
		lista.append(num)
	print("La lista original es: ",lista)

	for j in range(len(lista)):
		numero = lista[j]
		cont = 0
		for k in range(2,(numero//2) +1):
			if numero % k == 0:
				cont +=1

		if cont == 0:
			aux = numero
			pos = j
			if aux > mayor:
				mayor = aux
				posicion = pos

	print("El numero primo mayor es: ",mayor)
	print("El numero primo mayor se encuentra en la posicion: ",posicion)
	
except ValueError:
	print("Error...")