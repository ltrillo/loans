from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Usuario(models.Model):

    Apellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    DNI = models.CharField(max_length=8)
    email = models.EmailField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length = 1, choices = SEXOS, default = 'M')
    

    def NombreCompleto (self):
        cadena ="{0} {1} - {2}"
        return cadena.format(self.Apellido, self.Nombre, self.email)
        self.save()

    def __str__(self):
        return self.NombreCompleto()

class Condiciones(models.Model):
    
    ComisionFlat = models.DecimalField(max_digits=4, decimal_places=2)
    PorcentajePrestamo = models.DecimalField(max_digits=4, decimal_places=2)
    Intanual = models.DecimalField(max_digits=4, decimal_places=2)
    PenalidadMora = models.DecimalField(max_digits=4, decimal_places=2)
    
    
    def __str__(self):
        return "{0}% del Monto Evaluado  / {1}% Interes Anual / {2}% Comision Flat / {3}% Penalidad por Mora".format(self.PorcentajePrestamo, self.Intanual, self.ComisionFlat, self.PenalidadMora)

class Plazos(models.Model):
    ncuotas = models.IntegerField(null=False, verbose_name='Plazo')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ncuotas)

class PreciosIniciales(models.Model):
    onixsat1 = models.DecimalField(max_digits=17, decimal_places=8)
  
    btcves1 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):

        return "{0} BTC/ONX - {1} USD/BTC - {2} BsS/BTC".format(self.onixsat1, self.btcusd1, self.btcves1)   

class Prestamo(models.Model):

    #Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    Fecha_Prestamo = models.DateTimeField(default=timezone.now)
    Suma_Fecha_Cuota = 30

    Transferido_BsS = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Monto_ONX = models.DecimalField(max_digits=17, decimal_places=8, default=0)
    Cuotas_Mensuales = models.IntegerField()
    Garantia_ONX = models.DecimalField(max_digits=17, decimal_places=8, default=0)
     
    Cuota_ONX = models.DecimalField(max_digits=17, decimal_places=8, default=0)
    Capital_Mensual = models.DecimalField(max_digits=17, decimal_places=8, default=0)
    Interes_Mensual = models.DecimalField(max_digits=17, decimal_places=8, default=0)
    Penalidad_Mora = models.DecimalField(max_digits=4, decimal_places=2)
    Impagos_Posibles = models.DecimalField(max_digits=2, decimal_places=0, default=0)
   


    