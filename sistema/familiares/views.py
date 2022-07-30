from django.shortcuts import render
from familiares.models import Familia
def mostrar_familia(request):
    familiar = Familia.objects.all()
    return render(request, "list_familiares.html",context={'lista':familiar})

