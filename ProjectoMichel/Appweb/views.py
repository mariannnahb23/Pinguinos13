from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render (request, 'Appweb/index.html')

def apadrinamiento(request):
    return render (request, 'Appweb/apadrinamiento.html')

def galeria(request):
    return render (request,'Appweb/galeria.html' )