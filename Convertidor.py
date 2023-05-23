print("Bienvenido al convertidor. Por favor elija una opcion:");
print("Opcion1 = AUD a CLP","\nOpcion2 = ARG a CLP","\nOpcion3 = JPY a CLP");
opcion=int(input());

if opcion==1:
    aud=float(input("Ingrese la cantidad de AUD: "))
    con=aud*531.61
    print(f"La cantidad ingresada equivale a {con}")

elif opcion==2:
    arg=float(input("Ingrese la cantida de ARG: "))
    con=arg*3.64
    print(f"La cantidad ingresada equivale a {con}")

elif opcion==3:
    jpy=float(input("Ingrese la cantida de JPY: "))
    con=jpy*5.93
    print(f"La cantidad ingresada equivale a {con}")