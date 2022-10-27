from django.shortcuts import render

# Create your views here.
from math import prod
from django.shortcuts import render, redirect, HttpResponse
from .models import Producto, NewUser, Comentario
from django.http import JsonResponse
import datetime
from InOut_app import logic, models
from collections import OrderedDict
from django.urls import reverse
from .forms import productoForm, Deleteform, actualizarProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

current_product = ''

#tipo = "mes"
#fecha = 'nulo'
#mes = 6
meses={
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',

}


def Registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellidos']
        usuario = request.POST['usuario']
        ciudad = request.POST['ciudad']
        direccion = request.POST['direccion']
        correo = request.POST['correo']
        clave = request.POST['clave']

        user = NewUser.objects.create_user(usuario, correo, clave)
        user.first_name = nombre
        user.last_name = apellido
        user.Ciudad = ciudad
        user.Direccion = direccion
        user.save()
        return render(request, "welcome.html")
    return render(request, "registro.html")


def pind(request, id_obj):
    global current_product
    if not request.user.is_authenticated:
        return redirect('welcome')
    p = Producto.objects.filter(id=id_obj)
    current_product = (p[0])
    comentarios =  list(Comentario.objects.filter(Producto_id=current_product.id))
    names = []
    for i in comentarios:
        names.append([((NewUser.objects.get(id= i.Usuario_id)).username),i.Comentario])
    print(names)
    if request.method == "POST":
        new_comment = models.Comentario(Usuario=request.user, Producto = current_product, Comentario=request.POST['coment'])
        new_comment.save()
        return redirect(pind, id_obj)
    return render(request, "pind.html", {'producto': p[0], 'comentarios': names})

def Ingreso(request):
    if request.method == "POST":
        
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        user = authenticate(request, username = usuario, password = clave)
        if user is not None:
            login(request, user)
            return redirect('productos')
        else:
            messages.info(request, "Correo y/o contraseña incorrectos")

    return render(request, "ingreso.html")


def Home(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    productos =  Producto.objects
    return render(request, "home.html", {"productos":productos})


def Usuario(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "usuario.html")


def Productos(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    productos =  Producto.objects
    return render(request, "productos.html", {"productos":productos})


def Opciones(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "opciones.html")

def Main(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "main.html")


def Welcome(request):

    return render(request, "welcome.html")


def get_data(request):
    data = {"sales":100,
            "customers":10,
    }
    return JsonResponse(data)


def registroProducto(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=productoForm()
    context={'form':form}
    if request.method == 'POST':
        form=productoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    return render(request, 'agregar.html', context)


def EliminarItem(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('borrar', kwargs={"nombre": nombre}))
    return render(request, 'borrar2.html', context)


def modificar(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    form=Deleteform()
    context={'form':form}
    if request.method == 'POST':
        form=Deleteform(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data.get("Nombre")
            return redirect(reverse('actualizar', kwargs={"nombre": nombre}))
    return render(request, 'modificar.html', context)


def actualizar(request, nombre):
    if not request.user.is_authenticated:
        return redirect('welcome')
    try:
        productoactualizar = Producto.objects.get(Nombre=nombre)
    except:
        return redirect('modificar')
    if request.method == "POST":
        nombre = request.POST["producto"]
        cantidad = request.POST["cantidad"]
        actualizarProducto(nombre,cantidad)
        return redirect('productos')
    context={'item':productoactualizar}
    return render(request, 'actualizar.html', context)



def eliminacionProducto(request, nombre):
    if not request.user.is_authenticated:
        return redirect('welcome')
    try:
        productoBorrar=Producto.objects.get(Nombre=nombre)
    except:
        return redirect('eliminar')
    if request.method == "POST":
        productoBorrar.delete()
        return redirect('productos')
    context={'item':productoBorrar}
    return render(request, 'borrar.html', context)


def logOut_request(request):
    logout(request)
    return redirect("welcome")

