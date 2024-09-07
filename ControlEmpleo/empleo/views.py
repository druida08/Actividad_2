from django.shortcuts import render, redirect
from .models import Empresa, OfertaEmpleo
from .forms import EmpresaForm, OfertaEmpleoForm

def registrar_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
    return render(request, 'empleo/registrar_empresa.html', {'form': form})

def registrar_oferta_empleo(request):
    if request.method == "POST":
        form = OfertaEmpleoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ofertas')
    else:
        form = OfertaEmpleoForm()
    return render(request, 'empleo/registrar_oferta.html', {'form': form})

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empleo/lista_empresas.html', {'empresas': empresas})

def lista_ofertas(request):
    ofertas = OfertaEmpleo.objects.all()
    return render(request, 'empleo/lista_ofertas.html', {'ofertas': ofertas})
