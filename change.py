def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingresar gasto:"))
    ingreso = float(input("Dinero recibido"))
    vueltoentero = int(ingreso - gasto)
    vueltodecimal = int(round((ingreso - gasto - vueltoentero) * 100))
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vueltoentero)
    print("Centavos:")
    print(vueltodecimal)
