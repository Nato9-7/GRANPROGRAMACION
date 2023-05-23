num=int(input("Ingrese un número positivo: "))
i=1
while num<0:
    num=int(input("Erro! ingrese un número positivo por favor: "))

for i in range (11):
    mult=num*i
    print(f"{num}*{i} = {mult}")
    i+=1
