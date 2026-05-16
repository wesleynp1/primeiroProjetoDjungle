from django.http import HttpResponse

from produtos.models import Produto


def index(request):
    p = Produto.objects.all()
    mensagem = "Produtos:<br>"
    for produto in p:
        mensagem += f' <a href="detalhe/{produto.id}"> {produto.__str__()} </a><br>'

    return HttpResponse(_vira_html(mensagem))
def detalhe(request, produto_id):
    produto = Produto.objects.filter(id=produto_id).first()
    if produto is not None:
        mensagem = f'Detalhes:<br>{produto.nome} é um excelente smartphone em promoção de {produto.preco*2} por {produto.preco} <br>'
        return HttpResponse(_vira_html(mensagem))
    else:
        return HttpResponse("Ocorreu um erro!")

def _vira_html(mensagem : str):
    return f'<!DOCTYPE html><html><head></head><body> <h1>WELLCOME TO THE DJUNGLE!!!</h1> <p>{mensagem}</p></body></html>'