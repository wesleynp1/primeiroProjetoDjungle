from django.shortcuts import render, redirect

#from django.template import loader
#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
from django.core.exceptions import PermissionDenied

from loja.models import Produto, Cliente


def index(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()

    #template = loader.get_template('loja/index.html')# pega o template
    #return HttpResponse(template.render({ 'loja': loja }))

    return render(request, 'produtos/index.html', {"produtos": produtos, "clientes": clientes})

def add(request):
    if(request.method == 'GET'):
        return render(request, 'produtos/add.html')
    elif (request.method == 'POST'):
        Produto.objects.create(nome=request.POST["nome"], preco=request.POST["preco"])
        return redirect("loja:index")
    else:
        return redirect("loja:index")

def delete_form(request, produto_id):
    produto_para_deletar = Produto.objects.filter(id=produto_id).first()

    if produto_para_deletar is None:
        raise Http404
    else:
        return render(request, "produtos/delete.html", {"produto": produto_para_deletar})
def delete(request, produto_id):
    produto_para_deletar = Produto.objects.filter(id=produto_id).first()

    if produto_para_deletar is None:
        raise Http404
    else:
        produto_para_deletar.delete()
        return redirect("loja:index")

def edit_form(request, produto_id):
    produto = Produto.objects.filter(id=produto_id).first()
    return render(request, "produtos/edit.html", {"produto": produto})
def edit(request, produto_id):
    produto_para_editar = Produto.objects.filter(id=request.POST["id"]).first()

    if produto_para_editar is None:
        raise Http404
    else:
        produto_para_editar.nome = request.POST["nome"]
        produto_para_editar.preco = request.POST["preco"]
        produto_para_editar.save()
        return redirect("loja:index")

def detalhe(request, produto_id):
    try:
        produto = Produto.objects.filter(id=produto_id).first()
        return render(request, 'produtos/detalhe.html', {"produto": produto})
    except Produto.DoesNotExist:
        raise Http404("Desculpe, não temos esse produto")