from django.contrib import admin

from .models import Auto, Ciudad, Propietario

# Register your models here.

admin.site.register(Auto)
admin.site.register(Propietario)
admin.site.register(Ciudad)
