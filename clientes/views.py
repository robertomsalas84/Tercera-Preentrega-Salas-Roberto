from django.shortcuts import render
from .models import Cliente, Producto, Sucursal
from .forms import ClienteForm, ProductoForm, SucursalForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "clientes/home.html")

def cliente(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "clientes/cliente.html", contexto)


def producto(request):
    return render(request, "clientes/producto.html")

def sucursal(request):
    return render(request, "clientes/sucursal.html")

def clienteForm(request):
    if request.method == 'POST':
        cliente = Cliente(nombre=request.POST['nombre'],
                          dni=request.POST['dni'],
                          ciudad=request.POST['ciudad'],
                          email=request.POST['email'])
        cliente.save()
        return HttpResponse("Se grabó con exito el nuevo cliente")
    return render(request, "clientes/clienteForm.html")

def clienteForm2(request):
    if request.method == 'POST':
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_dni = miForm.cleaned_data.get('dni')
            cliente_ciudad = miForm.cleaned_data.get('ciudad')
            cliente_email = miForm.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre,
                              dni=cliente_dni,
                              ciudad=cliente_ciudad,
                              email=cliente_email)
            cliente.save()
            return render(request, "clientes/base.html")
    else:
        miForm = ClienteForm()
    
    return render(request, "clientes/clienteForm2.html", {"form": miForm})

def buscarCliente(request):
    return render(request, "clientes/buscarcliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'clientes': clientes, 'titulo': f'Reporte de Clientes que tienen como patrón: {patron}'}
        return render(request, "clientes/cliente.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")


def productoForm(request):
    if request.method == 'POST':
        producto = Producto(producto=request.POST['producto'],
                          meses_garantia=request.POST['meses_garantia'],
                          promocion=request.POST['promocion'])
        producto.save()
        return HttpResponse("Se grabó con exito el nuevo producto")
    return render(request, "clientes/productoForm.html")

def productoForm2(request):
    if request.method == 'POST':
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_producto = miForm.cleaned_data.get('producto')
            producto_meses_garantia = miForm.cleaned_data.get('meses_garantia')
            producto_promocion = miForm.cleaned_data.get('promocion')
            producto = Producto(producto=producto_producto,
                              meses_garantia=producto_meses_garantia,
                              promocion=producto_promocion)
            producto.save()
            return render(request, "clientes/base.html")
    else:
        miForm = ProductoForm()
    
    return render(request, "clientes/productoForm2.html", {"form": miForm})



def sucursalForm(request):
    if request.method == 'POST':
        sucursal = Sucursal(sucursal=request.POST['numero_sucursal'],
                          ciudad=request.POST['ciudad'],
                          metros_cuadrados=request.POST['metros_cuadrados'])
        sucursal.save()
        return HttpResponse("Se grabó con exito el nuevo producto")
    return render(request, "clientes/sucursalForm.html")

def sucursalForm2(request):
    if request.method == 'POST':
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursal_numero_sucursal = miForm.cleaned_data.get('numero_sucursal')
            sucursal_ciudad = miForm.cleaned_data.get('ciudad')
            sucursal_metros_cuadrados = miForm.cleaned_data.get('metros_cuadrados')
            sucursal = Sucursal(numero_sucursal=sucursal_numero_sucursal,
                              ciudad=sucursal_ciudad,
                              metros_cuadrados=sucursal_metros_cuadrados)
            sucursal.save()
            return render(request, "clientes/base.html")
    else:
        miForm = SucursalForm()
    
    return render(request, "clientes/sucursalForm2.html", {"form": miForm})


