 zap=20000

cant=int(input("Ingrese cantidad de zapatos a comprar\n:"))
precio=cant*zap

if precio>=40000:
    print(f"El precio a cancelar es de {precio}")

else:
    print(f"El precio a cancelar es de {(precio+3000)}")

