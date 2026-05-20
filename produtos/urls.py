from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns =[
    path("", views.index, name="index"),
    path("detalhe/<int:produto_id>", views.detalhe, name="detalhe"),#não dê espaço dentro dos <>
    path("add", views.add, name="add"),
    path("delete/form/<int:produto_id>", views.delete_form, name="delete_form"),
    path("delete/<int:produto_id>", views.delete, name="delete"),
    path("edit/form/<int:produto_id>", views.edit_form, name="edit_form"),
    path("edit/<int:produto_id>", views.edit, name="edit"),
]