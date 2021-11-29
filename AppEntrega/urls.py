from django.urls import path
from AppEntrega.views import (
    crear_auto,
    crear_propietario,
    crear_ciudad,
    ver_auto,
    ver_propietario,
    ver_ciudad,
    inicio,
)

urlpatterns = [
    path("", inicio),
    path("crear_auto/", crear_auto, name="crear_auto"),
    path("crear_propietario/", crear_propietario, name="crear_propietario"),
    path("crear_ciudad/", crear_ciudad, name="crear_ciudad"),
    path("ver_auto/", ver_auto, name="ver_auto"),
    path("ver_propietario/", ver_propietario, name="ver_propietario"),
    path("ver_ciudad/", ver_ciudad, name="ver_ciudad"),
]
