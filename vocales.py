letras=0
vocal=0
consonante=0
for i in range(10):
    letra=str(input("Ingrese una letra: "))

    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        vocal+=1

    else:
        consonante+=1

print(f"cantidad de vocales es: {vocal} \ncantidad de consonantes es: {consonante}")