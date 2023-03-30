"""4. Cargar una lista de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci
y mostrarlo en pantalla."""

try:
	lista = []
	a = 0
	b = 1

	lista.append(a)
	lista.append(b)
	
	for i in range(8):
		c = a + b
		a = b
		b = c
		lista.append(c)

	print("Los primeros diez elementos de la serie fibonacci son: ",lista)

except ValueError:
	print("Error...")