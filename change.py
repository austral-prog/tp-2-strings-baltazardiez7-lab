def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print ("Ingresar gasto:")
    gasto = float(input("Ingresar gasto:\n"))
    print(gasto)
    print ("Dinero recibido")
    ingreso = float(input("Dinero recibido\n"))
    print (int(ingreso))
    vueltoentero = int(ingreso - gasto)
    vueltodecimal = round((ingreso - gasto - vueltoentero) * 100)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vueltoentero)
    print("Centavos:")
    print (vueltodecimal)
    
