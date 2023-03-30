""" 6 leer dos números enteros y almacenar en una lista los 10 primeros números primos compredididos entre el menor y el mayor.Luego mostrarlo en pantalla."""

try:
	lista = []
	numero1 = int(input("Ingrese un numero entero: "))
	numero2 = int(input("Ingrese un numero entero: "))
	cont_primos = 0

	if numero2 > numero1:
		for i in range(numero1, numero2 + 1):
			cont = 0
			for j in range(2, i//2 + 1):
				if i % j == 0:
					cont += 1
			if cont == 0 and i != 1 and i != 0:
				if cont_primos < 10:
					lista.append(i)
					cont_primos += 1
		print("Los diez primeros numeros primos comprendidos entre",numero1,"y",numero2,"son: ",lista)

	else:
		for i in range(numero2, numero1 + 1):
			cont = 0
			for j in range(2, i//2 + 1):
				if i % j == 0:
					cont += 1
			if cont == 0 and i != 1 and i != 0:
				if cont_primos < 10:
					lista.append(i)
					cont_primos += 1
		print("Los diez primeros numeros primos comprendidos entre",numero2,"y",numero1,"son: ",lista)

except ValueError:
	print("Error...")
  

  
