from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
    path('form/add', views.add_form, name="add_form"),
    path('add', views.add, name="add"),
    path('form/delete/<str:cpf>', views.delete_form, name="delete_form"),
    path('delete/<str:cpf>', views.delete, name="delete"),
    path('form/edit/<str:cpf>', views.edit_form, name="edit_form"),
    path('edit/<str:cpf>', views.edit, name="edit"),
]