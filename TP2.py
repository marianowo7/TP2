#Carrito de Compras


#En el siguiente programa se busca proporcionar al usuario la opción de calcular el costo total de un producto, incluyendo impuestos y posibilidad de pago en cuotas. Se le solicitará el nombre y el valor del producto, así como si desea pagar en cuotas. En caso afirmativo, se le pedirá la cantidad de cuotas. El programa luego calculará el costo total en base a la opción elegida.
#Variables de entrada: Nombre y valor del producto, cantidad de cuotas a pagar.
#Datos de salida: Confirmación e información de la compra, cantidad y valor de cuotas, valor total

def main():
    porcentaje_iva = 1.21
    global nombre  
    global valor
    global vof
    nombre = ""
    valor = 0
    vof = False

    def ingresarNombre(): 
      nombreProducto = str(input( "Ingrese el nombre del producto : ",)) #No recibe parámetro y retorna valor
      return nombreProducto
      
    def ingresarValor(): 
      valorProducto = int(input("Ingrese el valor del producto (sin comas) : ")) #No recibe parámetro y retorna valor
      return valorProducto
    
    def obtenerDatosProducto():  ## No recibe parámetro y no retorna valor
        global nombre  
        global valor
        global vof

        nombreProducto = ingresarNombre()

        valorProducto = ingresarValor()

        if valorProducto < 0 or nombreProducto == "":
            response_menos_que_cero = str(
                input("El valor ingresado no puede ser cero o menor que cero / el nombre del producto no puede estar vacio, presione 1 para reiniciar el programa : " )
            )
            if response_menos_que_cero == "1":
                main()

        pagar_en_cuotas = input("Desea pagar en cuotas? (si o no) : ",)
        if (pagar_en_cuotas == "si" or pagar_en_cuotas == "SI"or pagar_en_cuotas == "Si"):
            pagoEnCuotas(nombreProducto, valorProducto)
            nombre = nombreProducto
            valor = valorProducto
            vof = True
        else:
            nombre = nombreProducto
            valor = valorProducto
            vof = False
            
    def pagoEnCuotas(nombre, valor): ## Recibe parametro y no retorna valor
        cuantas_cuotas = int( input("desea pagar en 3, 6 , 12 cuotas?(Ingresar numero de cuotas) : ", ))

        if cuantas_cuotas == 3:
            valor_total_en_tres_cuotas = round(
                valor * 1.2994 * porcentaje_iva
            )
            valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 3)
            print("")
            print("Usted compró " + str(nombre))
            print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
            print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
        elif cuantas_cuotas == 6:
            valor_total_en_tres_cuotas = round(
                valor * 1.5412 * porcentaje_iva
            )
            valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 6)
            print("")
            print("Usted compró " + str(nombre))
            print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
            print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
        elif cuantas_cuotas == 12:
            valor_total_en_tres_cuotas = round(
                valor * 2.04101 * porcentaje_iva
            )
            valor_en_tres_cuotas = round(valor_total_en_tres_cuotas / 12)
            print("")
            print("Usted compró " + str(nombre))
            print("En tres cuotas de " + str(valor_en_tres_cuotas) + "$")
            print("(Total de " + str(valor_total_en_tres_cuotas) + "$)")
   
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

    pago = unPago(nombre, valor, vof)
    print(pago)
    
main()