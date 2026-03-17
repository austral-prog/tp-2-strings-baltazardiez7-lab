def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre = input("Ingrese el nombre: ")
    nombremin =nombre.lower()
    print (f"Contiene a: {"a" in nombremin}")
    print(f"Contiene e: {"e" in nombremin}")
    print(f"Contiene i: {"i" in nombremin}")
    print(f"Contiene o: {"o" in nombremin}")
    print(f"Contiene u: {"u" in nombremin}")
    
