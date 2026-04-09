import csv

def encabezado():
    
    columnas = ["codigo", "nombre", "valorUnitario", "iva"]
    existe = False
    
    try:
        with open("productos.csv", "r", newline="") as file:
            if file.read(1): 
                existe= True
    except FileNotFoundError:
        
        existe= False

    if not existe:
        with open("productos.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columnas)
            writer.writeheader()