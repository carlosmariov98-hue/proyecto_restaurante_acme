from funcionesAcme import productos, crearMesas, crearCliente, facturacion, generarReporte

while True:
    print("------------OPCIONES------------")
    print("1.para resgistar productos o ver")
    print("2. para crear mesas")
    print("3. para crear clientes")
    print("4. para facturacion")
    print("5.para generar reporte de ventas")
    print("0. para salir del menu")

        
    opcion =int(input("Elige una opción (1-5): "))
        
    if opcion == 1:
        productos()
        
    elif opcion == 2:
        crearMesas()
        
    elif opcion == 3:
        crearCliente()
        
    elif opcion == 4:
        facturacion()
        
    elif opcion == 5:
        generarReporte()
        
    elif opcion == 0:
        print("saliendo de restaurante acme.....")
        break
    
    else:
        print("debes elejir una opcion valida")