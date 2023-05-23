i=0
promedio=0
for i in range (3):
    nota=float(input("Ingrese su nota: "))
    while nota<=0 or nota > 7:
        print("ERROR! la nota ingresada no es valida, por favor ingrese nuevamente")
        nota=float(input("Ingrese su nota: "))
    promedio+=nota

promedio=promedio/3

if promedio>=4:
    print("Usted esta aprobado")

else:
    print("Usted no ha aprobado")

