from .models import Usuario, Capacidad, Parqueadero
from django.shortcuts import render, redirect
from .forms import CapacidadForm
from django.contrib.auth.decorators import login_required
import json, requests


def index(request):
    return render(request, 'index.html')

@login_required
def UsuarioList(request):
    queryset = Usuario.objects.all().order_by('-time')[:10]
    context = {
        'usuario_list': queryset
    }
    return render(request, 'Usuario/usuarios.html', context)

@login_required
def CapacidadList(request):
    queryset = Capacidad.objects.all()
    role = getRole(request)
    context = {
        'capacidad_list': queryset,
        'role': role
    }
    print("role= ", role)
    return render(request, 'Capacidad/capacidadess.html', context)

@login_required
def CapacidadEdit(request, id_threshold):
    capacidad= Capacidad.objects.get(variable=id_capacidad)
    varName = Variable.objects.get(id=id_capacidad)
    if request.method == 'GET':
        form = CapacidadForm(instance=capacidad)
    else:
        form =CapacidadForm(request.POST, instance=capacidad)
        if form.is_valid():
            form.save()
        return redirect('capacidadList')
    role = getRole(request)
    return render(request, 'Capacidad/capacidadEdit.html', {'form':form, 'variable':varName.name, 'role': role})