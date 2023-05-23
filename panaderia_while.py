opcion = 0
print("BENVENID@ A PANADERIA NATO\n")

amasado=1500
molde=1000
integral=3000
bagette=2000
suma=0

flag=True


a=0
m=0
b=0
i=0

while flag==True:

    menu=int(input("(1)Comprar pan \n(2)Emitir boleta \n(3)Salir \nElegir aca: "))
    print("")

    if menu==1:
     while opcion != 5:
      try:
        opcion=int(input("(1)Amasado = 1.500 \n(2)Molde = 1.000 \n(3)Baguette = 2.000  \n(4)Integral = 3.000 \n(5)Para salir  \nIngresar Opcion: "))

        if opcion == 1:
            cantidad=int(input("Cuanta cantidad de pan desea: "))
            a+=cantidad
            suma+=amasado*cantidad

        elif opcion == 2:
           cantidad=int(input("Cuanta cantidad de pan desea: "))
           m+=cantidad
           suma+=molde*cantidad
    
        elif opcion == 3:
            cantidad=int(input("Cuanta cantidad de pan desea: "))
            b+=cantidad
            suma+=bagette*cantidad

        elif opcion == 4:
           cantidad=int(input("Cuanta cantidad de pan desea: "))
           i+=cantidad
           suma+=integral*cantidad

        print("")

      except ValueError:
        print("Valor invalido")

    elif menu==2:
        print(f"Usted compro: \n{a} pan amasados \n{m} pan molde \n{b} pan baguette \n{i} pan integral")

        print(f"El total de su compra es de: {suma}.\n")
        
        if suma>5000:
            print(f"Su compra supera los $5.000 por lo que no se le agregara una comision del 10%. \nEl precio total de su compra es de : {suma}")

        else:
            print(f"El precio total de su compra es de: {(suma*0.10)+suma}")
        
        flag=False

    elif menu==3:
       flag=False

       
    
        

    


