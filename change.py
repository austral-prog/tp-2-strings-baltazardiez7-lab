def change():
    gasto = float(input("Ingresar gasto:"))
    ingreso = float(input("Dinero recibido"))

    vuelto = ingreso - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)}")
    
