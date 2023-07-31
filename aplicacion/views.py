from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.

def index(request):
    return render(request, "aplicacion/base.html")


def departamentos(request):
    ctx ={"Departamentos": Departamentos.objects.all()}
    return render(request, "aplicacion/departamentos.html",ctx)


def bodegas(request):
    ctx ={"Bodegas": Bodegas.objects.all()}
    return render(request, "aplicacion/bodegas.html",ctx)


def terrenos(request):
    ctx ={"Terrenos": Terrenos.objects.all()}
    return render(request, "aplicacion/terrenos.html", ctx)


def estacionamientos(request):
    ctx ={"Estacionamientos": Estacionamientos.objects.all()}
    return render(request, "aplicacion/estacionamientos.html", ctx)

#---------------------------------------------------------------------------
#formularios
def dept_form(request):
    if request.method =="POST":
        miForm = DeptoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion=miForm.cleaned_data
            depto = Departamentos(
                ubicacion=informacion['ubicacion'], 
                metros2=informacion['metros'], 
                valor=informacion['valor'],
                piezas=informacion['piezas']  
                )
            depto.save()
            return render (request,"aplicacion/base.html")
    else:
        miForm =DeptoForm()
    return render(request, "aplicacion/dept_form.html", {"Form": miForm})


def bodega_form(request):
    if request.method == "POST":
        miForm = BodegaForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            bodega = Bodegas(
                ubicacion=informacion['ubicacion'],
                metro=informacion['metro'],
                valor=informacion['valor'],
            )
            bodega.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = BodegaForm()
    return render(request, "aplicacion/bodega_form.html", {"Form": miForm})


def terrenos_form(request):
    if request.method == "POST":
        miForm = TerrenoForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            terreno = Terrenos(
                ubicacion=informacion['ubicacion'],
                metro=informacion['metro'],
                valor=informacion['valor'],
            )
            terreno.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = TerrenoForm()
    return render(request, "aplicacion/terrenos_form.html", {"Form": miForm})


def est_form(request):

    if request.method == "POST":
        miForm = EstForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            est = Estacionamientos(
                ubicacion=informacion['ubicacion'],
                valor=informacion['valor'],
            )
            est.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = EstForm()
    return render(request, "aplicacion/bodega_form.html", {"Form": miForm})

#------------------------------------------------
#buscador
def buscardpto(request):
    return render(request, "aplicacion/buscardpto.html")

def buscar2(request):
    print(request.GET)  # Para imprimir los datos de búsqueda en la consola del servidor
    if 'Ubicacion' in request.GET:
        ubicacion = request.GET['Ubicacion']
        departamentos = Departamentos.objects.filter(ubicacion__icontains=ubicacion)
        return render(request, "aplicacion/resultadosdpto.html", {"Ubicacion": ubicacion, "departamentos": departamentos})
    else:
        return HttpResponse('No se ingresaron datos')