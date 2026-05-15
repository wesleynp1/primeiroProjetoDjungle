from django.http import HttpResponse

def index(request):
    return HttpResponse("Seja muito bem vindo ao meu site, aqui estarão os produtos...")