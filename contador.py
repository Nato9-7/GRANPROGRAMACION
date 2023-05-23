num1=int(input("Ingrese un número: "));
num2=int(input("Ingrese un número: "));
num3=int(input("Ingrese un número: "));

suma=0;

if num1%2==0:
    suma+=num1;
if num2%2==0:
    suma+=num2;
if num3%2==0:
    suma+=num3;

print(suma)