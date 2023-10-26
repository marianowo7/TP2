#Carrito de Compras


#En el siguiente programa se busca proporcionar al usuario la opción de calcular el costo total de un producto, incluyendo impuestos y posibilidad de pago en cuotas. Se le solicitará el nombre y el valor del producto, así como si desea pagar en cuotas. En caso afirmativo, se le pedirá la cantidad de cuotas. El programa luego calculará el costo total en base a la opción elegida.
#Variables de entrada: Nombre y valor del producto, cantidad de cuotas a pagar.
#Datos de salida: Confirmación e información de la compra, cantidad y valor de cuotas, valor total

def main():
    porcentaje_iva = 1.21
    nombre = ""
    valor = 0
    vof = False

    lista_mouse = ["Logitech G pro", "Logitech G203", "Razer Deathadder V2", "Razer Naga", "Redragon M711", "Redragon M808"]
    lista_mouse_precios = [70, 50, 80, 85, 40, 45]
    lista_teclado = ["Logitech K400", "Logitech K480", "Razer Blackwidow", "Razer Hunstman", "Redragon Kumara k552", "Redragon Visnu"]
    lista_teclado_precios = [40, 50, 120, 185, 90, 75]
    lista_auricular = ["Logitech G335", "Logitech G435", "Razer Blackshark", "Razer kraken", "Redragon H120", "Redragon H220"]
    lista_auricular_precios = [140, 150, 100, 95, 75, 60]

    productos_carrito = []
    precio_carrito = []

    def obtenerDatosProducto():  # No recibe parámetro y no retorna valor
        cantidad_productos = int(input("Cuantos productos desea comprar? : ", ))

        for i in range(cantidad_productos):

            eleccion_productos = int(input("Ingrese el tipo de producto que desea comprar: 1. Mouse, 2. Teclado, 3. Auricular : "))
            if eleccion_productos == 1:
                i = 0
                int(i)
                for mouse in lista_mouse:
                    print( str(i) + ". " + mouse)
                    int(i)
                    i = i+1
                num_producto = int(input("Escriba el numero del producto que desea comprar : ", ))
                productos_carrito.append(lista_mouse[num_producto])
                precio_carrito.append(lista_mouse_precios[num_producto])
                print(productos_carrito)
                print(precio_carrito)
            elif eleccion_productos == 2:
                i = 0
                int(i)
                for teclado in lista_teclado:
                    print( str(i) + ". " + teclado)
                    int(i)
                    i = i+1
                num_producto = int(input("Escriba el número del producto que desea comprar : ", ))
                productos_carrito.append(lista_teclado[num_producto])
                precio_carrito.append(lista_teclado_precios[num_producto])
                print(productos_carrito)
                print(precio_carrito)
            elif eleccion_productos == 3:
                i = 0
                int(i)
                for auricular in lista_auricular:
                    print( str(i) + ". " + auricular)
                    int(i)
                    i = i+1
                num_producto = int(input("Escriba el numero del producto que desea comprar : ", ))
                productos_carrito.append(lista_auricular[num_producto])
                precio_carrito.append(lista_auricular_precios[num_producto])
                print(productos_carrito)
                print(precio_carrito)
                

            pagar_en_cuotas = input("Desea pagar en cuotas? (si o no) : ",)
            if (pagar_en_cuotas == "si" or pagar_en_cuotas == "SI"or pagar_en_cuotas == "Si"):
                pagoEnCuotas(productos_carrito, precio_carrito)
            # else:
            #     nombre = nombreProducto
            #     valor = valorProducto
            #     vof = False
            
    def pagoEnCuotas(productos, valor_productos): # Recibe parametro y no retorna valor
        cuantas_cuotas = int( input("desea pagar en 3, 6 , 12 cuotas?(Ingresar numero de cuotas) : ", ))

        # if cuantas_cuotas == 3:
        #     valor_total_en_tres_cuotas = round(valor * 1.2994 * porcentaje_iva)
        #     valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 3)
        #     print("")
        #     print("Usted compró " + str(nombre))
        #     print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
        #     print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
        # elif cuantas_cuotas == 6:
        #     valor_total_en_tres_cuotas = round(valor * 1.5412 * porcentaje_iva)
        #     valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 6)
        #     print("")
        #     print("Usted compró " + str(nombre))
        #     print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
        #     print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
        # elif cuantas_cuotas == 12:
        #     valor_total_en_tres_cuotas = round(valor * 2.04101 * porcentaje_iva)
        #     valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 12)
        #     print("")
        #     print("Usted compró " + str(nombre))
        #     print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
        #     print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
   
    def unPago(nombre, valor, vof): # Recibe parámetro y retorna valor
        cuotas = vof
        if cuotas == False:
            precio_total = round(valor * porcentaje_iva)
            total =   "Usted compró "+ nombre + " con el valor total de " + str(precio_total) + " (Iva incuido)"
            return total
        else:
            total = "Se pagó en cuotas"
            return total
   
    obtenerDatosProducto()

    # pago = unPago(nombre, valor, vof)
    # print(pago)
    
main()