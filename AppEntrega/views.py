from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import FormularioAuto, FormularioCiudad, FormularioPropietario

from .models import Auto, Propietario, Ciudad

# Create your views here.


def inicio(request):
    return render(request, "AppEntrega/index.html", {})


def crear_auto(request):
    auto = None
    if request.method == "POST":
        formulario_auto = FormularioAuto(request.POST)

        if formulario_auto.is_valid():
            datos_auto = formulario_auto.cleaned_data
            auto = Auto(
                marca=datos_auto["marca"],
                modelo=datos_auto["modelo"],
                patente=datos_auto["patente"],
            )
            auto.save()

    formulario_auto = FormularioAuto()

    return render(
        request,
        "AppEntrega/crear_auto.html",
        {"auto": auto, "formulario": formulario_auto},
    )


def crear_propietario(request):
    propietario = None
    if request.method == "POST":
        formulario_propietario = FormularioPropietario(request.POST)

        if formulario_propietario.is_valid():
            datos_propietario = formulario_propietario.cleaned_data
            propietario = Propietario(
                nombre=datos_propietario["nombre"],
                apellido=datos_propietario["apellido"],
                dni=datos_propietario["dni"],
            )
            propietario.save()

    formulario_propietario = FormularioPropietario()

    return render(
        request,
        "AppEntrega/crear_propietario.html",
        {"propietario": propietario, "formulario": formulario_propietario},
    )


def crear_ciudad(request):
    ciudad = None
    if request.method == "POST":
        formulario_ciudad = FormularioAuto(request.POST)

        if formulario_ciudad.is_valid():
            datos_ciudad = formulario_ciudad.cleaned_data
            ciudad = Auto(
                origen=datos_ciudad["origen"],
                destino=datos_ciudad["destino"],
            )
            ciudad.save()

    formulario_ciudad = FormularioCiudad()

    return render(
        request,
        "AppEntrega/crear_ciudad.html",
        {"ciudad": ciudad, "formulario": formulario_ciudad},
    )


def ver_auto(request):
    if request.method == "GET":
        patente = request.GET.get("patente", "")
        autos = Auto.objects.filter(patente=patente)
    else:
        autos = Auto.objects.all()

    return render(request, "AppEntrega/ver_auto.html", {"autos": autos})


def ver_propietario(request):
    if request.method == "GET":
        dni = request.GET.get("dni", "")
        propietarios = Propietario.objects.filter(dni=dni)
    else:
        propietarios = Propietario.objects.all()

    return render(
        request, "AppEntrega/ver_propietario.html", {"propietarios": propietarios}
    )


def ver_ciudad(request):
    if request.method == "GET":
        destino = request.GET.get("destino", "")
        ciudades = Ciudad.objects.filter(destino=destino)
    else:
        ciudades = Ciudad.objects.all()

    return render(request, "AppEntrega/ver_auto.html", {"ciudades": ciudades})
