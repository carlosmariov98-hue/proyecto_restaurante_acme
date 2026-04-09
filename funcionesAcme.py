import csv
from datetime import datetime
from utilidades import encabezado

def productos():
    while True:
        print("elije 'r' para registrar productos")
        print("elije 'v' para ver productos")
        print("'s' para salir")
        producto=input("cual es tu opcion(r,v,s): ")
        print("-----------------------------------------")
        
        if producto == "r":
            print("tu opcion ha sido resgistrar elije una opcion")
            print("1. platillos")
            print("2.bebidas")
            print("3.salir")
            registro=int(input("cual es tu opcion: "))
            print("--------------------------------------------------")
        
        
            match(registro):
        
                case 1:
                    encabezado()
                    print("\n--- Registro platillo ---")
                    codigo= int(input(" codigo del platillo: "))
                    nombre= input("nombre del platillo: ")
                    while True:
                        try:
                            valorUnitario= float(input("precio del platillo: "))
                            if valorUnitario <= 0:
                                print("Error: El monto debe ser mayor que 0")
                            else:
                                break
                        except ValueError:
                            print("Error: Por favor, ingresa un numero.")
                    iva=float(input("cual es el iva del producto(ej:0.19): "))
                            
                    campos = ["codigo", "nombre", "valorUnitario", "iva"]
                    with open("productos.csv", "a", newline="") as file:
                        writer=csv.DictWriter(file,fieldnames=campos)
                        writer.writerow({
                                "codigo": codigo, 
                                "nombre": nombre, 
                                "valorUnitario": valorUnitario,
                                "iva":iva
                            })
                        
                    print("¡platillo guardado con exito!")
        
                case 2:
                    encabezado()
                    print("\n--- Registro Bebidas ---")
                    codigo= int(input(" codigo de la bebida: "))
                    nombre= input("nombre de la bebida: ")
                    while True:
                        try:
                            valorUnitario= float(input("precio de la bebida: "))
                            if valorUnitario <= 0:
                                print("Error: El monto debe ser mayor que 0")
                            else:
                                break
                        except ValueError:
                            print("Error: Por favor, ingresa un numero.")
                    iva=float( input("cual es el iva del producto(ej:0.19): "))
                            
                    campos = ["codigo", "nombre", "valorUnitario","iva"]
                    with open("productos.csv", "a", newline="") as file:
                        writer=csv.DictWriter(file,fieldnames=campos)
                        writer.writerow({
                            "codigo": codigo,
                            "nombre": nombre,
                            "valorUnitario": valorUnitario,
                            "iva": iva
                        })
                        
                    print("¡Bebida guardado con exito!")
                    
                case 3:
                    print("saliendo de registro")
                    break
            
                
        elif producto == "v":
            print("1.para ver")
            print("2.salir")
            ver=int(input("elige una opcion: "))
            
            match(ver):
                case 1:
                    with open("productos.csv", "r") as file:
                        print(file.read())
                
                case 2:
                    print("Saliendo......")
                    break
                
        elif producto== "s":
            print("saliendo.....")
            break
        
        else:
            print("debes elegir una opcion correcta")
            
def crearMesas():   
    print("----------Datos de la mesa----------")
    codigo=int(input("codigo de la mesa: "))
    nombre=input("nombre de la mesa: ")
    puestos=int(input("de cuantos puestos es la mesa: "))
    
    campos=["codigo", "nombre", "puestos"]
    with open("mesas.csv", "a", newline="") as file:
        writer=csv.DictWriter(file, fieldnames=campos)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
                            "codigo": codigo,
                            "nombre": nombre,
                            "puestos": puestos
                        })
        print("mesa guardada con exito")
        
def crearCliente():
    print("----------crear cliente----------")
    identificacion=int(input("# de identificacion: "))
    nombre=input("nombre del cliente: ")
    telefono=int(input("numero de telefono: "))
    email=input("correo electronico: ")
    
    campos=["identificacion","nombre","telefono","email"]
    with open("clientes.csv", "a", newline="") as file:
        writer=csv.DictWriter(file,fieldnames=campos)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            "identificacion": identificacion,
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        })
    print("los datos del cliente fueron cargados con exito")
    
def facturacion():
    
    print("\n----- SISTEMA DE FACTURACIÓN -----")
    
    cod_mesa = input("Ingrese el código de la mesa a atender: ")
    mesa_encontrada = None
    with open("mesas.csv", "r") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["codigo"] == cod_mesa:
                mesa_encontrada = fila
                break
    
    if not mesa_encontrada:
        print("Error: La mesa no existe.")
        return


    id_cliente = input("Ingrese la identificación del cliente: ")
    cliente_encontrado = None
    with open("clientes.csv", "r") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["identificacion"] == id_cliente:
                cliente_encontrado = fila
                break
    
    if not cliente_encontrado:
        print("Error: El cliente no está registrado.")
        return


    productos_factura = []
    fecha_factura = datetime.now()
    
    while True:
        cod_prod = input("\nIngrese el código del producto a añadir: ")
        producto_encontrado = None
        
        with open("productos.csv", "r") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila["codigo"] == cod_prod:
                    producto_encontrado = fila
                    break
        
        if producto_encontrado:
            cantidad = int(input(f"Cantidad de '{producto_encontrado['nombre']}': "))
            
            
            v_unitario = float(producto_encontrado["valorUnitario"])
            iva_valor = float(producto_encontrado.get("iva", 0))
            
            
            subtotal = (v_unitario + iva_valor) * cantidad
            
        
            item = {
                "codigo": cod_prod,
                "nombre": producto_encontrado["nombre"],
                "cantidad": cantidad,
                "v_unitario": v_unitario,
                "iva": iva_valor,
                "subtotal": subtotal
            }
            productos_factura.append(item)
            print("Producto agregado correctamente.")
        else:
            print("Producto no encontrado.")
            
        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    
    total_factura = sum(item["subtotal"] for item in productos_factura)
    
    factura_visual = f"""
==========================================
            ACME RESTAURANT
==========================================
Fecha: {fecha_factura}
Mesa: {mesa_encontrada['nombre']} (Puestos: {mesa_encontrada['puestos']})
------------------------------------------
CLIENTE:
Nombre: {cliente_encontrado['nombre']}
ID: {cliente_encontrado['identificacion']}
Tel: {cliente_encontrado['telefono']}
Email: {cliente_encontrado['email']}
------------------------------------------
DETALLE:
Cod | Producto | Cant | V.Unit | IVA | Subtotal
"""
    for p in productos_factura:
        linea = f"{p['codigo']} | {p['nombre']} | {p['cantidad']} | {p['v_unitario']} | {p['iva']} | {p['subtotal']}\n"
        factura_visual += linea
        
    factura_visual += "------------------------------------------"
    factura_visual += f"\nTOTAL A PAGAR: ${total_factura}"
    factura_visual += "\n==========================================\n"

    print(factura_visual)

    
    guardar = input("¿Desea guardar esta factura? (s/n): ").lower()
    if guardar == 's':
        # esta factura es para el cliente
        with open("facturacion.txt", "w") as f:
            f.write(factura_visual)
        print(f"Factura guardada con exito")   
        
        # esta factura es para el sistema para poder generar el reporte
        campos = ["total", "valor_iva"]
        with open("reporte.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            if f.tell() == 0:
                writer.writeheader()
            
            iva_total_factura = sum(item["iva"] * item["cantidad"] for item in productos_factura)
            
            writer.writerow({
                "total": total_factura,
                "valor_iva": iva_total_factura
            })
        print("venta registrada en el sistema")
        
def generarReporte():
    total_ventas = 0  
    total_iva = 0 
    
    try:
        with open("reporte.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for fila in reader:
                
                total_ventas += float(fila["total"])
                total_iva += float(fila["valor_iva"])
                
        
        print("======= REPORTE DE VENTAS =======")
        print(f"IVA Recaudado:           ${total_iva}") 
        print(f"TOTAL EN CAJA:           ${total_ventas}")
        print("=================================")
        
    except FileNotFoundError:
        print("Aún no hay facturas registradas.")