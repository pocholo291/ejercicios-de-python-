"""5. Almacenar en una lista de 10 posiciones los 10 primeros números primos comprendidos
entre 100 y 300. Luego mostrarlos en pantalla."""

try:
	lista = []
	cont = 0

	for i in range(100, 300 + 1):
		contador = 0

		for j in range(2,(i//2) + 1):
			if i % j == 0:
				contador += 1

		if contador == 0:
			if cont < 10:
				lista.append(i)
				cont +=1 

	print("Los primeros diez numeros primos entre 100 y 300 son: ",lista)

except ValueError:
	print("Error...")