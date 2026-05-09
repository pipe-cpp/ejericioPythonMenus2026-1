while True:
    print("1. Pago con tarjeta de crédito")
    print("2. Simulación de compra")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Pagando...")
    elif opcion == "2":
        print("Comprando...")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
