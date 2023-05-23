a = 4
b = "a"
try:
    c = a/b
    print(f"El resultado es: {c}")

except ZeroDivisionError:
    print("No se ha podido realizar la división")

except TypeError:
    print("Imposible dividir un int con un str")
 