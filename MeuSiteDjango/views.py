from django.http import HttpResponse

def index(request):
    return HttpResponse(_vira_html('Vá para <a href="loja">loja</a> ou <a href="vendas">vendas</a>'))

def _vira_html(mensagem : str):
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body> 
        <h1>WELLCOME TO THE DJUNGLE!!!</h1> 
        <p>{mensagem}</p>
    </body>
    </html>
    '''