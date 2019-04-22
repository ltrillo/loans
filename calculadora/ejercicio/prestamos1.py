print("*************************************************************************************")
print("                  BIENVENIDO AL SIMULADOR DE PRESTAMOS EN ONIX")
print("       USTED RECIBIRA BsS EN SU CUENTA ASOCIADA COLOCANDO ONIX EN GARANTIA")
print("             UNA VEZ CANCELADO SU PRESTAMO, LE RETORNAREMOS SUS ONIX")
print("      LEA DETENIDAMENTE LAS CONDICIONES ESTABLECIDAS PARA OTORGAR PRESTAMOS")
print("*************************************************************************************")
print("")
import time
print (time.strftime("%d/%m/%y"))
print("")
def main():

    while True: 
        try:
            saldowallet=float(input("Cual es el SALDO de su ONX wallet:"))
            print("")
            break
        except ValueError:
            print("Valor no permitido. Intente nuevamente")
       
    while True: 
        try:
            print("Tomando en cuenta que le prestaremos el 70% de este monto, ingrese cantidad de ONIX")
            onixcalculo=int(input("base para calcular su préstamo:"))
            print("")
            break
        except ValueError:
            print("Valor no permitido. Intente nuevamente")
      
    while onixcalculo>saldowallet:
        
        while True: 
            try:
                onixcalculo=int(input("Introduzca una cantidad de ONX menor o iguala al saldo de su wallet:"))
                print("")
                break
            except ValueError:
                print("Valor no permitido. Intente nuevamente")
               
            while True: 
                try:
                    onixcalculo=int(input("Introduzca una cantidad de ONX menor o iguala al saldo de su wallet:"))
                    print("")
                    break
                except ValueError:
                    print("Valor no permitido. Intente nuevamente") 
                    
    
    if onixcalculo<=saldowallet:
                              
        #definicion de condiciones de prestamos y variables iniciales
        
        print("*************************************************************************************")
        print("ADMINISTRADOR")
        print("CONDICIONES DEL PRESTAMO")
        print("")
       
        while True:
            try:
                comisionflat=float(input("Cual es el % de COMISION FLAT a cobrar (sugerido = 3%) ?:"))
                break
            except:
                print("Debe ingresar una cantidad valida") 
                pass  
                
        while True:
            try:
                intanual=float(input("Cual es el % de INTERES ANUAL a cobrar (sugerido = 12%) ?:"))
                break
            except:
                print("Debe ingresar una cantidad valida") 
                pass
               
        while True:
            try:
                xcienprestamo=float(input("Cual es el % DEL MONTO EVALUADO A PRESTAR (sugerido = 70%) ?:"))
                break
            except:
                print("Debe ingresar una cantidad valida") 
                pass
                
        while True:
            try:
                pena=float(input("Cual es el % de PENALIDAD POR MORA a cobrar (sugerido = 3%) ?:"))
                break
            except:
                print("Debe ingresar una cantidad valida") 
                pass
                           
        alza=10
        
        """
        while True:
            try:
                print("Cuanto puede subir el ONX respecto a su valor inicial antes de liquidar el credito por") 
                alza = float(input("ALZA (Sugerido: 10 veces) ="))
                print("El valor para liquidar el prestamo por BAJA del ONX sera el 50% del valor establecido")
                print("para liquidar el credito por ALZA")
                break
            except:
                print("Debe ingresar una cantidad valida") 
                pass                                    

        print("*************************************************************************************")
        input("Presione una tecla para continuar")
        print("")
        """
        comisionflat=comisionflat/100
        intanual=intanual/100
        xcienprestamo=xcienprestamo/100
        pena=pena/100   

        onixsat1=0.00000036
        btcusd1=6800
        btcves1=700000
        onixves1=onixsat1*btcves1 #Valor del ONX en BsS
        onixdolar1=onixsat1*btcusd1 #valor del ONX en USD
        
        """
        comisionflat=0.03 #Comision Flat a aplicar al monto del prestamo otrogado en ONX
        intanual=0.12 #Tasa de interes anual aplicable al monto prestado en OXN
        xcienprestamo=0.7 #Porcentaje que se otorgara en prestamo (del monto ingresado para calcular el prestamo en ONX)
        pena=0.03 #Porcentaje unico a aplicar por mora en la cuota mensual
        """

        xciengarantia=1-xcienprestamo
        
        
        intmes=intanual/12 #Interes mensual
        monto=onixcalculo*xcienprestamo #Monto total a prestar en ONX
        montoves=monto*onixves1 #Monto a depositarle al usuario en BsS
        
        penaxcien=pena #Valor en % de la penalidad por mora. solo para efector de texto
        comision=monto*comisionflat #Monto de la comision Flat en ONX
        garantia=onixcalculo-monto #Monto restante en garantia (30% del monto ingresado para calcular el prestamo menos la comision flat
        ejecucionprestamo=0 #variable de ejecucion del prestamo por incumplimiento
        saldowalletempresa=0 #wallet de la empresa prestataria
       
        if onixcalculo>0 and onixcalculo<=saldowallet:
            
            ncuotas=int(input("Plazo en el cual desea pagar el préstamo (6,12,18 o 24 meses):"))
            print("")

            while ncuotas !=6 and ncuotas !=12 and ncuotas !=18 and ncuotas !=24 :
                ncuotas=int(input("Introduzca plazos iguales a 6,12,18 o 24 meses:"))
                print("")
                
            #Definicion de variables del presrtamo en ONX
                
            capcuota=monto/ncuotas #capital de cada cuota
            intcuota=monto*intmes #Interes de cada cuota
            inttotal=intcuota*ncuotas #Interes total del prestamo
            cuota=capcuota+intcuota #Suma de capital mas interes a pagar mensualmente
            captotal=capcuota*ncuotas #Suma de todo el capital a pagar. es igual al monto total a prestar
            garantia_real=garantia-comision
            cantnopagos=garantia_real//(cuota+cuota*pena) #cantidad de cuotas que cubriria el monto en garantia en caso de no poder descontar del saldo en wallet del usuario
            prestamototal=captotal+inttotal #cantidad de onix que debe pagar el usuario de capital mas los intereses en el plazo establecido inicialmente
            
            print("")
            print("Si Usted acepta las siguientes condiciones recibirá en su cuenta bancaria la cantidad de BsS. %.2f" %(montoves))
            print("")
            print("Condiciones:")
            print("")
            print("Valores iniciales del ONX y BTC:")
            print("")
            print("USD/BTC = %.2f" % (btcusd1))
            print("BsS/BTC = %.2f" % (btcves1))
            print("BTC/ONX = %.8f" % (onixsat1))
            print("BsS/ONX = %.2f" % (onixves1))
            print("USD/ONX = %.8f" % (onixdolar1))
            print("*************************************************************************************")
            print("ADMINISTRADOR: SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f )" % (saldowalletempresa ,saldowalletempresa*onixdolar1))
            print("")
            vesinicio=onixves1*monto
            dolarinicio=onixdolar1*monto
            print("")
            print("Se le otorgará el %.2f%% del monto evaluado (%.8f ONX / %.2f USD), quedando en garantía" % (xcienprestamo*100,monto, monto*onixdolar1))
            print("el restante %.2f%% (%.8f ONX / %.2f USD), de la cual se descontará %.2f%% de comision Flat" % (xciengarantia*100, garantia,(garantia*onixdolar1), comisionflat*100))  
            print("(%.8f ONX / %.2f USD), quedando en garantia la cantidad de (%.8f ONX / %.2f USD)" % (comision, comision*onixdolar1, garantia_real, (garantia_real*onixdolar1)))
            print("la cual se podrá utilizar para cubrir los IMPAGOS de las cuotas en caso de NO poseer saldo suficiente")
            print("en su wallet. Sin embargo solo podrá incumplir en %.0f oportunidades. Es estos casos se aplicará un %.2f%%" % (cantnopagos, penaxcien*100 ))
            print("de penalidad por mora sobre el monto no cancelado")
            print("")
            print("NOTA IMPORTANTE: La cantidad de posibles IMPAGOS será recalculada en cada incumplimiento")
            print("")
            print("Le serán depositados %.2f BsS. (USD= %.2f) en su cuenta bancaria asociada" % (vesinicio,dolarinicio))
            print("")
            print("El capital mensual a pagar es: %.8f ONX" % (capcuota))
            print("El interes mensual a pagar es: %.8f ONX" % (intcuota))
            print("                               --------------")
            print("       La cuota total mensual: %.8f ONX" % (cuota))
            print("")
            print("Usted debera cancelar %.8f ONX de capital mas intereeses de la siguiente manera:" % (prestamototal))
            print("")
            
            from datetime import date, timedelta 
            hoy = date.today()
            fecha = hoy
            for a in range(ncuotas):
                fecha = fecha + timedelta(days=30)
                cuotas=("cuota Nro. %2.0f, %s: %.8f ONX" % (a+1, fecha.strftime("%d/%m/%y"), cuota))
                print (cuotas)
            print("")
           

            acepta=input("Acepta las condiciones (S/N):")
            acepta=acepta.upper()
            print("")
            while acepta != "S" and acepta != "N":
                acepta=(input("Debe responder con **S** (SI) o **N** (NO). Acepta las condiciones (S/N):"))
                acepta=acepta.upper()
                print("")
                
                                       
      
            if acepta == "S":
                          
                print("/////////////////////////////////PRESTAMO APROBADO////////////////////////////////////")
                print("")
                print("Le seran depositados %0.2f BsS (USD= %.2f) en su cuenta bancaria" % (vesinicio, dolarinicio))
                print("")
                from datetime import date, timedelta 
                hoy = date.today()
                fecha = hoy
                fecha = fecha + timedelta(days=30)
                print("Próxima cuota %s por un monto de %.8f ONX" % (fecha.strftime("%d/%m/%y"), cuota))
                print("")
                 
                saldowallet=saldowallet-onixcalculo
                garantia=garantia-comision
                saldowalletempresa=monto+comision+garantia
                vessaldoempresa=-vesinicio
               
                print("///////////////////////////////////////RECUERDE///////////////////////////////////////")
                print("")
                print("Saldo prestamo (Capital + Intereses): %.2f ONX (USD = %.2f )" % (prestamototal ,prestamototal*onixdolar1))
                print("")
                print("El monto en garantia es: %.2f ONX (USD = %.2f )" % (garantia_real ,garantia_real*onixdolar1))
                print("")
                print("saldo wallet: %.2f ONX (USD = %.2f )" % (saldowallet ,saldowallet*onixdolar1))
                print("")
                print("Se le ejecutará el monto en garantía si falla en %.0f cuotas" % (cantnopagos))
                print("")
                print("Aplicaremos el %.0f%% de penalidad por mora sobre el monto no cancelado" % (penaxcien*100))
                print("")
                print("*************************************************************************************")
                print("ADMINISTRADOR")
                print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar1, saldowalletempresa*onixves1))
                print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa))
                print("")


                contador=0 #contador para definir la cantidad de cuotas en caso de recalculo e incrementar las fechas.
                montopagado=0 #acumula los pagos que se realicen
                penalidad=0
                interespagado=0
                cuentacuotas=0
                                                                 
                while prestamototal>0 and cantnopagos>=1:
                    print("")
                                                          
                    print("Introduzca valores Actuales del ONX y BTC:")
                    
                    while True:
                        try:
                            btcusd2 = float(input("USD/BTC (Valor Iniciar = %.2f) =" % (btcusd1)))
                            break
                        except:
                            print("Debe ingresar una cantidad valida") 
                            pass        
                    while True:
                        try:
                            btcves2 = float(input("BsS/BTC (Valor Iniciar = %.2f) =" % (btcves1)))
                            break
                        except:
                            print("Debe ingresar una cantidad valida") 
                            pass        
                    while True:
                        try:
                            onixsat2 = float(input("BTC/ONX (Valor Iniciar = %.8f) =" % (onixsat1)))
                            break
                        except:
                            print("Debe ingresar una cantidad valida") 
                            pass        
                
                    """
                    btcusd2=btcusd1
                    btcves2=btcves1
                    onixsat2=onixsat1
                    """
                    onixves2=onixsat2*btcves2 #Valor actual del ONX en BsS
                    onixdolar2=onixsat2*btcusd2 #valor actual del ONX en USD
                                      
                    onixves2=onixsat2*btcves2 #Valor actual del ONX en BsS
                    onixdolar2=onixsat2*btcusd2 #valor actual del ONX en USD
                   
                    onixdividir=0
                    dolardividir=0
                    
                                  
                    variaonixsat = ((onixsat2/onixsat1)-1)*100
                    variaonixusd = ((onixdolar2/onixdolar1)-1)*100
                    variaonixves = ((onixves2/onixves1)-1)*100

                                    
                    
                                                         
                    if variaonixusd>alza*100:

                        xciendivideempresa=50/100
                        
                        print("*****************************************************************************************")
                        print("MOTIVADO AL ALZA DEL ONX (>%.2f VECES), EL PRESTAMO HA CESADO DE MANERA GANAR - GANAR" % (alza))
                        print("*****************************************************************************************")
                        print("")
                        print("Variación del ONX = %.2f%% (USD/ONX)_%.2f%% (BsS/ONX)_%.2f%% BTC/ONX" % (variaonixusd, variaonixves, variaonixsat))
                        print(prestamototal)
                        print(garantia_real)
                        print(inttotal)
                        print(interespagado)
                        print(cuota)
                        onixdividir=prestamototal+garantia_real-(inttotal-interespagado)-cuota
                        dolardividir=onixdividir*onixdolar2
                        
                        montoonixempresa=onixdividir*xciendivideempresa
                        montoonixusuario=onixdividir-montoonixempresa

                        montousdempresa=dolardividir*xciendivideempresa
                        montousdusuario=dolardividir-montousdempresa

                        porcentusdusuario=(montousdusuario/dolarinicio)*100
                        saldowallet=saldowallet+montoonixusuario
                        print("Hemos transferido a su wallet la cantidad de %.8f ONX (USD= %0.2f)" % (montoonixusuario, montousdusuario))
                        print("")
                        print("Saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                        print("representando este monto un %0.2f%% del valor inicial otorgado" % (porcentusdusuario))
                        print("")
                        saldowalletempresa=saldowalletempresa-montoonixusuario
                        print("***********")
                        print("ADMINISTRADOR")
                        print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                        print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                        print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                        print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                        print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                        print("")

                        prestamototal=0
                        garantia_real=0
                        cantnopagos=0
                        ejecucionprestamo=1


                    if variaonixusd<-(alza/2)*100:

                        print("*****************************************************************************************")
                        print("MOTIVADO AL BAJA DEL ONX  EN %.2f EL PRESTAMO HA CESADO DE MANERA GANAR - GANAR" % (variaonixusd))
                        print("*****************************************************************************************")
                        print("")
                       
                        saldowallet=saldowallet
                        saldowalletempresa=saldowalletempresa
                        
                        prestamototal=0
                        garantia_real=0
                        cantnopagos=0
                        ejecucionprestamo=1
                        
                        print("Saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                        print("Saldo de su Préstamo = %.8f ONX" % (prestamototal))
                        print("Saldo de su Granatía = %.8f ONX" % (garantia))
                        print("")
                        print("***********")
                        print("ADMINISTRADOR")
                        print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                        print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                        print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                        print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                        print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                        print("")

                                                  

                    if saldowallet<cuota+cuota*pena and ejecucionprestamo<1 or garantia_real<(cuota+cuota*pena) and saldowallet<prestamototal and ejecucionprestamo<1  or (saldowallet+garantia_real)<cuota+cuota*pena and cantnopagos>=1 and saldowallet<prestamototal and ejecucionprestamo<1:
                     
                        print("*****************************************************************************************")
                        print("   No cuenta con saldo suficiente en su wallet para cancelar la cuota. Recuerde que su   ")
                        print(" prestamo puede ser ejecutado si falla en sus pagos. Para proceder al cobro de la cuota ")
                        print("             del saldo en su wallet, debe depositar: %0.8f ONX:" % (cuota-saldowallet))
                        print("*****************************************************************************************")

                        depositar=input("Desea hacer depósito a su wallet (S/N)?: ")
                        print("")
                        depositar=depositar.upper()
                                    
                        while depositar != "S" and depositar != "N":
                            depositar=(input("Debe responder con **S** (SI) o **N** (NO). Desea hacer depósito a su wallet(S/N)?:"))
                            depositar=depositar.upper()
                            print("")
                         
                        if depositar=="S":

                            while True:
                                try:
                                    deposito = float(input("Introduzca monto de ONX a depositar:"))
                                    break
                                except:
                                    print("Debe ingresar una cantidad valida") 
                                    pass        
                            
                            print("")
                            saldowallet=(saldowallet+deposito)
                            print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                            print("")

                                         
                        else:

                            if garantia_real>=(2*(cuota+cuota*pena)):

                                print("Procederemos a descontar de su garantia y de su wallet el monto de su cuota")
                                print("")
                                


                            else:
                         
                                print("***************************  Prestamo ejecutado  ************************************")
                                saldowalletempresa=saldowalletempresa+garantia_real+saldowallet
                                monto=garantia_real-cuota
                                ejecucionprestamo=1

                     
                    if garantia_real>(cuota+cuota*pena) and cantnopagos>=1 and prestamototal>0 and saldowallet>=0 and ejecucionprestamo<1:
                         
                        pagado=0
                        pagar = input("Pagar cuota (S/N)?: ")
                        pagar=pagar.upper()
                      
                        print("")
                                                            

                        if pagar== "S" and cantnopagos>=1 and garantia_real>(cuota+cuota*pena):
                                                    
                            
                            if saldowallet>=cuota: #CONDICION 1
                                
                                cuentacuotas=cuentacuotas+1
                                contador=contador+1 
                                pagado=cuota
                                prestamototal=prestamototal-pagado
                                montopagado=montopagado+pagado
                                interespagado=interespagado+intcuota
                                saldowallet=saldowallet-cuota
                                saldowalletempresa=saldowalletempresa+pagado
                                
                                fechapc = hoy + (contador*timedelta(days=30))
                                fechapc=(fechapc.strftime("%d/%m/%y"))
                                print("***********")
                                print("GRACIAS POR SU PAGO EN ONIX")
                                print("")
                                print("")
                                print("Usted cancelo su cuota Nro.%2.0f por %.8f ONX (USD= %.2f) " % (cuentacuotas ,pagado,pagado*onixdolar2))
                                print("")                                 
                                print("Total cancelado a la fecha= %.8f ONX (USD= %.2f) " % (montopagado ,montopagado*onixdolar2))
                                print("")
                                print("Proxima Cuota: %s. Monto= %.8f ONX" % (fechapc,cuota))
                                print("")
                                print("Se le ejecutará el monto en garantía si falla en %.0f cuotas" % (cantnopagos))
                                print("")
                                print("Saldo prestamo: %.8f ONX (USD= %.2f)" % (prestamototal,prestamototal*onixdolar2))
                                print("")
                                print("Monto en garantia: %.8f ONX (USD= %.2f)" % (garantia_real,garantia_real*onixdolar2))
                                print("")
                                print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                                print("")
                                print("***********")
                                print("ADMINISTRADOR")
                                print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                                print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                                print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                                print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                                print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                                print("")
               
                            else:  #CONDICION 2
                                 
                                if saldowallet>0 and saldowallet<2*(cuota+cuota*pena) and garantia>(cuota+cuota*pena) and cantnopagos>=1 : 
                                     
                                    cuentacuotas=cuentacuotas+1
                                    contador=contador+1 
                                    impago=cuota-saldowallet #como se cobran los intereses de la wallet lo no pagado es solo el capital de la cuota
                                    penalidad=impago*pena #penalidad de lo no pagado
                                    descuento1=saldowallet #descuento de los intereses de la cuota
                                    saldowallet=saldowallet-descuento1 #reflejo del descuento d elos intereses en la walet
                                    descuento2=impago #descuento capital no pagado de la cuota
                                    garantia_real=garantia_real-descuento2-penalidad #nuevo monto de la garantia al descontar el capital de la cuota y la penalidad
                                    cantnopagos=garantia_real//(cuota+cuota*pena)
                                    pagado=descuento1+descuento2+penalidad #Total pagado incluyendo penalidades
                                    pagado1=pagado-penalidad
                                    prestamototal=prestamototal-descuento1-descuento2 #Saldo del prestramo
                                    montopagado=montopagado+pagado
                                    montopagado1=montopagado-penalidad
                                    interespagado=interespagado+intcuota
                                    saldowalletempresa=saldowalletempresa+pagado
                                    fechapc = hoy + (contador*timedelta(days=30))
                                    fechapc=(fechapc.strftime("%d/%m/%y"))
                                    print("*********************")                              
                                    print("PAGO IRREGULAR TIPO I")
                                    print("*********************")
                                    print("")
                                    print("Descontamos de su wallet los intereses del mes y parte de su cuota Nro.%2.0f: %.8f ONX (USD= %.2f) y de su garantia" % (cuentacuotas,descuento1,descuento1*onixdolar2))
                                    print("el monto restante de la cuota: %.8f ONX (USD= %.2f) mas la penalidad por mora %.8f ONX (USD= %.2f)" % (descuento2,descuento2*onixdolar2,penalidad,penalidad*onixdolar2))
                                    print("")
                                    print("Total cancelado a la fecha= %.8f ONX (USD= %.2f) " % (montopagado ,montopagado*onixdolar2))
                                    print("")
                                    print("Proxima Cuota: %s Monto= %.8f ONX" % (fechapc,cuota))
                                    print("")
                                    print("Saldo prestamo: %.8f ONX (USD= %.2f)" % (prestamototal,prestamototal*onixdolar2))
                                    print("")
                                    print("Monto en garantia: %.8f ONX (USD= %.2f)" % (garantia_real,garantia_real*onixdolar2))
                                    print("")
                                    print("Se le ejecutará el monto en garantía si falla en %.0f cuotas" % (cantnopagos))
                                    print("")
                                    print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                                    print("")
                                    print("***********")
                                    print("ADMINISTRADOR")
                                    print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                                    print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                                    print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                                    print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                                    print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                                    print("")
                                    
                                     
                                    ncuotas=ncuotas-contador #cuotas restantes
                                    monto=monto-pagado1 #monto del prestamo objeto a recalculo
                                                    
                                else: #CONDICION 3
                                     
                                    if saldowallet==0 and garantia>2*(cuota+cuota*pena) and cantnopagos>1: 

                                        cuentacuotas=cuentacuotas+1                                  
                                        contador=contador+1 
                                        impago=cuota #Lo no pagado es toda la cuota
                                        penalidad=impago*pena #penalidad de lo no pagado
                                        descuento1=impago #descuento capital no pagado de la cuota
                                        garantia_real=garantia_real-descuento1-penalidad #nuevo monto de la garantia al descontar el capital de la cuota y la penalidad
                                        cantnopagos=garantia_real//(cuota+cuota*pena)
                                        pagado=descuento1+penalidad #Total pagado incluyendo penalidades
                                        pagado1=pagado-penalidad
                                        prestamototal=prestamototal-descuento1 #Saldo del prestramo
                                        montopagado=montopagado+pagado
                                        montopagado1=montopagado-penalidad
                                        interespagado=interespagado+intcuota
                                        saldowalletempresa=saldowalletempresa+pagado
                                        fechapc = hoy + (contador*timedelta(days=30))
                                        fechapc=(fechapc.strftime("%d/%m/%y"))
                                        print("**********************")
                                        print("PAGO IRREGULAR TIPO II")
                                        print("**********************")
                                        print("")
                                        print("El saldo en su wallet es insuficiente para descontar la cuota. Descontamos de su garantia") 
                                        print("el monto total de la cuota Nro.%2.0f: %.8f ONX (USD= %.2f) mas la penalidad por mora %.8f ONX (USD= %.2f)" % (cuentacuotas, descuento1,descuento1*onixdolar2,penalidad,penalidad*onixdolar2))
                                        print("")
                                        print("Total cancelado a la fecha= %.8f ONX (USD= %.2f) " % (montopagado ,montopagado*onixdolar2))
                                        print("")
                                        print("Proxima Cuota: %s. Monto= %.8f ONX" % (fechapc,cuota))
                                        print("")
                                        print("Saldo prestamo: %.8f ONX (USD= %.2f)" % (prestamototal,prestamototal*onixdolar2))
                                        print("")
                                        print("Monto en garantia: %.8f ONX (USD= %.2f)" % (garantia_real,garantia_real*onixdolar2))
                                        print("")
                                        print("Se le ejecutará el monto en garantía si falla en %.0f cuotas" % (cantnopagos))
                                        print("")
                                        print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                                        print("")
                                        print("***********")
                                        print("ADMINISTRADOR")
                                        print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                                        print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                                        print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                                        print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                                        print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                                        print("")
                                        ncuotas=ncuotas-contador #cuotas restantes
                                        monto=monto-pagado1 #monto del prestamo objeto a recalculo
                    
                                    else:
                                        saldowalletempresa=saldowalletempresa+garantia+saldowallet
                                        monto=garantia_real-cuota
                                        ejecucionprestamo=1
                                        saldowallet=0
                    else:
                        if ejecucionprestamo>0 and garantia_real != 0 or saldowallet<(cuota+cuota*pena) and garantia_real<(2*(cuota+cuota*pena)) and garantia_real != 0:
                            
                            saldowalletempresa= saldowalletempresa+saldowallet
                            saldowallet = 0
                            print("*************************************************************************************")
                            print("Por incumplimiento en sus pagos su prestamo ha sido cancelado y su garantia ejecutada")
                            print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet ,saldowallet*onixdolar2))
                            print("*************************************************************************************")
                            print("")
                            print("***********")
                            print("ADMINISTRADOR")
                            print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                            print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                            print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                            print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                            print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                            prestamototal=0  

                    if  ejecucionprestamo<1 and prestamototal<=0:
                        print("")
                        print("**************************************************************************************")
                        print("***                     USTED HA CANCELADO EXITOSAMENTE SU PRESTAMO                ***")
                        print("**************************************************************************************")
                        #print(saldowallet)
                        reintegro=0
                        deducciones=0
                        reintegro=montopagado+garantia_real
                        deducciones=interespagado+penalidad
                        devolver=reintegro-deducciones
                        saldowallet=saldowallet+devolver
                        #print(montopagado)
                        #print(garantia)
                        #print(interespagado)
                        #print(penalidad)  
                        saldowalletempresa=saldowalletempresa-devolver
                        print("")
                        print("Hemos transferido a su Wallet la cantidad de %.8f ONX (USD= %.2f)" % (devolver, devolver*onixdolar2))
                        print("")
                        print("saldo wallet: %.8f ONX (USD= %.2f)" % (saldowallet,saldowallet*onixdolar2))
                        print("")
                        print("***********")
                        print("LE INVITAMOS A SOLICITAR UN NUEVO PRESTAMO")
                        print("")
                        print("***********")
                        print("ADMINISTRADOR")
                        print("SALDO WALLET EMPRESA: %.2f ONX (USD = %.2f / BsS = %.2f)" % (saldowalletempresa ,saldowalletempresa*onixdolar2, saldowalletempresa*onixves2))
                        print("SALDO CUENTA BANCARIA EMPRESA: %.2f BsS" % (vessaldoempresa+saldowalletempresa*onixves2))
                        print("Variacion BTC/ONX = %.2f%%" % (variaonixsat))
                        print("Variacion USD/ONX = %.2f%%" % (variaonixusd))
                        print("Variacion BsS/ONX = %.2f%%" % (variaonixves))
                        print("")
            else:
                print("**************************************************************************************")
                print("***         LE INVITAMOS A OPTAR A UN PRESTAMO EN UNA NUEVA OPORTUNIDAD            ***")
                print("**************************************************************************************")
 
if __name__ == "__main__":
	main()
