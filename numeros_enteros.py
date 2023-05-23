x=int(input("Ingrese un número: "))
y=int(input("Ingrese su segundo número: "))

if x>y:
    print(f"El número ingresado {x} es mayor a {y}")

elif x==y or y==x:
    print("Los números ingresados son iguales")

else:
    print(f"El número ingresado {y} es mayor a {x}")