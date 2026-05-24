from django.contrib import admin

# Register your models here.
from .models import Produto
from .models import Cliente

admin.site.register(Produto)
admin.site.register(Cliente)

