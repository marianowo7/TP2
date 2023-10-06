def main():
    porcentaje_iva = 1.21
    global dato1  
    global dato2
    global dato3
    dato1 = ""
    dato2 = 0
    dato3 = False

    def ingresarNombre(): 
      nombreProducto = str(input( "Ingrese el nombre del producto : ",)) #No recibe parámetro y retorna valor
      return nombreProducto
      

    def ingresarValor(): 
      valorProducto = int(input("Ingrese el valor del producto (sin comas) : ")) #No recibe parámetro y retorna valor
      return valorProducto
    
    def ingresarProducto():  ## No recibe parámetro y no retorna valor
        global dato1  
        global dato2
        global dato3
        nombreProducto = ingresarNombre()

        valorProducto = ingresarValor()

        if valorProducto < 0:
            response_menos_que_cero = str(
                input("El valor ingresado no puede ser cero o menor que cero, presione 1 para reiniciar el programa : " )
            )
            if response_menos_que_cero == "1":
                main()

        pagar_en_cuotas = input("Desea pagar en cuotas? (si o no) : ",)
        if (pagar_en_cuotas == "si" or pagar_en_cuotas == "SI"or pagar_en_cuotas == "Si"):
            pagoEnCuotas(nombreProducto, valorProducto)
            dato1 = nombreProducto
            dato2 = valorProducto
            dato3 = False
        else:
            dato1 = nombreProducto
            dato2 = valorProducto
            dato3 = True
            

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

    ## Recibe parámetro y retorna valor
    def unPago(nombre, valor, c):
        cuotas = c
        if cuotas == True:
            precio_total = round(valor * porcentaje_iva)
            total =   "Usted compró "+ nombre + " con el valor total de " + str(precio_total) + " (Iva incuido)"
            return total
        else:
            total = "Se pagó en cuotas"
            return total
   
    ingresarProducto()
    pago = unPago(dato1, dato2, dato3)
    print(pago)
main()