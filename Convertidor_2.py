print("Bienvenido al convertidor. Por favor elija una opcion:");
print("Opcion1 = USD a CLP","\nOpcion2 = ARG a CLP","\nOpcion3 = CLP A USD");
opcion=int(input());

if opcion==1:
    usd=float(input("Ingrese la cantidad de USD: "))
    con=usd*794.61
    print(f"La cantidad ingresada equivale a {con}")

elif opcion==2:
    arg=float(input("Ingrese la cantida de ARG: "))
    con=arg*3.64
    print(f"La cantidad ingresada equivale a {con}")

elif opcion==3:
    clp=float(input("Ingrese la cantida de CLP: "))
    con=clp*0.0013
    print(f"La cantidad ingresada equivale a {con}")