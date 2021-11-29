from django import forms


class FormularioAuto(forms.Form):
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Patente = forms.IntegerField()


class FormularioPropietario(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    DNI = forms.IntegerField()


class FormularioCiudad(forms.Form):
    Origen = forms.CharField()
    Destino = forms.CharField()
