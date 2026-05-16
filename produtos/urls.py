from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("detalhe/<int:produto_id>", views.detalhe, name="detalhe")#não dê espaço dentro dos <>

]