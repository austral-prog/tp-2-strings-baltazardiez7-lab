def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingrese el Gasto: "))
    ingreso = float(input ("Ingrese el ingreso: "))
    vueltoentero =int(ingreso - gasto)
    vueltodecimal = int((ingreso - gasto- vueltoentero)*100)
    print (f"Ingresar gasto:\n{gasto}")
    print(f"Dinero Recibido\n{int(ingreso)}")
    print (f"\nVuelto\n")
    print (f"Pesos:\n{vueltoentero}")
    print (f"Centavos:\n{vueltodecimal}")
