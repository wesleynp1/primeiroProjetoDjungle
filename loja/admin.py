from django.contrib import admin

# Register your models here.
from .models import Produto
from clientes.models import Cliente

admin.site.register(Produto)
admin.site.register(Cliente)

