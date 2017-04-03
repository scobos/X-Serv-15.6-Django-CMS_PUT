from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def pagina(request, identificador):

    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "El nombre no está en la base de datos"
    return HttpResponse(respuesta)

def mostrar_Info(request):
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

@csrf_exempt
def pagina_nueva(request, rec, contenido):

    if request.method == "PUT" or request.method == "POST":
        nueva_pag = Pages(rec = nombre, page = request.body)
        nueva_pag.save()
    elif request.method == "GET":
        nueva_pag = Pages(rec = nombre, page = contenido)
        nueva_pag.save()
    return HttpResponse("Se ha añadido la pagina")
