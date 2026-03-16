def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("Ingrese su nombre: ")
    apellido = input ("Ingrese su apellido: ")
    print (nombre.lower() +" "+ apellido.lower())
    print(nombre.title() + " " + apellido.title())
    print(nombre.upper() + " " + apellido.upper())
    print(f" \t{nombre.lower()} {apellido.lower()} ")
