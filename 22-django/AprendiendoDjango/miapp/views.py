from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def index(request):
    return HttpResponse("""
    <h1>Inicio</h1>
    """)

def hola_mundo(request):
    return HttpResponse("Hola mundo con Django")