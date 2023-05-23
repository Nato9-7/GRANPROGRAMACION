print("Ingrese 5 números")
mayor=0
menor=0
igual=0
for i in range (5):
    num=int(input(" "))

    if num>0:
        mayor+=1
    
    elif num<0:
        menor+=1

    elif num==0:
        igual+=1

print(f"mayor a cero = {mayor} \nmenores a cero = {menor} \niguales a cero = {igual}")