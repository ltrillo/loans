
from calculadora.models import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from decimal import *
import json
import requests



def inicio (request):

	
	return render(request,'calculadora/inicio.html')
 	

def solicitud (request):

	headers = {'Content-Type': 'application/json'}
	url = 'https://precio.onixcoin.com/api/v1/price/VEN/'
	r = requests.get(url, headers=headers)
	resp = r.json()

	btc_onx_buy = resp['btc_onx_buy']
	onx_bs_buy = resp['onx_bs_buy']
	usd_onx_buy = resp['usd_onx_buy']
	btc_onx_sell = resp['btc_onx_sell']
	onx_bs_sell = resp['onx_bs_sell']
	usd_onx_sell = resp['usd_onx_sell']
	
	print(btc_onx_buy)
	print(onx_bs_buy)
	print(usd_onx_buy)
	print(btc_onx_sell)
	print(onx_bs_sell)
	print(usd_onx_sell)

	if request.method == 'GET':

		condiciones = Condiciones.objects.get(pk=1)
		plazos = Plazos.objects.filter(activo=True)
		interes_anual = float(condiciones.Intanual)
		porcentaje_flat = float(condiciones.ComisionFlat)
		porcentaje_prestamo = condiciones.PorcentajePrestamo
		porcentaje_penalidad_mora = float(condiciones.PenalidadMora)
		porcentaje_garantia = 100 - float(porcentaje_prestamo)

		conext = {
			'plazos': plazos,
			'porcentaje_prestamo': porcentaje_prestamo,
			'interes_anual': interes_anual,
			'porcentaje_garantia': porcentaje_garantia,
			'porcentaje_flat': porcentaje_flat,
			'porcentaje_penalidad_mora': porcentaje_penalidad_mora
		}
		return render(request,'calculadora/solicitud.html', conext)

	elif request.method == 'POST':
		# buscar precio onix
		
		condiciones = Condiciones.objects.get(pk=1)
		porcentaje_prestamo = condiciones.PorcentajePrestamo

		monto = float(porcentaje_prestamo/100 ) * float(request.POST['onixcalculo'])
		plazos = Plazos.objects.filter(activo=True)
		ncuotas = int(request.POST['ncuotas'])
		#Calculo de las cuotas en Onx (capital + ineteres) y monto en garantia
		capcuota = monto / ncuotas
		captotal = capcuota*ncuotas
		interes_anual = float(condiciones.Intanual) 
		intmes = (interes_anual /100)/ 12
		intcuota = monto * intmes
		inttotal = intcuota*ncuotas
		garantia = float(request.POST['onixcalculo']) - monto
		comision_flat =  ( float(condiciones.ComisionFlat)/100 ) * monto
		garantia_real = float(garantia - comision_flat)

	    #Calculo de los BsS. que recibira por su prestamo
		
		precio_onix_sat1 = btc_onx_buy
		precio_onix_ves1 = onx_bs_buy
		montoves1 = float(precio_onix_ves1) * monto
		cuota = float((captotal+inttotal)/ncuotas)

		saldo_wallet = float(request.POST['saldowallet'])


		from datetime import date, timedelta 
		hoy = date.today()
		fecha = hoy
		arreglo=[]
		for a in range(ncuotas):
			fecha = fecha + timedelta(days=30)
			cuotas=("cuota Nro. %2.0f -- %s" % (a+1, fecha.strftime("%d/%m/%y")))
			arreglo.append({'numero_cuota': a+1, 'fecha_cuota': fecha.strftime("%d/%m/%y")})
		
		porcentaje_garantia = 100 - float(porcentaje_prestamo)
		porcentaje_flat = float(condiciones.ComisionFlat)
		monto_evaluado = float(request.POST['onixcalculo'])
		cuota_interes_mensual = intcuota
		cuota_capital_mensual = float(captotal)/ncuotas
		porcentaje_penalidad_mora = float(condiciones.PenalidadMora)
		cuotas_impago = garantia_real / (( 1 + (porcentaje_penalidad_mora/100)) * cuota)
		'''
		monto = Decimal(monto)
		ncuotas = Decimal(ncuotas) 
		montoves1 = Decimal(montoves1)
		cuota = Decimal(cuota)
		garantia_real = Decimal(garantia_real)
		interes_anual = Decimal(interes_anual)
		porcentaje_flat = Decimal(porcentaje_flat)
		cuota_interes_mensual = Decimal(cuota_interes_mensual)
		cuota_capital_mensual = Decimal(cuota_capital_mensual)
		porcentaje_penalidad_mora = Decimal(porcentaje_penalidad_mora)
		cuotas_impago = Decimal(cuotas_impago)'''

		conext = {
			'monto': monto,
			'ncuotas': ncuotas,
			'inttotal': inttotal,
			'plazos': plazos,
			'montoves1': montoves1,
			'cuota': cuota,
			'comision_flat': comision_flat,
			'garantia_real': garantia_real,
			'garantia': garantia,
			'cuotas': arreglo,
			'porcentaje_prestamo': porcentaje_prestamo,
			'interes_anual': interes_anual,
			'porcentaje_garantia': porcentaje_garantia,
			'porcentaje_flat': porcentaje_flat,
			'monto_evaluado': monto_evaluado,
			'cuota_interes_mensual': cuota_interes_mensual,
			'cuota_capital_mensual': cuota_capital_mensual,
			'porcentaje_penalidad_mora': porcentaje_penalidad_mora,
			'precio_onix_ves1': precio_onix_ves1,
			'cuotas_impago': cuotas_impago,
			

		}
	
	return render(request,'calculadora/solicitud.html', conext)



def prestamo (request):

	from datetime import date, timedelta 
	hoy = date.today()
	fecha = hoy

	context={
    }
	if request.method=='POST':

		condiciones = Condiciones.objects.get(pk=1)
		plazos = Plazos.objects.filter(activo=True)
		interes_anual = float(condiciones.Intanual)
		porcentaje_flat = float(condiciones.ComisionFlat)
		porcentaje_prestamo = condiciones.PorcentajePrestamo
		porcentaje_penalidad_mora = float(condiciones.PenalidadMora)


		#usuario = Usuario.objects.get(pk=1)
		
		'''p = Prestamo(Transferido_BsS=montoves1, Monto_ONX=Decimal(monto), Cuotas_Mensuales=ncuotas, Garantia_ONX=Decimal(garantia_real), Capital_Mensual= Decimal(cuota_capital_mensual), Interes_Mensual= Decimal(cuota_interes_mensual), Penalidad_Mora=Decimal(porcentaje_penalidad_mora), Impagos_Posibles= cuotas_impago, Cuota_ONX=Decimal(cuota), Fecha_Prestamo=fecha)
		p.save()
		print(p)'''

		estado = False 

		Prestamo(

			Fecha_Prestamo = fecha,
			Transferido_BsS = str(request.POST['montoves1']).replace(',','.'),
			Monto_ONX = str(request.POST['monto']).replace(',','.'),
			Cuotas_Mensuales = str(request.POST['ncuotas']).replace(',','.'),
			Garantia_ONX = str(request.POST['garantia_real']).replace(',','.'),
			Cuota_ONX = str(request.POST['cuota']).replace(',','.'),
			Capital_Mensual = str(request.POST['cuota_capital_mensual']).replace(',','.'),
			Interes_Mensual = str(request.POST['cuota_interes_mensual']).replace(',','.'),
			Impagos_Posibles = request.POST['cuotas_impago'],
			Penalidad_Mora = porcentaje_penalidad_mora
		).save()

 	

		context={
		
			"estado":estado
			}

	return render(request,'calculadora/prestamo.html',context)
	
    
