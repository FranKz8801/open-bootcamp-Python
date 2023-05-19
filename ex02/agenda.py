agenda = {}

while True:
    print("¿Qué acción quieres realizar?")
    print("1. Añadir persona")
    print("2. Buscar teléfono de una persona")
    print("3. Salir")
    
    opcion = input("Introduce una opción (1-3): ")
    
    if opcion == "1":
        nombre = input("Introduce el nombre de la persona: ")
        telefono = input("Introduce el teléfono de la persona: ")
        agenda[nombre] = telefono
        print(f"Se ha añadido a {nombre} con el teléfono {telefono}")
    elif opcion == "2":
        nombre = input("Introduce el nombre de la persona: ")
        resultados = []
        for persona, telefono in agenda.items():
            if persona.startswith(nombre):
                resultados.append((persona, telefono))
        if len(resultados) > 0:
            print("Resultados:")
            for persona, telefono in resultados:
                print(f"{persona}: {telefono}")
        else:
            print("No se han encontrado resultados.")
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Introduce una opción del 1 al 3.")
