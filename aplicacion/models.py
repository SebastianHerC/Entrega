from django.db import models

# Create your models here.

#Modelos Estacionamiento, departamentos, bodegas, terrenos
class Estacionamientos(models.Model):
    ubicacion = models.CharField(max_length=50)
    valor = models.IntegerField()

    #Visualicación en panel admin
    def __str__(self):
        return f"{self.ubicacion},{self.valor}"


class Departamentos(models.Model):
    ubicacion = models.CharField(max_length=50)
    metros2 = models.IntegerField()
    valor = models.IntegerField()
    piezas = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.ubicacion},{self.metros2}, {self.valor}, {self.piezas}"
    

class Bodegas(models.Model):
    ubicacion = models.CharField(max_length=50)
    metro = models.IntegerField()
    valor = models.IntegerField()

   
    def __str__(self):
        return f"{self.ubicacion},{self.metro}, {self.valor}"



class Terrenos(models.Model):
    ubicacion = models.CharField(max_length=50)
    metro = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.ubicacion},{self.metro}, {self.valor}"