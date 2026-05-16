user1 = None
user2 = None
user3 = None

pass1 = None
pass2 = None
pass3 = None

telefono = None

volver = True

sesion_iniciada = False

while volver:
    
    while True:
        option = int(input("1) Iniciar Sesión\n2) Registrar Usuario\n3) Salir\nElige una opción: "))
        try:
            if option == 1:
                if user1 or user2 or user3:
                    resp = input("Ingrese nombre de usuario: ")
                    if resp == user1:
                        resp2 = input("Ingrese la contraseña: ")
                        if resp2 == pass1:
                            print("Sesion Iniciada: ")
                            sesion_iniciada = True
                            break
                    if resp == user2:
                        resp2 = input("Ingrese la contraseña: ")
                        if resp2 == pass2:
                            print("Sesion Iniciada: ")
                            sesion_iniciada = True
                            break

                    if resp == user3:
                        resp2 = input("Ingrese la contraseña: ")
                        if resp2 == pass3:
                            print("Sesion Iniciada: ")
                            sesion_iniciada = True
                            break

                print("Debe registrar un usuario! ")
                continue
                    
            elif option == 2:
                print("Crear usuario: ")
                if user1 == None:
                    user1 = input("Cree su nombre de usuario: ")
                    pass1 = input("Cree su contraseña: ")
                    
                
                elif user2 == None:
                    user2 = input("Cree su nombre de usuario: ")
                    pass2 = input("Cree su contraseña: ")
                   
                
                elif user3 == None:
                    user3= input("Cree su nombre de usuario: ")
                    pass3 = input("Cree su contraseña: ")  
                 

                    

            elif option == 3:
                volver = False
                break
        except:
            print("Ha ingresado una opcion invalida!")

    while sesion_iniciada:
        
        try:
            print("1) Realizar llamada: ")
            print("2) Enviar correo: ")
            print("3) Cerrar Sesion")
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                print("LLamar")
                telefono = input("Ingrese numero de telefono: ")
                if telefono.startswith("9") and telefono.isdigit():
                    print(f"Llamando a {telefono}")

            elif option == 2:
                print("Enviar correo electronico: ")
                correo = input("Ingrese correo electronico:")
                print("enviando correo a",correo)
            elif option == 3:
                print("Cerrando sesion")
                sesion_iniciada = False
                break
        except:
            print("Ingrese una opcion valida")



        


