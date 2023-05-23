print("Bienvenido a su delivery, por favor ingrese lo que va a llevar")
print("Opcion1 = Churrasco a $1.500\nOpcion2 = Completo a $1000\nOpcion3 = Vegetariano a $2000\nOpcion4 = Barros Luco a $3000\nOpcion5 = Salir")
chu=0
com=0
vege=0
barr=0
precio=0
opcion=int(input())

while opcion!=5:
    if opcion==1:
        precio+=1500
        chu+=1

    elif opcion==2:
       precio+=1000
       com+=1
    
    elif opcion==3:
        precio+=2000
        vege+=1
    
    elif opcion==4:
        precio+=3000
        barr+=1
    opcion=int(input())

cod=str(input("Posee codigo de descuento? (ingrese si o no)\n:"))

if cod=="si":
    precio=precio-(precio*0.10)

print(f"Usted lleva:\n{chu} churrascos\n{com} completos\n{vege} vegetarianos\n{barr} barros lucos")
print(f"Todo por ${precio}")