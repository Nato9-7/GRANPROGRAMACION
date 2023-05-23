num=int(input("Ingrese un número: "));

cont=1;
fact=num;

while cont<num:
    fact=cont*fact
    cont+=1
  
print(f"El factorial de {num} es : {fact}")