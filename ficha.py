def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombremal =input ("Introduce tu nombre: ")
    nombre= nombremal.strip()
    nombrelower= nombre.lower()
    email= input ("Introduce tu email: ")
    nota1 = int(input ("Introduce una nota: "))
    nota2 = int(input ("Introduce otra nota: "))
    nota3 = int(input("Introduce otra nota: "))
    print("""========================
    FICHA DEL ALUMNO
========================""")
    print (f"Nombre: {nombre.title()}")
    print (f"Email: {email.lower()}")
    print (f"Caracteres en nombre: {len(nombre)}")
    espacio= int(nombre.find(" "))
    inicial= nombre[0:1]+nombre[espacio+1:espacio+2]
    print (f"Iniciales: {inicial.upper()}")
    name=nombre[0:espacio]
    surname=nombre[espacio+1:]
    print (f"Usuario: {surname.lower()}.{name.lower()}")
    print (f"Email valido: {'@'in email}")
    arroba= int(email.find("@"))
    print (f"Dominio: {email.lower()[arroba+1:]}")
    print (f"Nombre para archivo: {name.title()}_{surname.title()}")
    print (f"Cantidad de a: {nombrelower.count('a')}")
    codigo=nombre[::-1]
    print (f"Codigo secreto: {codigo.upper()}")
    print (f"Nota 1: {nota1}")
    print (f"Nota 2: {nota2}")
    print (f"Nota 3: {nota3}")
    print (f"Suma: {int(nota1+nota2+nota3)}")
    print (f"Promedio: {(nota1+nota2+nota3)/3}")
    print (f"Promedio entero: {int((nota1+nota2+nota3)/3)}")
    print ("========================")
    
    
