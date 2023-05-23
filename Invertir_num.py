num = int(input("Ingrese un número entre 103 y 987: "))

while num<103 or num>987:
    print("Ingrese entre el rango pedido")
    num=int(input())
    
i=0
invertido=0
while i<3:
    invertido=(invertido*10)+(num % 10)
    num=num//10
    i+=1

print(invertido)


