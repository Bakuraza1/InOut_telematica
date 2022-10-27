from django.contrib import admin
from .models import NewUser
from InOut_app.models import Producto, Usuario

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)

# Register your models here.
admin.site.register(NewUser)