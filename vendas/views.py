from django.shortcuts import render, redirect
from .models import Venda
from loja.models import Cliente, Produto

def index(request):
    return render(request,"vendas/index.html",{"vendas" : Venda.objects.all()})

def add_form(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    return  render(request,"vendas/add.html",{"produtos" : produtos, "clientes" : clientes})

def add(request):
    produto = Produto.objects.get(id=request.POST["produto"])
    cliente = Cliente.objects.get(cpf=request.POST["cliente"])
    Venda.objects.create(produto=produto, cliente=cliente, quantidade=request.POST["quantidade"])
    return redirect("vendas:index")

def delete_form(request, id):
    venda = Venda.objects.get(id=id)
    return render(request,"vendas/delete.html",{"venda" : venda})

def delete(request, id):
    Venda.objects.get(id=id).delete()
    return redirect("vendas:index")

def edit_form(request, id):
    venda = Venda.objects.get(id=id)
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()

    return render(request,"vendas/edit.html",{"venda" : venda,"produtos" : produtos, "clientes" : clientes})

def edit(request, id):
    venda = Venda.objects.get(id=id)
    venda.quantidade = request.POST["quantidade"]
    venda.cliente = Cliente.objects.get(cpf=request.POST["cliente"])
    venda.produto = Produto.objects.get(id=request.POST["produto"])
    venda.save()
    return redirect("vendas:index")
