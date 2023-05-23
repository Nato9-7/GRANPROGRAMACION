import random

for i in range(4):
    querer=random.randint(1,3)

    if querer==1:
        print("Me quiere mucho")

    elif querer==2:
        print("Me quiere poquito")
    
    elif querer==3:
        print("Me quiere nada")


if querer==1:
    print("Felicidades, ¡¡¡ Te Quieren Mucho!!! \nMucho!!! \nMucho!!!")

elif querer==2:
    print("Te quieren poquitooo (al menos es algo)")
    
elif querer==3:
    print("No te quieren nada :(")

