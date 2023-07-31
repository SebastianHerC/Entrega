from django import forms 

#Formularios
class DeptoForm(forms.Form):
    ubicacion = forms.CharField(label='Comuna del departamento', max_length=50, required=True)
    metros = forms.IntegerField(label='Cantidad de m2', required=True)
    valor = forms.IntegerField(label='Valor del departamento', required=True)
    piezas = forms.IntegerField(label='Cantidad de piezas', required=True)

class BodegaForm(forms.Form):
    ubicacion = forms.CharField(label='Comuna de la Bodega', max_length=50, required=True)
    valor = forms.IntegerField(label='Valor de la Bodega', required=True)
    metro = forms.IntegerField(label='Cantidad de m3', required=True)


class EstForm(forms.Form):
    ubicacion = forms.CharField(label='Comuna del Estacionamiento', max_length=50, required=True)
    valor = forms.IntegerField(label='Valor del Estacionamiento', required=True)   

class TerrenoForm(forms.Form):
    ubicacion = forms.CharField(label='Comuna del Terreno', max_length=50, required=True)
    metro = forms.IntegerField(label='Cantidad de m2', required=True)
    valor = forms.IntegerField(label='Valor del Terreno', required=True)