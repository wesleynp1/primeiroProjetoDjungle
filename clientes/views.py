from .models import Cliente
from django.shortcuts import render, redirect


# Create your views here.
def add_form(request):
    return render(request,"clientes/add.html")


def add(request):
    Cliente.objects.create(
        cpf=request.POST["cpf"],
        nome = request.POST["nome"],
        telefone= request.POST["telefone"]
    )

    return redirect("loja:index")


def delete_form(request, cpf : str):
    return render(request,"clientes/delete.html",{"cliente":Cliente.objects.get(cpf=cpf)})


def delete(request,cpf : str):
    Cliente.objects.get(cpf=cpf).delete()
    return redirect("loja:index")


def edit_form(request,cpf : str):
    return render(request,"clientes/edit.html",{"cliente":Cliente.objects.get(cpf=cpf)})


def edit(request,cpf : str):
    cliente = Cliente.objects.get(cpf=cpf)

    if "nome" in request.POST:
        cliente.nome = request.POST["nome"]

    if "telefone" in request.POST:
        cliente.telefone = request.POST["telefone"]

    cliente.save()

    return redirect("loja:index")