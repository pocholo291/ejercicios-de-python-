# 8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200

try:
	print("Los numeros pares comprendidos entre 20 y 200 son: ")
	for i in range(20, 200 + 1, 2):
		print(i)

except ValueError:
	print("Error...")