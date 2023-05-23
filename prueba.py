num = int(input("Ingrese un número entero positivo entre 103 y 987: "))

# Invertir el número
num_invertido = 0
while num > 0:
    num_invertido = (num_invertido * 10) + (num % 10)
    num //= 10

# Aplicar las 4 operaciones matemáticas básicas
suma = num + num_invertido
resta = num - num_invertido
multiplicacion = num * num_invertido
division = num / num_invertido

# Mostrar el resultado
print("El número invertido es:", num_invertido)
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)