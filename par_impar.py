num=int(input("Ingrese un número entre 1 y 101\n"))

while num<1 or num>101:
    print("Error número ingresado no es valido")
    num=int(input("Ingrese un número entre 1 y 101\n"))

if (num%2==0):
    print("El número ingresado es par")

elif(num%2==1):
    print("El número ingresado es impar")