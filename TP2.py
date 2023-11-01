#Carrito de Compras

#En el siguiente programa se busca proporcionar al usuario la opción de calcular el costo total de un producto, incluyendo impuestos y posibilidad de pago en cuotas. Se le solicitará el nombre y el valor del producto, así como si desea pagar en cuotas. En caso afirmativo, se le pedirá la cantidad de cuotas. El programa luego calculará el costo total en base a la opción elegida.
#Variables de entrada: Nombre y valor del producto, cantidad de cuotas a pagar.
#Datos de salida: Confirmación e información de la compra, cantidad y valor de cuotas, valor total

def main():
    global precios_finales_cuotas, precios_finales, cantidad_cuotas_seleccionadas
    porcentaje_iva = 1.21

    lista_mouse = ["Logitech G pro", "Logitech G203", "Razer Deathadder V2", "Razer Naga", "Redragon M711", "Redragon M808"]
    lista_mouse_precios = [70, 50, 80, 85, 40, 45]
    lista_teclado = ["Logitech K400", "Logitech K480", "Razer Blackwidow", "Razer Hunstman", "Redragon Kumara k552", "Redragon Visnu"]
    lista_teclado_precios = [40, 50, 120, 185, 90, 75]
    lista_auricular = ["Logitech G335", "Logitech G435", "Razer Blackshark", "Razer kraken", "Redragon H120", "Redragon H220"]
    lista_auricular_precios = [140, 150, 100, 95, 75, 60]

    productos_carrito = []
    precio_carrito = []
    precios_finales = 0
    precios_finales_cuotas = 0
    cantidad_cuotas_seleccionadas = 0

    def obtenerDatosProducto():  # No recibe parámetro y no retorna valor
        cantidad_productos = int(input("Cuantos productos desea comprar? : ", ))
        x = 0
        for i in range(cantidad_productos):
            eleccion_productos = int(input("Ingrese el tipo de producto que desea comprar: 1. Mouse, 2. Teclado, 3. Auricular : "))
            lista_productos = []
            lista_precio = []
            if eleccion_productos == 1: 
                lista_productos = lista_mouse
                lista_precio = lista_mouse_precios
            elif eleccion_productos == 2:
                lista_productos = lista_teclado
                lista_precio = lista_teclado_precios
            elif eleccion_productos == 3:
                lista_productos = lista_auricular
                lista_precio = lista_auricular_precios
            
            for producto in lista_productos:
                print(str(x) + " " + producto)
                x + 1
                int(x)
                
            num_producto = int(input("Escriba el numero del producto que desea comprar : ", ))
            productos_carrito.append(lista_productos[num_producto])
            precio_carrito.append(lista_precio[num_producto])
            print(productos_carrito)
            print(precio_carrito)

    def EleccionCuotas(productos): # Recibe parametro y no retorna valor
        global cantidad_cuotas_seleccionadas
        print("Usted tiene en el carrito los siguientes productos : ")
        for producto in productos:
            print(producto)
        precioTotal = 0
        for carrito in precio_carrito:
            precioTotal += carrito
        print("A un total de " + str(precioTotal)+"$USD")

        pagar_en_cuotas = input("Desea pagar en cuotas? (si o no) : ",)
        if (pagar_en_cuotas == "si" or pagar_en_cuotas == "SI"or pagar_en_cuotas == "Si"):
            
            cuantas_cuotas = int( input("desea pagar en 3, 6 , 12 cuotas?(Ingresar numero de cuotas) : ", ))
            cantidad_cuotas_seleccionadas = cuantas_cuotas
            if cuantas_cuotas == 3:
                calculoEnCuotas(1.2994, 3, precioTotal)
            elif cuantas_cuotas == 6:
                calculoEnCuotas(1.5412, 6, precioTotal)
            elif cuantas_cuotas == 12:
                calculoEnCuotas(2.04101, 12, precioTotal)
        else:
            unPago(precioTotal)

    
    def calculoEnCuotas(intres,cuotas,precioCarrito):
        global precios_finales_cuotas, precios_finales
        precio_final = round(precioCarrito * intres)
        precio_final_en_cuotas = round(precio_final / cuotas)

        print("El precio final es de " + str(precio_final)+"$ USD")
        print("En " +str(cuotas) + " cuotas de " +str(precio_final_en_cuotas)+"$ USD")
        precios_finales += precio_final
        precios_finales_cuotas += precio_final_en_cuotas
        
    def unPago(precioTotal): # Recibe parámetro y retorna valor
        global precios_finales
        print("El precio Final es de " + str(precioTotal*porcentaje_iva) + " USD$ (iva incluido)")
        print(precios_finales)
        precios_finales = precioTotal*porcentaje_iva
   
    def tipoDePago():
        global precios_finales_cuotas, precios_finales, cantidad_cuotas_seleccionadas
        tipo_de_pago = int(input("Ingrese 1 para pagar con debito/contado (5% descuento) o ingrese 2 para pagar con tarjeta (15% de recargo) : ", ))
        if cantidad_cuotas_seleccionadas > 0:
            if tipo_de_pago == 1:
                precios_finales = round(precios_finales - (precios_finales * 0.05))
                precios_finales_cuotas = round(precios_finales / cantidad_cuotas_seleccionadas)
                print("Su nuevo precio es de " + str(precios_finales)+"$USD por pagar con debito/contado")
                print("En "+ str(cantidad_cuotas_seleccionadas) +" de " + str(precios_finales_cuotas))
            else:
                precios_finales = round(precios_finales * 1.15)
                precios_finales_cuotas = round(precios_finales / cantidad_cuotas_seleccionadas)
                print("Su nuevo precio es de " + str(precios_finales)+"$USD por pagar con tarjeta")
                print("En "+ str(cantidad_cuotas_seleccionadas) +" de " + str(precios_finales_cuotas))
        else:
            if tipo_de_pago == 1:
                precios_finales = round(precios_finales - (precios_finales * 0.05))
                print("Su nuevo precio es de " + str(precios_finales)+"$USD por pagar con debito/contado")
            elif tipo_de_pago == 2:
                precios_finales = round(precios_finales * 1.15)
                print("Su nuevo precio es de " + str(precios_finales)+"$USD por pagar con tarjeta")

    obtenerDatosProducto()
    EleccionCuotas(productos_carrito) 
    tipoDePago()

main()