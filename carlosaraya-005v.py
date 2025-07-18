productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock ={
'8475HD': [8500000,10],
'2175HD': [7500000,15],
'JjfFHD': [1200000, 8],
'fgdxFHD': [600000, 20],
'GF75HD': [950000, 12],
'123FHD': [70000, 18],
'342FHD': [1000000, 7],
'UWU131HD': [650000, 25]
}

def menu_principal():
    print("\n***MENU PRINCIPAL***")
    print("1. Stock marca")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir")

def stock_por_marca():
    marca = input("ingrese marca a consultar: ").strip().capitalize()
    found = False
    print(f"\n ---modelos de la marca {marca}---")
    for modelo, datos_producto in productos.items():
        if datos_producto[0].capitalize() == marca:
            if modelo in stock:
                print(f"modelo: {modelo}, Precio: {stock[modelo][0]}, Stock: {stock[modelo][1]}")
            found=True
        if not found:
             print(f"No se encontraron notebooks de la marca {marca}.")   
def busqueda_por_precio():
    while True:
        try:
            precio_min = int(input("ingrese precio minimo: "))  
            precio_max = int(input("ingrese precio maximo: "))  
            if precio_min > precio_max:
                print("El precio minimo no puede ser mayor al precio maximo. Intente nuevamente. ")
                continue
            break
        except ValueError :
            print("Dedebe ingresar valores enteros !! ")

        found = False
        print(f"\n --- Notbooks entre ${precio_min} y ${precio_max}---")
        for modelo, datos_stock in stock.items():
            precio = datos_stock[0]
            if precio_min <= precio_max:
                marca = productos[modelo][0]
                print(f"Modelo: {modelo} {marca}, Precio: {precio}, Stock: {datos_stock}")
                found = True
            if not found:
                print("No hay notebooks en ese rango de precios. ")

    def actualizar_precio():
            while True:
                modelo_a_actualizar = input("Ingrese el modelo por actualizar: ").strip().upper()
                if modelo_a_actualizar in stock:
                    while True:
                        try:
                            nuevo_precio = int(input(f"Ingrese precio nuevo: "))
                            stock[modelo_a_actualizar][0] = nuevo_precio
                            print("Precio actualizado !!")
                            break
                        except ValueError:
                            print("Debe ingresar valores enteros!! ")
                            break
                        else:
                            print("El modelo no existe!!")
                        desea_continuar = input("Desea actualizar el precio (s/n)?: ").strip().lower()
                        if desea_continuar != 's':
                            break
    def main():
            while True:
                menu_principal()
                opcion = input("Ingrese opcion: ")
                if opcion == '1':
                    stock_por_marca()    
                elif opcion == '2':
                    busqueda_por_precio()
                elif opcion == '3':
                    actualizar_precio() 
                elif opcion == '4':
                    print("Programa finalizado. ")
                    break
                else:
                    print("Debe seleccionar una opcion valida. ")
                if __name__ == "__main__":
                    main()





                

   