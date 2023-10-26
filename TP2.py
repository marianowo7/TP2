#Carrito de Compras


#En el siguiente programa se busca proporcionar al usuario la opción de calcular el costo total de un producto, incluyendo impuestos y posibilidad de pago en cuotas. Se le solicitará el nombre y el valor del producto, así como si desea pagar en cuotas. En caso afirmativo, se le pedirá la cantidad de cuotas. El programa luego calculará el costo total en base a la opción elegida.
#Variables de entrada: Nombre y valor del producto, cantidad de cuotas a pagar.
#Datos de salida: Confirmación e información de la compra, cantidad y valor de cuotas, valor total

def main():
    porcentaje_iva = 1.21

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

        cuantasCuotas(productos_carrito)
            
    def cuantasCuotas(productos): # Recibe parametro y no retorna valor

        print("Usted tiene en el carrito los siguientes productos : ")

        i = 1

        for producto in productos:
            print(str(i) + ". " + producto)
            i += 1

        precioTotal = 0
        for carrito in precio_carrito:
            precioTotal += carrito
        print("A un total de " + str(precioTotal)+"$USD")

        pagar_en_cuotas = input("Desea pagar en cuotas? (si o no) : ",)
        if (pagar_en_cuotas == "si" or pagar_en_cuotas == "SI"or pagar_en_cuotas == "Si"):
            
            cuantas_cuotas = int( input("desea pagar en 3, 6 , 12 cuotas?(Ingresar numero de cuotas) : ", ))
            
            if cuantas_cuotas == 3:
                calculoEnCuotas(1.2994, 3, precioTotal)
            elif cuantas_cuotas == 6:
                calculoEnCuotas(1.5412, 6, precioTotal)
            elif cuantas_cuotas == 12:
                calculoEnCuotas(2.04101, 12, precioTotal)
        else:
            unPago(precioTotal)

    
    def calculoEnCuotas(intres,cuotas,precioCarrito):
        precio_final = round(precioCarrito * intres)
        precio_final_en_cuotas = round(precio_final / cuotas)

        print("El precio final es de " + str(precio_final)+"$ USD")
        print("En " +str(cuotas) + " cuotas de " +str(precio_final_en_cuotas)+"$ USD")
        
    def unPago(precioTotal): # Recibe parámetro y retorna valor
        print("El precio Final es de " + str(precioTotal*porcentaje_iva) + " USD$ (iva incluido)")
   
    obtenerDatosProducto()
    
main()

#en el parte practica va todo lo q se vio en clase, mas algunas preguntas para resolver pequeños ejercicios en el parcial.
#dsp viene la parte oral en donde se hacen preguntas conceptuales. Inscribirse como libre cuando se abran las mesas de examen.